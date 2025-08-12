pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/kerthiks/jenkins_1.git'
        GIT_CREDENTIALS = credentials('git-credentials-id') // Injects GIT_CREDENTIALS_USR and GIT_CREDENTIALS_PSW
        TARGET_BRANCH = 'main'
        GIT_USER_NAME = 'jenkins'
        GIT_USER_EMAIL = 'jenkins@example.com'
    }

    stages {
        stage('Build') {
            steps {
                echo '✅ Building project...'
                // sh 'your build command'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                // sh 'your test command'
            }
        }

        stage('Merge PR to Main') {
            when {
                expression { return env.BRANCH_NAME != env.TARGET_BRANCH }
            }
            steps {
                script {
                    echo "🔁 Merging branch '${env.BRANCH_NAME}' into '${env.TARGET_BRANCH}'..."

                    sh """
                        git config --global user.name "${GIT_USER_NAME}"
                        git config --global user.email "${GIT_USER_EMAIL}"

                        git remote set-url origin https://${GIT_CREDENTIALS_USR}:${GIT_CREDENTIALS_PSW}@github.com/kerthiks/jenkins_1.git

                        git fetch origin
                        git checkout ${TARGET_BRANCH}
                        git merge origin/${BRANCH_NAME} --no-edit
                        git push origin ${TARGET_BRANCH}
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Merge completed successfully.'
        }
        failure {
            echo '❌ Merge failed.'
        }
    }
}
git checkout main
git add Jenkinsfile
git commit -m "Add working Jenkinsfile to main"
git push origin main
