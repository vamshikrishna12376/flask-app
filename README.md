# Flask CI/CD Pipeline

## Introduction
This README outlines the setup and configuration of a CI/CD pipeline for a Flask web application using GitHub Actions, Jenkins, and Docker. The pipeline automates testing, building, and deploying the application to a remote server.

## Project Overview
This project includes:
- A simple Flask web application
- CI/CD pipeline using GitHub Actions & Jenkins
- Automated unit testing with `unittest`
- Dockerized deployment
- Deployment automation to a remote server

## Project Structure
```
flask-app/
│── .github/workflows/
│   └── main.yml          # GitHub Actions workflow
│── tests/  
│   ├── test_app.py       # Unit tests for the Flask app
│── app/  
│   ├── __init__.py       # Flask app initialization
│   ├── app.py            # Main Flask app
│── Dockerfile            # Docker build instructions  
│── requirements.txt      # Python dependencies  
│── Jenkinsfile           # Jenkins CI/CD pipeline  
│── .gitignore            # Ignore unnecessary files  
│── README.md             # Project documentation  
```

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/your-username/flask-cicd.git
cd flask-cicd
```

### Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Run the Flask App Locally
```sh
python app.py
```
Access the application at **http://localhost:5000**

## Running Tests
Execute unit tests with:
```sh
python -m unittest discover -s tests
```

## Docker Usage

### Build and Run Locally
```sh
docker build -t myusername/flask-app .
docker run -d -p 5000:5000 myusername/flask-app
```
Access the application at **http://localhost:5000**

### Push to Docker Hub
```sh
docker login
docker tag myusername/flask-app myusername/flask-app:latest
docker push myusername/flask-app:latest
```

## CI/CD Pipeline

### GitHub Actions Workflow
Located in `.github/workflows/main.yml`, this workflow:
1. Runs unit tests (`unittest`)
2. Builds and pushes Docker images to Docker Hub
3. Deploys the application to a remote server

### Jenkins Pipeline
Located in `Jenkinsfile`, this pipeline:
1. Pulls the latest code from GitHub
2. Runs unit tests
3. Builds and pushes the Docker image
4. Deploys the application to a remote server

## Deployment to Remote Server

### Ensure Docker is Installed
```sh
sudo apt update && sudo apt install docker.io -y
```

### Deploy via SSH
```sh
ssh user@server-ip <<EOF
docker pull myusername/flask-app:latest
docker stop flask-container || true
docker rm flask-container || true
docker run -d --name flask-container -p 5000:5000 myusername/flask-app:latest
EOF
```





