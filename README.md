# 🛒 DemoBlaze Modern Playwright Framework

[![Python](https://img.shields.io)](https://www.python.org)
[![Playwright](https://img.shields.io)](https://playwright.dev)
[![Docker](https://img.shields.io)](https://www.docker.com)
[![CI/CD](https://img.shields.io)](https://github.com)

An end-to-end automation framework designed for the **DemoBlaze** platform. This project demonstrates a professional-grade testing architecture including UI/API testing, database validation, and full containerization.

## 🏗️ Architecture & Workflow
Below is the high-level system design of the testing environment:

![Architecture Diagram](./architecture.png) 
*Note: Ensure your PNG file is named 'architecture.png' and is in the root of your repo.*

---

## 🛠️ Tech Stack
*   **Language:** Python
*   **Testing Tool:** Playwright (Pytest-Playwright)
*   **Database:** PostgreSQL (Containerized)
*   **API Layer:** FastAPI Service
*   **Environment:** Docker & Docker Compose
*   **CI/CD:** GitHub Actions

---

## 🚀 How to Run Locally

### Prerequisites
*   [Docker Desktop](https://www.docker.comproducts/docker-desktop/) installed and running.
*   [Git](https://git-scm.com) installed.

### Setup
1. **Clone the repository:**
   ```bash
   git clone [INSERT_YOUR_REPO_URL_HERE]
   cd demoblaze-automation
