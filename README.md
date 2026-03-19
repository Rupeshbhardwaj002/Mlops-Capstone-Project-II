# 🚀 MLOps Capstone Project II

[![MLOps](https://img.shields.io/badge/MLOps-End--to--End-blue)](#)
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange)](#)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)](#)
[![Docker](https://img.shields.io/badge/Docker-Containerization-blue)](#)

An industry-standard, end-to-end Machine Learning Operations (MLOps) project demonstrating a complete pipeline from data versioning to model deployment and observability.

## 🛠️ Tech Stack & Architecture

This project integrates a robust stack of modern MLOps tools:

*   **Code Versioning & CI/CD:** Git & GitHub Actions
*   **Data Versioning:** DVC (Data Version Control)
*   **Experiment Tracking & Model Registry:** MLflow
*   **Containerization:** Docker
*   **Cloud Infrastructure (AWS):** S3, IAM, ECR, EKS, CloudFormation, EC2
*   **Distributed Computing & Orchestration:** Kubernetes
*   **Monitoring & Observability:** Prometheus & Grafana

## 🏗️ Pipeline Architecture

1.  **Data Pipeline:** Raw data is versioned using **DVC** and stored remotely in **AWS S3**.
2.  **Model Training:** Models are trained and experiments are tracked using **MLflow**, which also serves as the model registry.
3.  **CI/CD:** **GitHub Actions** automates the testing, building, and pushing of Docker images to **AWS ECR**.
4.  **Deployment:** The containerized application is deployed to a **Kubernetes** cluster hosted on **AWS EKS** (provisioned via CloudFormation/EC2).
5.  **Monitoring:** **Prometheus** scrapes metrics from the deployed model, and **Grafana** provides real-time observability dashboards.

## 🚀 Getting Started

### Prerequisites
*   Python 3.8+
*   Docker & Docker Compose
*   AWS CLI configured with appropriate IAM permissions
*   kubectl & eksctl
*   DVC & MLflow

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Rupeshbhardwaj002/Mlops-Capstone-Project-II.git
    cd Mlops-Capstone-Project-II
    ```

2.  **Set up the virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Pull data using DVC:**
    ```bash
    dvc pull
    ```

4.  **Run MLflow UI locally (optional):**
    ```bash
    mlflow ui
    ```

## ☁️ Cloud Deployment (AWS & Kubernetes)

1.  **Provision Infrastructure:** Use CloudFormation to spin up the necessary EC2 instances and networking components.
2.  **Build & Push Docker Image:** Trigger the GitHub Actions pipeline to build the image and push it to AWS ECR.
3.  **Deploy to EKS:**
    ```bash
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

## 📊 Monitoring & Observability

The deployed application is monitored using Prometheus and Grafana.
*   **Prometheus** scrapes system and model-specific metrics.
*   **Grafana** visualizes these metrics on a custom dashboard for real-time observability.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Rupeshbhardwaj002/Mlops-Capstone-Project-II/issues).

## 📝 License

This project is licensed under the MIT License.

---
*Created by [Rupesh Bhardwaj](https://github.com/Rupeshbhardwaj002)*
