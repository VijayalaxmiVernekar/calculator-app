pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VijayalaxmiVernekar/calculator-app.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat """
                ${env.PYTHON} -m venv venv
                venv\\Scripts\\activate
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                venv\\Scripts\\activate && python -m pip install --upgrade pip
                venv\\Scripts\\activate && pip install -r requirements.txt
                """
            }
        }

        stage('Run Script') {
            steps {
                bat """
                venv\\Scripts\\activate && python main.py
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                venv\\Scripts\\activate && pytest --junitxml=report.xml
                """
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}
