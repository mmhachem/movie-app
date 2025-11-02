pipeline {
  agent any
  stages {
    stage('Debug Docker Environment') {
      steps {
        bat '''
            echo === Current Docker Info ===
            docker info
            
            echo === Minikube Status ===
            minikube status
            
            echo === Minikube Docker Env ===
            minikube docker-env --shell cmd
        '''
      }
    }
  }
}
