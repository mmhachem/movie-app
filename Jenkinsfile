pipeline {
  agent any
  triggers {
    pollSCM('H/2 * * * *')
  }
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/mmhachem/movie-app.git'
      }
    }
    
    stage('Start Minikube') {
      steps {
        bat '''
            REM Check if Minikube is running
            minikube status || minikube start --driver=docker
        '''
      }
    }
    
    stage('Build in Minikube Docker') {
      steps {
        bat '''
            REM Set Minikube Docker environment
            @FOR /f "tokens=*" %%i IN ('minikube docker-env --shell cmd ^| findstr "^SET"') DO @%%i
            
            REM Build the Docker image
            docker build -t mydjangoapp:latest .
        '''
      }
    }
    
    stage('Deploy to Minikube') {
      steps {
        bat '''
            REM Apply the updated deployment manifest
            kubectl apply -f deployment.yaml
            
            REM Ensure the rollout completes
            kubectl rollout status deployment/django-deployment
        '''
      }
    }
  }
}
