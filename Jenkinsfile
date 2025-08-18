pipeline {
    agent any

    environment {
        VENV = './venv'
    }

    stages {
        stage('Setup') {
            steps {
                echo '🔧 Setting up the environment...'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh './venv/bin/python -m unittest discover -s tests || true'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying the application...'
                sh './venv/bin/python app.py &'
            }
        }

        stage('Merge to Main') {
            when {
                expression {
                    // This allows merging if source branch is 'devops'
                    def branch = sh(script: "git rev-parse --abbrev-ref HEAD", returnStdout: true).trim()
                    return branch == 'devops' || env.CHANGE_BRANCH == 'devops'
                }
            }
            steps {
                echo '🔀 Merging devops into main branch...'
                sh '''
                git config user.name "Jenkins"
                git config user.email "jenkins@example.com"

                # Detect current branch (might be devops or PR)
                CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
                echo "Current branch is: $CURRENT_BRANCH"

                git fetch origin
                git checkout main
                git pull origin main

                # Merge devops branch into main
                git merge --no-ff origin/devops -m "Auto-merged by Jenkins from devops"

                # Push the merged changes to main
                git push origin main
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up...'
            sh 'pkill -f app.py || true'
        }
        success {
            echo '✅ Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
