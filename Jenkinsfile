pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sanketcloud25/python-ci.git'
            }
        } // <- Added this closing brace
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Compile') {
            steps {
                sh 'python3 -m py_compile src/*.py'
                // Optionally, compile other Python files or directories if needed
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
        stage('Package') {
            steps {
                sh 'python3 setup.py sdist bdist_wheel'
                // If you don’t have a setup.py file, you can create one or use another packaging command
            }
        }
    }
}
