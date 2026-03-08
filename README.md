# 📄 PDF RAG System (Multi-Format Document Intelligence)

A full-stack Retrieval-Augmented Generation (RAG) system that allows users to upload documents (PDF, Word, PowerPoint) and ask intelligent questions based on their content.

Built using FastAPI, LangChain, ChromaDB, Gemini/Ollama/OpenAI, and React.

---

# 🎯 Why This Project?

Modern applications require intelligent document understanding.

This project demonstrates:

- How to build a complete RAG pipeline
- How to process multiple document formats
- How to store semantic embeddings in a vector database
- How to retrieve relevant context for LLMs
- How to build a full backend + frontend system
- How to structure a production-ready project
- How to support multiple LLM providers dynamically
- How to implement conversational memory in document QA systems

This is not just a demo — it is a complete intelligent document Q&A system.

---

# 🧠 How It Works (Architecture Flow)

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
Embedding Generator (Ollama / OpenAI / Gemini)  
│  
▼  
ChromaDB (Vector Store)  
│  
▼  
Retriever  
│  
▼  
LLM Provider Layer  
│      ├── Ollama  
│      ├── OpenAI  
│      └── Gemini  
│  
▼  
Conversation Memory + Context  
│  
▼  
Final Answer Returned to User (with Sources)

---

# 🏗 Project Architecture


pdf-rag-gemini/
│
├── backend/
│ ├── app/
│ │ ├── api/ # API endpoints
│ │ ├── core/ # File handling & utilities
│ │ ├── rag/ # RAG pipeline logic
│ │ ├── memory/ # Conversation memory
│ │ ├── providers/ # LLM provider implementations
│ │ └── main.py # FastAPI entry point
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ └── layouts/
│ └── public/
│
├── data/
│ ├── uploads/
│ ├── conversations/
│ └── chroma_db/
│
├── docker-compose.yml
├── .env.example
└── README.md


---

# 🚀 Features

### Backend

- Multi-format document support (PDF, DOCX, PPT)
- PowerPoint extraction using **python-pptx**
- Word document extraction using **python-docx**
- Automatic file type detection and routing
- Background document processing with status tracking
- Vector database persistence using **ChromaDB**
- Retrieval-Augmented Generation (RAG) pipeline
- Document metadata tracking (page / slide numbers)
- Relevance score calculation for retrieved results
- Source extraction and excerpt generation from documents
- Conversation memory using **LangChain ConversationBufferWindowMemory**
- File-based conversation persistence
- Conversation CRUD API endpoints
- Document list endpoint (`GET /api/documents`)
- Document delete endpoint (`DELETE /api/documents/{id}`)
- Multiple interaction modes (Q&A, Summary, Completion)
- Mode-specific prompt templates
- Provider-based LLM architecture
- Support for multiple LLM providers:
  - Ollama
  - OpenAI
  - Gemini
- Provider factory pattern for dynamic provider selection
- Environment-based provider configuration

### Frontend

- Drag-and-drop document upload interface
- Upload progress indicator
- Document list view with processing status
- File type icons (PDF/PPT/DOC)
- Delete document functionality
- Chat interface for document questions
- Conversation session management
- Sidebar conversation list
- Switch between conversations
- Conversation history display
- New conversation creation
- Delete conversation option
- Multiple interaction mode selector
- UI indicators for selected mode
- Source citation display
- Document name and page/slide reference display
- Relevance score visualization
- Provider status indicator
- Active model/provider display

---

# ⚙️ Complete Setup Guide (Actual Working Version)

## 1️⃣ Clone Repository


git clone https://github.com/IshaRoyxR/pdf-rag-gemini.git

cd pdf-rag-gemini


---

# 🧠 Step 2: Install and Run Ollama (Required)

Download Ollama:

https://ollama.com/download

Pull the model:


ollama pull llama3


Start Ollama if needed:


ollama serve


---

# 🔐 Step 3: Create Environment File

Before starting Docker, create a `.env` file in the project root.


copy .env.example .env


Edit `.env` if needed.

---

# 🐳 Step 4: Start Backend (Docker)

Stop previous containers:


docker compose down


Build backend:


docker compose build backend


Start backend:


docker compose up


Backend runs at:


http://localhost:8000


Check API documentation:


http://localhost:8000/docs


---

# 🎨 Step 5: Start Frontend

Open a new terminal:


cd frontend
npm install
npm start


Frontend runs at:


http://localhost:3000


---

# 🧠 System Architecture (Runtime Flow)

User  
↓  
React Frontend (localhost:3000)  
↓  
FastAPI Backend (Docker container)  
↓  
Retriever + Conversation Memory  
↓  
LLM Provider (Ollama / OpenAI / Gemini)  
↓  
ChromaDB Vector Store  
↓  
Answer with Source Citations