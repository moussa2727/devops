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
                # Initialisation de Terraform si nécessaire
                if [ ! -d ".terraform" ]; then
                    terraform init
                fi
                
                # Appliquer la configuration (auto-approve valide sans demander)
                terraform apply -auto-approve
                '''
            }
        }
    }
}pipeline {
    agent any

    stages {
        stage('Installation des dépendances') {
            steps {
                sh '''
                # Nettoyage de l'ancien environnement
                rm -rf venv
                
                # Création du venv
                python3 -m venv venv
                
                # Installation des dépendances
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Vérification du code') {
            steps {
                echo "Vérification syntaxique de l'application..."
                // On vérifie que app.py est syntaxiquement correct
                sh './venv/bin/python -m py_compile app.py'
            }
        }
    }
}
