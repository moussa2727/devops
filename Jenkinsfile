pipeline {
    agent any

    stages {
        stage('Installation des dépendances') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Exécution') {
            steps {
                sh '''
                . venv/bin/activate
                echo "Dépendances installées avec succès."
                '''
            }
        }
    }
}
