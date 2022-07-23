pipeline{
    agent any
    stages{
        stage("Cloning"){
            steps{
                echo 'Cloning the Repo'
                checkout scm
            }
        }
        stage("Install"){
            steps{
                echo 'Installing packages'
                sh 'pip install -r requirements.txt'
            }
        }
        stage("Build"){
            steps{
                sh 'python3 test.py'
            }
        }
    }
}