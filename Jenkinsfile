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
            // Match if this is from devops branch or PR from devops
            return env.BRANCH_NAME == 'devops' || env.CHANGE_BRANCH == 'devops'
        }
    }
    steps {
        echo '🔀 Preparing to merge devops into main...'
        sh '''
        git config user.name "Jenkins"
        git config user.email "jenkins@example.com"

        echo "🔍 Fetching all remote branches..."
        git fetch origin +refs/heads/*:refs/remotes/origin/*

        echo "📦 Checking out main branch..."
        git checkout -B main origin/main

        echo "🔀 Merging devops into main..."
        git merge --no-ff origin/devops -m "Auto-merged by Jenkins from devops"

        echo "🚀 Pushing merged changes to main..."
        git push origin main
        '''
    }
}
    }
}           