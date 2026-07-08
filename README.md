# 🚀 Infra AI Assistant

An AI-powered Infrastructure Repository Assistant that analyzes DevOps repositories using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

The assistant understands infrastructure repositories containing Docker, Kubernetes, Terraform, Nginx, CI/CD pipelines, environment files, logs, and configuration files. Users can upload an infrastructure repository as a ZIP file and ask natural language questions to receive intelligent, context-aware explanations and recommendations.

---

# ✨ Features

- 📦 Upload complete infrastructure repositories as ZIP files
- 🤖 AI-powered repository analysis using RAG
- ☸️ Kubernetes manifest analysis
- 🐳 Docker & Docker Compose analysis
- 🌍 Terraform configuration analysis
- 🌐 Nginx configuration analysis
- 🔄 Basic CI/CD workflow analysis
- 🔐 Infrastructure security analysis
- 🔗 Relationship detection between infrastructure components
- 📄 Repository summary generation
- 🧠 Multi-provider LLM support (Gemini, Ollama, OpenAI)
- 💬 Interactive chat interface
- 🐳 Dockerized deployment

---

# 🏗️ Architecture

```text
                    User
                      │
                      ▼
             React Frontend (Vite)
                      │
                 FastAPI Backend
                      │
             Upload Repository ZIP
                      │
             Extract Repository Files
                      │
              Repository Parser
      ┌──────────┬──────────┬──────────┐
      ▼          ▼          ▼          ▼
 Kubernetes   Docker    Terraform   Nginx
      │
      ▼
 Relationship Engine
      │
      ▼
 Security Analyzer
      │
      ▼
 Text Chunking
      │
      ▼
 Chroma Vector Database
      │
      ▼
 LangChain Retriever
      │
      ▼
 Gemini / Ollama / OpenAI
      │
      ▼
 AI Generated Response
```

---

# 🛠️ Tech Stack

## Backend

- FastAPI
- Python
- LangChain
- ChromaDB
- Docker

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui

## AI

- Gemini
- Ollama
- OpenAI

---

# 📂 Project Structure

```text
infra-ai-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── analyzer/
│   │   ├── parsers/
│   │   ├── prompts/
│   │   ├── rag/
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│
├── docker-compose.yml
├── README.md
├── RESULT.md
├── LICENSE
└── .env.example
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/IshaRoyxR/infra-ai-assistant.git

cd infra-ai-assistant
```

---

## Install Ollama

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

## Start Ollama

```bash
ollama serve
```

---

## Configure Environment

Create:

```text
.env
```

using:

```text
.env.example
```

Add your Gemini/OpenAI API keys if required.

---

## Run Application

```bash
docker compose up --build
```

---

# 🌐 Application URLs

Frontend

```
http://localhost:8080
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# 💬 Example Questions

- Explain this repository.
- Explain the deployment flow.
- Find security issues.
- Explain the Dockerfile.
- Explain the Kubernetes resources.
- Explain Terraform resources.
- Which services communicate?
- What ports are exposed?
- How does Nginx route traffic?
- Suggest infrastructure improvements.

---

# 📸 Demo

Upload an infrastructure repository ZIP and interact with the assistant using natural language to analyze Docker, Kubernetes, Terraform, Nginx, and CI/CD configurations.

---

# 🔮 Future Improvements

- Helm Chart support
- AWS CloudFormation support
- Azure ARM/Bicep support
- Better security rule engine
- Multi-repository comparison
- Streaming responses
- Authentication
- Cloud deployment

---

# 📄 License

Apache License 2.0