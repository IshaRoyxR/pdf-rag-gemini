# PDF RAG System — Multi-Format Intelligent Document Understanding Platform

A production-ready full-stack Retrieval-Augmented Generation (RAG) platform that enables users to upload PDF, DOCX, and PowerPoint documents and interact with them using context-aware AI conversations.

Built using FastAPI, LangChain, ChromaDB, React, Docker, Ollama, OpenAI, and Gemini.

---

# Overview

This project demonstrates how modern AI systems combine:
- semantic retrieval
- vector databases
- conversational memory
- multi-provider LLM orchestration
- scalable backend architecture

to build intelligent document understanding systems.

Instead of building a basic chatbot wrapper, this project focuses on production-oriented AI infrastructure and full-stack engineering principles.

---

# Core Capabilities

- Multi-format document ingestion (PDF, DOCX, PPT/PPTX)
- Retrieval-Augmented Generation (RAG)
- Semantic search using vector embeddings
- Context-aware conversational AI
- Multi-provider LLM integration
- Source-cited answer generation
- Conversational memory support
- Modular backend architecture
- Dockerized full-stack deployment
- Production-ready API workflows

---

# System Architecture

```text
User
│
▼
React + Vite Frontend
│
▼
FastAPI Backend
│
├── Document Processing Pipeline
│ ├── PDF Loader
│ ├── DOCX Loader
│ └── PPT Extractor
│
▼
Text Chunking + Embedding Generation
│
▼
ChromaDB Vector Store
│
▼
Semantic Retriever
│
▼
LLM Provider Layer
│ ├── Ollama
│ ├── OpenAI
│ └── Gemini
│
▼
Conversation Memory + Context Injection
│
▼
Grounded AI Response with Source Citations
```

---

# Tech Stack

## Backend
- FastAPI
- LangChain
- ChromaDB
- Python
- Docker
- Ollama
- OpenAI API
- Gemini API

## Frontend
- React
- Vite
- TypeScript
- Tailwind CSS
- shadcn/ui

---

# Key Engineering Features

## AI / RAG Features
- Retrieval-Augmented Generation (RAG)
- Semantic similarity search
- Embedding-based retrieval
- Conversational memory
- Multi-turn contextual Q&A
- Source-aware answer generation
- Relevance scoring
- Multi-provider LLM orchestration

## Backend Engineering
- Modular FastAPI architecture
- Async API workflows
- Background document processing
- Provider abstraction layer
- Factory design pattern
- Environment-based configuration
- Production-ready Docker setup

## Frontend Features
- Modern React + Vite UI
- Drag-and-drop document upload
- Conversation session management
- Multi-mode AI interaction
- Source citation display
- Provider selection interface
- Responsive UI components

---

# Supported LLM Providers

- Ollama
- OpenAI
- Gemini

The provider layer is dynamically configurable and supports switching between local and cloud-hosted LLMs.

---

# Project Structure

```text
pdf-rag-gemini/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── rag/
│   │   ├── providers/
│   │   ├── memory/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── components/
│
├── data/
├── docker-compose.yml
├── .env.example
├── LICENSE
└── README.md
```

---

# Setup Guide

## 1. Clone Repository

```bash
git clone https://github.com/IshaRoyxR/pdf-rag-gemini.git

cd pdf-rag-gemini
```

---

## 2. Install Ollama

Download:
https://ollama.com/download

Pull model:

```bash
ollama pull llama3
```

Start Ollama:

```bash
ollama serve
```

---

## 3. Configure Environment Variables

Create `.env` file:

```bash
copy .env.example .env
```

Update API keys if required.

---

# 4. Start Full Stack Application

```bash
docker compose up --build
```

---

# Application URLs

Frontend:
```text
http://localhost:8080
```

Backend:
```text
http://localhost:8000
```

Swagger API Docs:
```text
http://localhost:8000/docs
```

---

# Example Use Cases

- AI document assistants
- Enterprise knowledge retrieval
- Research paper Q&A systems
- Internal AI copilots
- Technical documentation assistants
- Conversational knowledge systems

---

# Future Improvements

- Hybrid search (BM25 + vector search)
- Authentication & user management
- Streaming LLM responses
- Multi-document reasoning
- Kubernetes deployment
- Redis caching
- Cloud deployment support
- Agentic workflows

---

# License

Apache License 2.0