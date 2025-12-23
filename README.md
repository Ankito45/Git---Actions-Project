# GitHub Actions CI/CD Project
A comprehensive collection of GitHub Actions workflows demonstrating end-to-end CI/CD pipelines for Java, Python, Kubernetes, and Docker Swarm deployments.

## 🎯 Overview

This repository contains production-ready GitHub Actions workflows that automate:
- Java application builds with Maven
- Code quality analysis with SonarQube
- Kubernetes deployments
- Docker Swarm deployments
- Python testing with pytest

## 🚀 Workflows

### 1. End-to-End Java CI/CD (`deploy-java-with-maven-sonar-k8s.yml`)

Complete pipeline for Java applications with quality gates and Kubernetes deployment.

**Features:**
- Java 12 setup
- Maven build and test
- SonarCloud code quality analysis
- Automated Kubernetes deployment

### 4. Python Application (`Fibonacci.py`)

Sample Python application with test cases for CI/CD demonstration.

**Features:**
- Fibonacci sequence calculator
- Unit tests with pytest
- Ready for GitHub Actions integration

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/Ankito45/Git---Actions-Project.git
cd Git---Actions-Project
```

### Step 2: Configure Secrets

Navigate to your GitHub repository:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add the following secrets:

| Secret Name | Description | Required For |
|------------|-------------|--------------|
| `KUBECONFIG` | Base64 encoded Kubernetes config | K8s workflows |
| `SONAR_TKN` | SonarCloud authentication token | Java workflow |
| `DOCKER_REGISTRY_PASS` | Docker registry password | Swarm workflow |

#### Generating KUBECONFIG Secret

```bash
# Encode your kubeconfig file
cat ~/.kube/config | base64 -w 0

# Copy the output and add as KUBECONFIG secret
```

### Running Workflows

Workflows automatically trigger on push to `main` branch:

```bash
git add .
git commit -m "Deploy application"
git push -u origin main
```

### Monitoring Workflow Runs

1. Go to the **Actions** tab in your repository
2. Click on the workflow run to see details
3. Expand steps to view logs
4. Check for ✅ (success) or ❌ (failure) status


## 📁 Project Structure

```
Git---Actions-Project/
├── .github/
│   └── workflows/
│       ├── deploy-java-with-maven-sonar-k8s.yml
│       ├── deploy-to-k8s.yml
│       └── deploy-to-swarm.yml
        └── Fibonacci.py
├── kubernetes/
│   └── (your k8s manifests)
└── README.md
```

Give a ⭐️ if this project helped you learn GitHub Actions!
