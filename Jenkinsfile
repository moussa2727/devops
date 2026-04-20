pipeline {
    agent any

    stages {
        stage('Installation des dépendances') {
            steps {
                // 1. Création d'un environnement virtuel propre pour ce build
                sh 'python3 -m venv venv'
                
                // 2. Installation des packages depuis ton requirements.txt
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Exécution') {
            steps {
                echo "Dépendances installées avec succès."
                // 3. Exemple : Lancer ton script principal ici
                // sh './venv/bin/python ton_script.py'
            }
        }
    }
}
