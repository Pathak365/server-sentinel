# Server Sentinel

A local-first server monitoring application built with Python, FastAPI, Docker, Terraform, and GitHub Actions.

Server Sentinel collects system metrics, evaluates health against configurable thresholds, caches recent metrics, and stores health-check history in a JSON file.

## Features

- CPU, memory, and disk usage collection using `psutil`
- Health evaluation with configurable thresholds
- REST API built with FastAPI
- TTL-based in-memory caching
- Persistent health-check history using JSON
- Automated tests with pytest
- Docker containerization
- Infrastructure management using Terraform
- Continuous integration using GitHub Actions

## Technology Stack

- **Language:** Python
- **API:** FastAPI and Uvicorn
- **Monitoring:** psutil
- **Testing:** pytest and FastAPI TestClient
- **Containerization:** Docker
- **Infrastructure as Code:** Terraform with the Docker provider
- **CI:** GitHub Actions

## Project Structure

```text
server-sentinel/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   │   ├── system_collector.py
│   │   ├── health_checker.py
│   │   └── history_manager.py
│   ├── utils/
│   │   ├── cache.py
│   │   └── decorators.py
│   └── main.py
├── tests/
├── data/
├── infra/
│   ├── versions.tf
│   ├── main.tf
│   ├── outputs.tf
│   └── .terraform.lock.hcl
├── .github/workflows/
│   └── tests.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Prerequisites

- Python and pip
- Git
- Docker Desktop
- Terraform

## Run Locally

Create and activate a virtual environment on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Start the API:

```powershell
python -m uvicorn app.main:app --reload
```

Open the API documentation at `http://localhost:8000/docs`.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Application status |
| GET | `/api/v1/system` | Current system metrics |
| GET | `/api/v1/health` | Evaluate health and record history |
| GET | `/health` | Health-check alias |
| GET | `/api/v1/history` | Retrieve recorded history |
| GET | `/api/v1/history/{record_id}` | Retrieve one history record |

## Run Tests

```powershell
python -m pytest -v
```

The current test suite contains 14 tests covering API endpoints, caching, health evaluation, and history management.

## Run with Docker

Build the image from the project root:

```powershell
docker build -t server-sentinel:0.1.0 .
```

Run the container with persistent history:

```powershell
docker run --name server-sentinel -p 8000:8000 -v "${PWD}/data:/app/data" server-sentinel:0.1.0
```

Open `http://localhost:8000/docs` to access the API.

## Manage with Terraform

Initialize Terraform:

```powershell
terraform -chdir=infra init
```

Validate the configuration and preview changes:

```powershell
terraform -chdir=infra validate
terraform -chdir=infra plan
```

Apply the configuration:

```powershell
terraform -chdir=infra apply
```

Terraform manages the Docker container and exposes outputs for its name, ID, and local application URL.

## Continuous Integration

The GitHub Actions workflow runs when code is pushed to `main` or a pull request targets `main`. It checks out the repository, sets up Python, installs dependencies, and runs the pytest suite.

## Data and Local Files

Health history is stored in `data/history.json`. The local history file and Terraform state are excluded from Git because they are generated environment-specific data.

## Current Scope and Limitations

- Metrics reflect the environment visible to the Python process. Inside Docker, they may represent the container rather than the full Windows host.
- History is stored in a local JSON file rather than a production database.
- The cache is in-memory and local to the running application process.
- The project currently targets local Docker infrastructure; it does not provision cloud resources.

## Project Status

The application, test suite, Docker image, GitHub Actions workflow, and Terraform-managed container have been tested in the local development environment.