pipeline {
    agent { label 'docker-agent-1' }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat', // Reference the credential ID
                    url: 'https://github.com/your-username/your-repo.git'
            }
        }        
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                sh '. .venv/bin/activate && pytest --junitxml=test-results.xml'
            }
        }

        stage('Run Black') {
            steps {
                sh '. .venv/bin/activate && black --check .'
            }
        }

        stage('Run Pylint') {
            steps {
                sh '. .venv/bin/activate && pylint --exit-zero your_project_directory'
            }
        }
        
        stage('Compile for Linux') {
            steps {
                sh '. .venv/bin/activate && python3 scripts/compile_rosary.py'
            }
        }
        
        stage('Cross-Compile for Windows') {
            steps {
                sh '. .venv/bin/activate && wine python scripts/compile_rosary.py'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/windows/start_rosary.exe,dist/linux/start_rosary', allowEmptyArchive: true
            }
        }
    }
}