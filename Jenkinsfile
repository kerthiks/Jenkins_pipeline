pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up the environment...'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh './venv/bin/python -m unittest discover -s tests || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh './venv/bin/python app.py &'
            }
        }

        stage('Merge to Main') {
            when {
                branch 'devops'
            }
            steps {
                echo 'Merging devops into main branch...'
                sh '''
                git config user.name "Jenkins"
                git config user.email "jenkins@example.com"

                CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

                git fetch origin
                git checkout main
                git pull origin main

                git merge --no-ff "$CURRENT_BRANCH" -m "Merged by Jenkins from $CURRENT_BRANCH"
                git push origin main
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'pkill -f app.py || true'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
