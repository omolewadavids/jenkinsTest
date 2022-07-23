pipeline{
    agent any
    stages{
        stage("Install"){
            steps{
                echo 'Installing packages'
                sh 'python3 pip install -r requirements.txt'
            }
        }
        stage("Build"){
            steps{
                sh 'python3 test.py'
            }
        }
    }
}