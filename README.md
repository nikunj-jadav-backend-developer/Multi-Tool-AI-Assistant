# 🤖 Multi-Tool AI Assistant

A production-ready AI Assistant built using Python that combines Retrieval-Augmented Generation (RAG), memory, web search, and multiple AI tools into a single application.

The project follows enterprise software engineering practices including GitHub Flow, CI/CD, Azure App Service deployment, Azure Key Vault secret management, and OIDC authentication.

---

# 🚀 Features

- 🔍 Retrieval-Augmented Generation (RAG)
- 💬 Conversation Memory
- 🧠 Multi-step AI Agent
- 🌐 Web Search Tool
- 📄 Document Question Answering
- 🗂 Modular Architecture
- 🔐 Azure Key Vault Integration
- ☁ Azure App Service Deployment
- ⚙ GitHub Actions CI/CD
- 🔑 OIDC Authentication (Passwordless Azure Login)
- 📈 Production-ready Project Structure

---

# 🛠 Tech Stack

## Programming Language

- Python 3.12

## AI Frameworks

- LangGraph
- LangChain
- Groq
- OpenAI Compatible APIs

## RAG

- ChromaDB
- Sentence Transformers
- Recursive Text Splitter

## Frontend

- Streamlit

## Cloud

- Microsoft Azure
    - App Service
    - Key Vault
    - Managed Identity

## CI/CD

- GitHub Actions
- OIDC Authentication

## Others

- python-dotenv
- Azure Identity
- Azure Key Vault Secrets
- Requests

---

# 📂 Project Structure

```
Multi-Tool-AI-Assistant
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── src/
│   └── app/
│       ├── config/
│       ├── infrastructure/
│       ├── memory/
│       ├── tools/
│       ├── utils/
│       └── main.py
│
├── tests/
│
├── data/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Local Setup

## Clone Repository

```bash
git clone https://github.com/nikunj-jadav-backend-developer/Multi-Tool-AI-Assistant.git

cd Multi-Tool-AI-Assistant
```

---

## Create Virtual Environment

Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

## Configure Environment

Create

```
.env
```

Example

```env
GROQ_API_KEY=xxxxxxxxxxxxxxxx

OPEN_WEATHER_API_KEY=xxxxxxxxxxxx

LLM_MODEL=llama-3.1-8b-instant

TEMPERATURE=0.4
```

---

## Run Application

```bash
streamlit run src/app/main.py
```

---

# ☁ Azure Deployment

This project is deployed using

- Azure App Service
- Azure Key Vault
- Managed Identity
- GitHub Actions
- OIDC Authentication

---

# Azure Architecture

```
GitHub
    │
    ▼
GitHub Actions

    │
    ▼
Azure Login (OIDC)

    │
    ▼
Azure App Service

    │
Managed Identity

    │
    ▼
Azure Key Vault

    │
    ▼
Secrets

    │
    ▼
Application
```

---

# Secret Management

Sensitive values are stored inside Azure Key Vault.

Examples

- GROQ_API_KEY
- OPEN_WEATHER_API_KEY

Non-sensitive configuration is stored in Azure App Service Configuration.

Examples

- LLM_MODEL
- TEMPERATURE

---

# CI/CD Pipeline

Continuous Integration

```
Push

↓

Install Dependencies

↓

Lint

↓

Run Tests

↓

Success
```

Continuous Deployment

```
CI Success

↓

Azure Login (OIDC)

↓

Deploy to Azure App Service

↓

Application Restart
```

---

# Git Workflow

```
main

develop

feature/*
```

Example

```
feature/rag

feature/key-vault

feature/azure-app-service

feature/github-actions

feature/deployment
```

---

# Security

✔ Azure Key Vault

✔ Managed Identity

✔ OIDC Authentication

✔ GitHub Secrets

✔ No API Keys committed to Git

---

# Future Improvements

- Azure AI Search
- Azure Cosmos DB
- Azure App Configuration
- Docker Support
- Terraform Infrastructure
- Monitoring
- Application Insights
- Prompt Versioning

---

# Author

Nikunj Jadav

Senior Backend Developer (PHP/WordPress/Shopify)

Transitioning into Python Backend & AI Engineering

GitHub

https://github.com/nikunj-jadav-backend-developer

LinkedIn

https://www.linkedin.com/in/nikunj-jadav-backend-developer/

Preview URL 

https://apps-srvapi-development-svkc7t.azurewebsites.net/

---

# License

MIT License