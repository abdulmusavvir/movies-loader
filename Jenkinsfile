def imageName = 'abdulmusavvirrohe/movies-loader'

node {
    stage('Checkout') {
        checkout scm
    }
    stage('Unit Test') {
        script {
            // Use WORKSPACE for Jenkins workspace path instead of $PWD
            def reportDir = "${WORKSPACE}/reports"
            
            // Ensure the reports directory exists
            sh "mkdir -p ${reportDir}"
            
            // Build the Docker image
            sh "docker build -t ${imageName}-test -f Dockerfile.test ."
            
            // Run the Docker container and mount the reports directory
            sh "docker run --rm -v ${reportDir}:/app/reports ${imageName}-test"
            
            // Ensure the reports were generated
            sh "ls -la ${reportDir}"
            
            // Publish the test results
            junit "${reportDir}/*.xml"
        }
    }
}
