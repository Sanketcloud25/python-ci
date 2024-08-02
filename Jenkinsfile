pipeline {
    agent any
    tools {
        python 'Python3'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/my-python-app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'flake8 src/'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
