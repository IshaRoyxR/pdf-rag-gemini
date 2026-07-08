from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import zipfile
import shutil

from app.rag.splitter import split_text
from app.rag.vector_store import store_chunks

from app.parsers.repository_parser import RepositoryParser
from app.analyzer.relationship_engine import RelationshipEngine
from app.analyzer.security_analyzer import SecurityAnalyzer
from app.analyzer.repository_summary import RepositorySummary

router = APIRouter()

UPLOAD_DIR = "uploads"
EXTRACT_DIR = os.path.join(UPLOAD_DIR, "repository")

os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_file_type(filename: str) -> str:
    filename = filename.lower()

    if filename == "dockerfile":
        return "Dockerfile"

    if filename.endswith((".yaml", ".yml")):
        return "Kubernetes YAML"

    if filename.endswith(".tf"):
        return "Terraform"

    if filename.endswith(".conf"):
        return "Nginx Configuration"

    if filename.endswith(".properties"):
        return "Application Properties"

    if filename.endswith(".log"):
        return "Application Log"

    if filename.endswith(".env"):
        return "Environment File"

    if filename.endswith(".sh"):
        return "Shell Script"

    if filename.endswith(".md"):
        return "Markdown"

    if filename.endswith(".txt"):
        return "Text File"

    return "Unknown"


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # Accept only ZIP repositories
    if not file.filename.lower().endswith(".zip"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a ZIP repository."
        )

    # Remove previously extracted repository
    if os.path.exists(EXTRACT_DIR):
        shutil.rmtree(EXTRACT_DIR)

    os.makedirs(EXTRACT_DIR, exist_ok=True)

    zip_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded ZIP
    with open(zip_path, "wb") as f:
        f.write(await file.read())

    # Extract ZIP
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(EXTRACT_DIR)
    except zipfile.BadZipFile:
        raise HTTPException(
            status_code=400,
            detail="Invalid ZIP file."
        )

    supported_extensions = {
        ".yaml",
        ".yml",
        ".tf",
        ".conf",
        ".properties",
        ".log",
        ".env",
        ".sh",
        ".md",
        ".txt",
    }

    documents = []

    # Read every supported infrastructure file
    for root, dirs, files in os.walk(EXTRACT_DIR):

        for filename in files:

            filepath = os.path.join(root, filename)

            extension = os.path.splitext(filename)[1].lower()

            # Dockerfile has no extension
            if filename == "Dockerfile":
                supported = True
            else:
                supported = extension in supported_extensions

            if not supported:
                continue

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                relative_path = os.path.relpath(filepath, EXTRACT_DIR)

                file_type = get_file_type(filename)

                documents.append(
                    f"""
==================================================
File: {relative_path}
Type: {file_type}
==================================================

Content:

{content}
"""
                )

            except Exception:
                continue

    # ---------------------------------------
    # Repository Parsing
    # ---------------------------------------

    repository_parser = RepositoryParser()
    repository = repository_parser.parse_repository(EXTRACT_DIR)

    # Repository Summary
    repository_summary = RepositorySummary()
    summary = repository_summary.generate(repository)

    # Relationship Analysis
    relationship_engine = RelationshipEngine()
    relationships = relationship_engine.build(repository)

    # ---------------------------------------
    # Security Analysis
    # ---------------------------------------

    security_analyzer = SecurityAnalyzer()
    security_issues = security_analyzer.analyze_repository(EXTRACT_DIR)

    relationship_text = "\n".join(
        str(item) for item in relationships
    )

    security_text = "\n".join(
        str(item) for item in security_issues
    )

    full_text = f"""
==============================
Repository Summary
==============================

{summary}

==============================
Repository Analysis
==============================

{relationship_text}

==============================
Security Analysis
==============================

{security_text}

==============================
Repository Files
==============================

{''.join(documents)}
"""

    chunks = split_text(full_text)

    store_chunks(chunks, file.filename)

    return {
        "status": "success",
        "repository": file.filename,
        "summary": summary,
        "files_processed": len(documents),
        "relationships_found": len(relationships),
        "security_issues": len(security_issues),
        "chunks": len(chunks),
    }