pipeline {
    agent {
        docker {
            perspective {
                label 'docker-agent-1'
            }
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/PierceMcGowan/rosary_prayer_counter'
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

        stage('Cross-Compile for Windows') {
            steps {
                sh '. venv/bin/activate && wine pyinstaller --onefile your_main_script.py -n your_app_windows.exe'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/windows/start_rosary.exe,dist/linux/start_rosary', allowEmptyArchive: true
            }
        }
    }
}