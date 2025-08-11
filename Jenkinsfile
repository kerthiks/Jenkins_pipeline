pipeline {
    agent any

    environment {
        BRANCH_NAME = "${env.BRANCH_NAME}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
                // Example: sh 'mvn clean install'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Example: sh 'mvn test'
            }
        }

        stage('Merge PR') {
            when {
                expression {
                    return env.CHANGE_ID != null  // Ensures this only runs for Pull Requests
                }
            }
            steps {
                script {
                    echo 'Attempting to merge PR...'

                    def gitUser = 'jenkins'
                    def gitEmail = 'jenkins@example.com'

                    sh """
                    git config --global user.name "${gitUser}"
                    git config --global user.email "${gitEmail}"

                    git remote set-url origin https://${GIT_CREDENTIALS}@github.com/kerthiks/jenkins_1.git
                    git fetch origin
                    git checkout ${env.CHANGE_BRANCH}
                    git merge origin/main --no-edit
                    git push origin ${env.CHANGE_BRANCH}
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build & PR Merge Successful!'
        }
        failure {
            echo '❌ Build or PR Merge Failed.'
        }
    }
}
