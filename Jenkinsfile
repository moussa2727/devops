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
                echo "Mise à jour de l'infrastructure..."
                sh '''
                if [ ! -d ".terraform" ]; then
                    terraform init
                fi
                terraform apply -auto-approve
                '''
            }
        }
    }

    // C'est ici que la magie opère pour arrêter la boucle
    post {
        always {
            echo "Nettoyage du workspace pour éviter les builds fantômes..."
            // Supprime les fichiers qui trompent Git (tfstate, venv, etc.)
            sh 'rm -rf venv .terraform *.tfstate *.tfstate.backup'
        }
    }
}
