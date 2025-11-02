pipeline {
  agent any
  
  environment {
    MINIKUBE_HOME = 'C:\\SPB_Data'
    DOCKER_TLS_VERIFY = '1'
    DOCKER_HOST = 'tcp://127.0.0.1:54578'
    DOCKER_CERT_PATH = 'C:\\SPB_Data\\.minikube\\certs'
    MINIKUBE_ACTIVE_DOCKERD = 'minikube'
    KUBECONFIG = 'C:\\SPB_Data\\.kube\\config'
  }
  
  triggers {
    pollSCM('H/2 * * * *')
  }
  
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/mmhachem/movie-app.git'
      }
    }
    
    stage('Build in Minikube Docker') {
      steps {
        bat '''
            REM Build the Docker image using YOUR running Minikube
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
