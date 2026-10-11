pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/Someshwar24/Flight-Price-Prediction-MLOps.git'
            }
        }

        stage('API Syntax Check') {
            steps {
                bat '"C:\\Users\\somes\\anaconda3\\envs\\flight-mlops\\python.exe" -m py_compile app.py'
    }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\somes\\anaconda3\\envs\\flight-mlops\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\somes\\anaconda3\\envs\\flight-mlops\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flight-price-api:latest .'
            }
        }
    }
}
