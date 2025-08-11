pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/kerthiks/jenkins_1.git'
        GIT_CREDENTIALS = credentials('git-credentials-id') // Jenkins credentials ID
        SOURCE_BRANCH = 'devops'
        TARGET_BRANCH = 'main'
        GIT_USER_NAME = 'jenkins'
        GIT_USER_EMAIL = 'jenkins@example.com'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: "*/${env.SOURCE_BRANCH}"]],
                    userRemoteConfigs: [[
                        url: env.GIT_REPO,
                        credentialsId: 'git-credentials-id'
                    ]]
                ])
            }
        }

        stage('Build') {
            steps {
                echo '✅ Building project...'
                // sh 'mvn clean install' or similar
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                // sh 'mvn test' or similar
            }
        }

        stage('Merge to Main') {
            steps {
                script {
                    echo '🔁 Attempting to merge devops → main...'

                    sh """
                        git config --global user.name "${GIT_USER_NAME}"
                        git config --global user.email "${GIT_USER_EMAIL}"

                        git fetch origin
                        git checkout ${TARGET_BRANCH}
                        git merge origin/${SOURCE_BRANCH} --no-edit
                        git push https://${GIT_CREDENTIALS_USR}:${GIT_CREDENTIALS_PSW}@github.com/kerthiks/jenkins_1.git ${TARGET_BRANCH}
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Merge to main successful!'
        }
        failure {
            echo '❌ Merge failed.'
        }
    }
}
