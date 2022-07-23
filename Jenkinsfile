pipeline{
    agent any
    stages{
        stage("Install"){
            steps{
                echo 'Installing packages'
            }
        }
        stage("Build"){
            steps{
                'python3 test.py'
            }
        }
    }
}