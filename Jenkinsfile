pipeline {
  agent any
  triggers {
    // Poll GitHub every 2 minutes
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
        powershell '''
            # Get Minikube Docker environment variables
            $env_output = minikube docker-env --shell powershell | Out-String
            
            # Execute the environment setup
            Invoke-Expression $env_output
            
            # Build the Docker image
            docker build -t mydjangoapp:latest .
        '''
      }
    }
    
    stage('Deploy to Minikube') {
      steps {
        bat '''
        REM === Apply the updated deployment manifest ===
        kubectl apply -f deployment.yaml
        REM === Ensure the rollout completes ===
        kubectl rollout status deployment/django-deployment
        '''
      }
    }
  }
}
