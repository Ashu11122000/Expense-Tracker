# Expense Tracker Application 

A scalable Expense Tracker backend built using Python, evolving from basic concepts to a production-ready architecture using FastAPI, Pydantic, CSV-based storage, and Docker.

This project demonstrates how a simple CLI-based application can be transformed into a modern backend system while still using CSV instead of a traditional database.

---

## Overview

This application allows users to manage expenses through APIs with proper validation, structured architecture, and containerized deployment.

Key capabilities include:

* Expense creation and tracking
* Categorization of expenses
* Budget monitoring
* CSV-based persistent storage
* RESTful API support using FastAPI
* Production-ready architecture design

---

## Features

### Core Features

1. Add new expense records
2. Categorize expenses (Food, Home, Work, Fun, Misc)
3. Store data in a CSV file 
4. View all expenses
5. Calculate total spending
6. Track remaining budget
7. Daily budget calculation

### Backend & Advanced Features

1. FastAPI-based REST APIs
2. Pydantic for request/response validation
3. Layered architecture (API → Service → Repository)
4. Environment configuration using `.env`
5. CSV used as a data persistence layer
6. CORS support for frontend integration
7. Unit testing using Pytest
8. Docker containerization
9. Dependency management using UV
10. Virtual environment setup

---

## Tech Stack

### Language

* Python 3.11+

### Backend Framework

* FastAPI
* Uvicorn

### Data Handling

* CSV (File-based storage)

### Validation

* Pydantic

### Configuration

* python-dotenv

### Architecture

* Service Layer Pattern
* Repository Pattern

### Testing

* Pytest

### DevOps

* Docker
* Docker Compose

---

## Project Structure

```
expense-tracker-app/
│
├── app/
│   ├── main.py                  # FastAPI entry point
│
│   ├── core/
│   │   └── config.py            # Environment configuration
│
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── expenses.py  # API routes
│
│   ├── schemas/
│   │   └── expense.py           # Pydantic models
│
│   ├── services/
│   │   └── expense_service.py   # Business logic
│
│   ├── repositories/
│   │   └── expense_repo.py      # CSV operations
│
│   └── utils/
│       └── csv_handler.py
│
├── data/
│   └── expenses.csv             # Data storage
│
├── tests/
│   └── test_expenses.py         # Unit tests
│
├── images/                      # Screenshots
│
├── .env                         # Environment variables
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt / uv.lock
├── run.py
└── README.md
```

---

## Architecture Flow

```
Client Request
     ↓
FastAPI Route Layer
     ↓
Service Layer (Business Logic)
     ↓
Repository Layer
     ↓
CSV File Storage
```

Pydantic is used at the API layer to validate incoming and outgoing data.

---

## Setup Instructions

### 1. Install Python

Download Python:
`https://www.python.org/downloads/`

Ensure "Add Python to PATH" is enabled.

---

### 2. Clone Repository

```bash
git clone `https://github.com/Ashu11122000/Expense-Tracker-App.git`
cd Expense-Tracker-App
```

---

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies (Using UV)

```bash
pip install uv
uv pip install fastapi uvicorn pydantic python-dotenv sqlalchemy pytest
uv pip install -r requirements.txt
```

---

### 5. Setup Environment Variables

Create `.env` file:

```bash
APP_NAME=Expense Tracker
DEBUG=True
CSV_FILE_PATH=data/expenses.csv
```

---

### 6. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Access API:

```browser
http://127.0.0.1:8000/docs
```

---

## Running Tests

```bash
pytest
```

---

## Docker Setup

### Build Image

```bash
docker build -t expense-tracker .
```

### Run Container

```bash
docker run -p 8000:8000 expense-tracker
```

### Using Docker Compose

```bash
docker-compose up --build
```

---

## Concepts Covered

### Basic Python

* Variables
* Functions
* Lists & Dictionaries
* File Handling (CSV)
* Loops and Conditions

### Advanced Concepts

* API Development (FastAPI)
* Data Validation (Pydantic)
* Clean Architecture Design
* Dependency Injection
* Environment Management
* Containerization (Docker)
* Unit Testing

---

## Future Improvements

1. Replace CSV with PostgreSQL
2. Add authentication (JWT)
3. Implement GraphQL support
4. Add gRPC services
5. Build frontend (React/Next.js)
6. Add caching (Redis)
7. Role-based access control
8. CI/CD pipeline integration
9. Kubernetes deployment

---
