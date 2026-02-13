📄 PDF RAG System (Multi-Format Document Intelligence)

A full-stack Retrieval-Augmented Generation (RAG) system that allows users to upload documents (PDF, Word, PowerPoint) and ask intelligent questions based on their content.

Built using FastAPI, LangChain, ChromaDB, Gemini/Ollama, and React.

🎯 Why This Project?

Modern applications require intelligent document understanding.

This project demonstrates:

How to build a complete RAG pipeline

How to process multiple document formats

How to store semantic embeddings in a vector database

How to retrieve relevant context for LLMs

How to build a full backend + frontend system

How to structure a production-ready project

This is not just a demo — it is a complete document Q&A system.

🧠 How It Works (Architecture Flow)
User
  │
  ▼
React Frontend (Upload / Chat UI)
  │
  ▼
FastAPI Backend
  │
  ├── File Router
  │      ├── PDF Loader
  │      ├── DOCX Loader
  │      └── PPT Extractor
  │
  ▼
Text Splitter
  │
  ▼
Embedding Generator (Gemini / Ollama)
  │
  ▼
ChromaDB (Vector Store)
  │
  ▼
Retriever
  │
  ▼
LLM (Gemini / Ollama)
  │
  ▼
Final Answer Returned to User

🏗 Project Architecture
pdf-rag-gemini/
│
├── backend/
│   ├── app/
│   │   ├── api/        # API endpoints
│   │   ├── core/       # File handling & utilities
│   │   ├── rag/        # RAG pipeline logic
│   │   ├── llm/        # LLM integrations
│   │   └── main.py     # FastAPI entry point
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── public/
│
├── data/
│   ├── uploads/        # Uploaded files
│   └── chroma_db/      # Vector DB (auto-generated)
│
├── docker-compose.yml
├── .env.example
└── README.md

🚀 Features
Backend

Multi-format support (PDF, DOCX, PPT)

Automatic file type detection

Background processing

Status tracking

Vector database persistence (ChromaDB)

REST API endpoints

Document list & delete endpoints

Gemini and Ollama support

Frontend

Drag-and-drop upload

Upload progress tracking

Document library view

File-type icons

Delete document button

Chat interface


⚙️ Complete Setup Guide (Backend + Frontend)
1️⃣ Clone Repository
git clone https://github.com/IshaRoyxR/pdf-rag-gemini.git
cd pdf-rag-gemini

🖥 Backend Setup

Step 1: Create Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

Step 2: Install Dependencies
pip install -r backend/requirements.txt

Step 3: Create Environment File
Create a .env file in the root directory:
GOOGLE_API_KEY=your_google_api_key
MODEL_NAME=gemini-pro

Step 4: Run Backend Server
uvicorn backend.app.main:app --reload


Backend will run at:
http://127.0.0.1:8000


You can check:
http://127.0.0.1:8000/docs


for Swagger API documentation.

🎨 Frontend Setup

Open a new terminal:
cd frontend
npm install
npm start


Frontend runs at:

http://localhost:3000


Make sure backend is running before starting frontend.

🐳 Docker Setup (Optional)

To run full application using Docker:
docker-compose up --build