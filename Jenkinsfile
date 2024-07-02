pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("your-dockerhub-username/your-app:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image("your-dockerhub-username/your-app:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
        
        stage('Update Kubernetes Manifests') {
            steps {
                sh """
                sed -i 's|image: .*|image: your-dockerhub-username/your-app:${env.BUILD_NUMBER}|' k8s/deployment.yaml
                git config user.email "jenkins@example.com"
                git config user.name "Jenkins"
                git add k8s/deployment.yaml
                git commit -m "Update image to ${env.BUILD_NUMBER}"
                git push origin main
                """
            }
        }
    }
}
