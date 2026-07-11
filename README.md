# 🤖 Multi-Tool AI Assistant (LangGraph + Groq)

A production-ready AI assistant built using **LangGraph**, **Groq LLM**, and a modular microservices architecture.

The system combines deterministic routing, intelligent tool orchestration, and a separate Retrieval-Augmented Generation (RAG) service. It is designed for scalable, cloud-native deployment using **Microsoft Azure**, **Terraform**, and **GitHub Actions**.

---

# 🚀 Features

## 🧠 Intelligent Routing

- Rule-based intent detection
- Regex-based classification
- LLM fallback classifier
- LangGraph conditional execution
- State-aware workflow orchestration

---

## 🧮 Deterministic Tools

- Calculator Tool
- Weather Tool
- Date & Time Tool
- Wikipedia Tool

---

## 📚 RAG Microservice

- FastAPI-based REST API
- LlamaIndex
- Semantic document retrieval
- Vector indexing
- Embedding search

---

## ⚡ Performance & Cost Optimization

- Deterministic routing
- Reduced LLM calls
- Configurable recursion limits
- Dynamic model selection (8B / 70B)

---

## ☁ Cloud Deployment

- Azure App Service
- Azure Key Vault
- Managed Identity
- Azure RBAC
- GitHub Actions Deployment
- Infrastructure as Code using Terraform

---

# 🏗 Architecture

```text
                        GitHub

                           │

                           ▼

                  GitHub Actions

                           │

                           ▼

                 Azure App Service

                           │

                  Managed Identity

                           │

          ┌────────────────┴──────────────┐

          ▼                               ▼

   Azure Key Vault                App Settings

          │

          ▼

   Multi-Tool AI Assistant

          │

    ┌─────┼──────────┐

    ▼     ▼          ▼

 Weather  Wiki      Calculator

          │

          ▼

      RAG Service

          │

          ▼

     LlamaIndex

          │

          ▼

      Groq LLM
```

---

# 🧰 Tech Stack

## AI

- LangGraph
- LangChain
- Groq LLM
- LlamaIndex

## Backend

- Python 3.12
- FastAPI
- Uvicorn
- Gunicorn

## Cloud

- Microsoft Azure
- Azure App Service
- Azure Key Vault
- Managed Identity

## Infrastructure

- Terraform
- Azure CLI
- GitHub Actions

## Vector Search

- HuggingFace Embeddings
- LlamaIndex

## Database

- MongoDB

## Quality

- Ruff
- Black
- Pytest

---

# 📂 Project Structure

```text
Multi-Tool-AI-Assistant/

├── app/
│   ├── api/
│   ├── core/
│   ├── graph/
│   ├── prompts/
│   ├── services/
│   ├── tools/
│   └── main.py
│
├── rag-service/
│
├── terraform/
│   ├── app-service.tf
│   ├── key-vault.tf
│   ├── resource-group.tf
│   ├── role-assignment.tf
│   └── ...
│
├── .github/
│   └── workflows/
│
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

# ⚙ Local Development

## Clone

```bash
git clone https://github.com/<username>/Multi-Tool-AI-Assistant.git

cd Multi-Tool-AI-Assistant
```

---

## Install Dependencies

```bash
poetry install
```

Activate

```bash
poetry shell
```

---

## Local Environment

Create `.env`

```env
GROQ_API_KEY=

OPEN_WEATHER_API_KEY=

LANGSMITH_API_KEY=
```

---

## Run

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

---

# ☁ Azure Deployment

Infrastructure is provisioned using Terraform.

Resources include:

- Azure Resource Group
- Azure App Service
- Azure Key Vault
- Managed Identity
- RBAC Role Assignments

Deploy Infrastructure

```bash
terraform init

terraform plan

terraform apply
```

---

# 🔐 Configuration Strategy

## Azure App Service (Non-sensitive)

```text
APP_ENV=production

LLM_MODEL=llama-3.1-8b-instant

TEMPERATURE=0.4

KEYVAULT_URL=https://<keyvault>.vault.azure.net/
```

---

## Azure Key Vault (Secrets)

```text
groq-api-key

open-weather-api-key

langsmith-api-key

google-api-key
```

---

# 🔁 CI/CD

GitHub Actions automatically:

- Checkout source code
- Install dependencies
- Ruff linting
- Black formatting
- Run tests
- Authenticate with Azure (OIDC)
- Deploy to Azure App Service

---

# ⚡ Performance Strategy

- Deterministic routing
- Minimized LLM calls
- Fast tool execution
- RAG microservice isolation
- Configurable recursion limits

---

# 🛡 Security

- Azure Key Vault
- Managed Identity
- RBAC
- No secrets committed to Git
- Infrastructure as Code

---

# 📌 Useful Commands

Run application

```bash
uvicorn app.main:app --reload
```

Export dependencies

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

Terraform

```bash
terraform init

terraform plan

terraform apply

terraform destroy
```

Azure Login

```bash
az login
```

Deploy

```bash
az webapp deploy \
  --resource-group <resource-group> \
  --name <app-service-name> \
  --src-path app.zip
```

---

# 🚀 Roadmap

- Azure App Configuration
- Azure Monitor
- Application Insights
- Docker
- Azure Container Apps
- Kubernetes
- Azure OpenAI
- Redis Cache
- Semantic Caching

---

# 📄 License

MIT License