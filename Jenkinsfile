pipeline {
    agent any

    stages {
        stage('Installation dépendances') {
            steps {
                sh '''
                rm -rf venv
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Vérification code') {
            steps {
                sh './venv/bin/python -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Construction de la nouvelle image Docker..."
                sh 'docker build -t devops-app:latest .'
            }
        }

        stage('Déploiement Terraform') {
            steps {
                echo "Mise à jour de l'infrastructure sur le port 8081..."
                sh '''
                if [ ! -d ".terraform" ]; then
                    terraform init
                fi
                terraform apply -auto-approve
                '''
            }
        }
    }
}

