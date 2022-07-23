pipeline{
    agent any
    stages{
        stage("Install"){
            steps{
                echo 'Installing packages'
                sh 'sudo apt update && sudo apt install python3-pip'
            }
        }
        stage("Build"){
            steps{
                sh 'python3 test.py'
            }
        }
    }
}