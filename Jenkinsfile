pipeline {
    agent { label 'docker-agent-1' }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat', // Reference the credential ID
                    url: 'https://github.com/PierceMcGowan/rosary_prayer_counter'
            }
        }        
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
                sh '. .venv/bin/activate && pip install -r dev_requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                sh '. .venv/bin/activate && pytest --junitxml=test-results.xml'
            }
        }

        stage('Run Black') {
            steps {
                sh '. .venv/bin/activate && black python_lib/divine_mercy python_lib/rosary python_lib/counter_gui scripts --check .'
            }
        }

        stage('Run Pylint') {
            steps {
                sh '. .venv/bin/activate && pylint --exit-zero python_lib/divine_mercy python_lib/rosary python_lib/counter_gui scripts'
            }
        }

        stage('Run MyPy') {
            steps {
                sh '. .venv/bin/activate && mypy python_lib/divine_mercy python_lib/rosary python_lib/counter_gui scripts'
            }
        }

        stage('Install Local Libraries') {
            steps {
                sh '. .venv/bin/activate && pip install --editable ./python_lib/counter_gui'
                sh '. .venv/bin/activate && pip install --editable ./python_lib/divine_mercy'
                sh '. .venv/bin/activate && pip install --editable ./python_lib/rosary'
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