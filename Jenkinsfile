pipeline {
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
