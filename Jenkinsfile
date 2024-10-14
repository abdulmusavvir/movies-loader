def imageName = 'abdulmusavvirrohe/movies-loader'

node {
    stage('Checkout') {
        checkout scm
    }
    stage('Unit Test') {
        script {
            def reportDir = "${WORKSPACE}/reports"
            
            // Ensure the reports directory exists
            sh "mkdir -p ${reportDir}"
            
            // Get the UID and GID of the Jenkins user
            def uid = sh(script: "id -u", returnStdout: true).trim()
            def gid = sh(script: "id -g", returnStdout: true).trim()

            // Build the Docker image
            sh "docker build -t ${imageName}-test -f Dockerfile.test ."
            
            // Run the Docker container as the Jenkins user
            sh """
            docker run --rm -u ${uid}:${gid} -v ${reportDir}:/app/reports ${imageName}-test
            """
            
            // Ensure the reports were generated
            sh "ls -la ${reportDir}"
            
            // Publish the test results
            junit "${reportDir}/*.xml"
        }
    }
}
