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


⚙️ Complete Setup Guide (Actual Working Version)

1️⃣ Clone Repository
git clone https://github.com/IshaRoyxR/pdf-rag-gemini.git
cd pdf-rag-gemini

🧠 Step 2: Install and Run Ollama (Required)

Download Ollama from:

https://ollama.com/download

After installation, pull the model:

ollama pull llama3       #Run


Start Ollama (if not auto-running):

ollama serve              #Run

🔐 Step 2: Create Environment File (Required)

Before starting Docker, create a .env file in the project root.

You can copy the example file:

copy .env.example .env


(Windows)

Or:

cp .env.example .env


(Mac/Linux)

Then edit .env if needed.

🐳 Step 4: Start Backend (Docker)

Stop previous containers:

docker compose down                                      #Run


Build backend:

docker compose build backend                            #Run


Start backend:

docker compose up                                       #Run


Backend runs at:

http://localhost:8000


Check API docs:

http://localhost:8000/docs

🎨 Step 5: Start Frontend

Open new terminal:

cd frontend                  
npm install
npm start


Frontend runs at:

http://localhost:3000

🧠 System Architecture (Your Real Setup)
User
   ↓
React Frontend (localhost:3000)
   ↓
FastAPI Backend (Docker container)
   ↓
Ollama (Local Model Server)
   ↓
ChromaDB (Vector Store)
   ↓
Response to User