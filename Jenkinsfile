pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sudo apt update
      }
    }
    stage ('Test') {
      steps
        mkdir example
      }
    }
    stage('Deploy') {
      steps {
        cd example
        pwd
      }
    }
  }
}
