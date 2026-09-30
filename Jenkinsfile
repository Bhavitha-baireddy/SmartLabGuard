pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t smartlabguard:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                docker stop smartlabguard-jenkins 2>NUL || exit /b 0
                docker rm smartlabguard-jenkins 2>NUL || exit /b 0
                docker run -d -p 5001:5000 --name smartlabguard-jenkins smartlabguard:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'SmartLabGuard CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}