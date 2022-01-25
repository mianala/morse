pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }
    environment {
        HOME = "${env.WORKSPACE}"
    }
    stages {
        stage('build') {
            steps {
                sh 'pip install pipenv --user'
                sh '~/.local/bin/pipenv install --dev'
            }
        }
        stage('test') {
            steps {
                sh '~/.local/bin/pipenv run nosetests'
            }
        }
    }
}