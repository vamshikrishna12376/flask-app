pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'myusername/flask-app:latest'
        DOCKER_CREDENTIALS = 'docker-hub-credentials'  // Jenkins credentials ID
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/user/repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: DOCKER_CREDENTIALS, url: '']) {
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent(['server-ssh-credentials']) {
                    sh """
                    ssh user@your-server-ip <<EOF
                    docker pull $DOCKER_IMAGE
                    docker stop flask-container || true
                    docker rm flask-container || true
                    docker run -d --name flask-container -p 5000:5000 $DOCKER_IMAGE
                    EOF
                    """
                }
            }
        }
    }
}
