pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
              sh "sudo apt update"
            }
        }
        stage('Test') {
            steps {
              sh "mkdir new" 
            }
        }
        stage('Deploy') {
            steps {
              sh "cd new"
              sh "touch example.txt"
              sh "ls"
            }
        }
    }
}
