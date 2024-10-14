def imageName = 'abdulmusavvirrohe/movies-loader'

node {
    stage('Checkout') {
        checkout scm
    }
    stage('Unit Test') {
        script {
            def reportDir = "${WORKSPACE}/reports"
            
            // Clean the reports directory, removing old reports
            sh "rm -rf ${reportDir}/*"  // Clean any old reports
            
            // Get the UID and GID of the Jenkins user to avoid root ownership issues
            def uid = sh(script: "id -u", returnStdout: true).trim()
            def gid = sh(script: "id -g", returnStdout: true).trim()

            // Build the Docker image for running tests
            sh "docker build -t ${imageName}-test -f Dockerfile.test ."
            
            // Run the Docker container as the Jenkins user and mount the reports directory
            sh """
            docker run --rm -u ${uid}:${gid} -v ${reportDir}:/app/reports ${imageName}-test
            """

            // Check the ownership and presence of the test report files
            sh "ls -la ${reportDir}"

            // Use junit to collect the test reports
            junit "${reportDir}/*.xml"
        }
    }
}
