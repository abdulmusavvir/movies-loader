def imageName = 'abdulmusavvirrohe/movies-loader'

node {
    stage('Checkout') {
        checkout scm
    }
    stage('Unit Test') {
        script {
            def reportDir = "reports"
            
            // Ensure the reports directory is clean and has correct permissions
            sh "rm -rf ${reportDir}/*"
            sh "mkdir -p ${reportDir} && chown -R \$(id -u):\$(id -g) ${reportDir}"

            // Get the UID and GID of the Jenkins user
            def uid = sh(script: "id -u", returnStdout: true).trim()
            def gid = sh(script: "id -g", returnStdout: true).trim()

            // Build the Docker image for running tests
            sh "docker build -t ${imageName}-test -f Dockerfile.test ."

            // Run the Docker container as the Jenkins user and mount the reports directory
            sh """
            docker run --rm -u ${uid}:${gid} -v ${PWD}/${reportDir}:/app/${reportDir} ${imageName}-test
            """

            // Check the ownership and presence of the test report files
            sh "ls -la ${reportDir}"

            // Use junit to collect the test reports
            junit "${reportDir}/*.xml"
        }
    }
}
