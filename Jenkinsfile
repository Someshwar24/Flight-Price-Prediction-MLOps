pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Flight Price Prediction project is ready.'
            }
        }

        stage('Check Python') {
            steps {
                bat 'py --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Test API Code') {
            steps {
                bat 'py -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flight-price-api:latest .'
            }
        }
    }
}
