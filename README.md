# PDF RAG Application (Gemini + LangChain)

## Overview
This project is a Retrieval-Augmented Generation (RAG) system that allows users to upload PDF documents and ask questions based on their content.
It supports both text-based and scanned PDFs.

The project is built with a clean, modular structure following industry best practices.

## Tech Stack
- Gemini (Google Generative AI)
- LangChain
- FastAPI (Backend)
- ChromaDB (Vector Database)
- React (Frontend – planned)

## Project Structure

pdf-rag-gemini/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── llm/
│   │   ├── rag/
│   │   ├── config.py
│   │   └── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
├── .gitignore
└── README.md

## Setup Instructions

```bash
git clone https://github.com/IshaRoyxR/pdf-rag-gemini.git
cd pdf-rag-gemini/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
