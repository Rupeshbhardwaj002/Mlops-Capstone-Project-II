# Mlops-Capstone-Project-II
This is an end to end mlops project which covers git-github actions(Code versioning), DVC(data versioning), MLFlow(Performence data visualization model registery), Docker(Contarization), AWS(S3, IAM, ECR, EKS, Cloud Formation, EC2), Kubernetes(Distributed Computing), Prometheus- Grafana(Monitoring and observabilty)


# 🚀 Enterprise MLOps Capstone Project II

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![AWS](https://img.shields.io/badge/AWS-Deployed-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

An end-to-end, highly scalable Machine Learning Operations (MLOps) architecture designed for production environments. This project focuses on establishing a robust bridge between data science and software engineering by automating the lifecycle of machine learning models—from data ingestion and versioning to model registry, containerized deployment, and real-time observability.

---

## 📑 Table of Contents
1. [System Architecture](#-system-architecture)
2. [Technology Stack](#-technology-stack)
3. [Project Directory Structure](#-project-directory-structure)
4. [CI/CD Workflow](#-cicd-workflow)
5. [Local Development Setup](#-local-development-setup)
6. [Cloud Deployment (AWS EKS)](#-cloud-deployment-aws-eks)
7. [Observability & Monitoring](#-observability--monitoring)
8. [License & Author](#-license--author)

---

## 🏗️ System Architecture

This project is built on a modular pipeline architecture, ensuring that each step of the machine learning lifecycle is isolated, reproducible, and scalable.

### 1. The ML Pipeline (`src/components/`)
* **Data Ingestion:** Reads raw data from remote sources, splitting it into training and testing sets.
* **Data Validation:** Ensures data schema integrity and checks for drift before processing.
* **Data Transformation:** Applies feature engineering, scaling, and handling of missing values. The preprocessor object is saved as a `.pkl` file for inference.
* **Model Trainer:** Trains various algorithms, performs hyperparameter tuning, and selects the best-performing model based on predefined metrics.
* **Model Evaluation:** Evaluates the chosen model on holdout data and logs all metrics, parameters, and artifacts to the remote MLflow tracking server.

### 2. The Infrastructure Pipeline
* **Data Storage:** Raw datasets and DVC metadata are synced to an **AWS S3** bucket.
* **Tracking & Registry:** **MLflow** handles the logging of experiments. *Note: This is configured to work with a remote tracking server like DagsHub for distributed team access.*
* **Deployment Orchestration:** The prediction API (built with Flask/FastAPI) is containerized via **Docker**, pushed to **Amazon ECR**, and managed by **Amazon EKS** (Kubernetes) to handle variable inference loads.

---

## 🛠️ Technology Stack

| Category | Tools Used | Purpose |
| :--- | :--- | :--- |
| **Code & Versioning** | Git, GitHub | Source code management |
| **CI/CD Automation** | GitHub Actions | Automated testing, Docker builds, and EKS deployments |
| **Data Versioning** | DVC, AWS S3 | Tracking changes in large datasets and model artifacts |
| **Experiment Tracking** | MLflow | Logging hyperparameters, metrics, and model registry |
| **Containerization** | Docker | Packaging the application and its dependencies |
| **Cloud Provider** | AWS (IAM, ECR, EKS, EC2) | Infrastructure hosting, container registry, and compute |
| **Orchestration** | Kubernetes | Managing and scaling containerized deployment |
| **Observability** | Prometheus, Grafana | Scraping system metrics and visualizing real-time dashboards |

---

## 📂 Project Directory Structure

```text
├── .github/workflows/       # GitHub Actions CI/CD YAML files (main.yml)
├── config/                  # Configuration files for the pipeline (config.yaml)
├── data/                    # Local data folder (Ignored by Git, tracked by DVC)
├── kubernetes/              # K8s manifests
│   ├── deployment.yaml      # Pod configurations and replica counts
│   ├── service.yaml         # LoadBalancer/NodePort configurations
│   └── ingress.yaml         # Routing rules
├── monitoring/              # Prometheus config and Grafana dashboard templates
├── src/                     # Core application source code
│   ├── components/          # Pipeline stages (ingestion, transformation, trainer)
│   ├── pipeline/            # Train_pipeline.py and Predict_pipeline.py
│   ├── logger.py            # Custom logging framework
│   ├── exception.py         # Custom exception handling
│   └── utils.py             # Helper functions (saving/loading objects)
├── app.py                   # Main web API (Flask/FastAPI) for inference
├── Dockerfile               # Instructions to build the Docker image
├── dvc.yaml                 # DVC pipeline stages and dependencies
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup file
└── README.md
