def imageName = 'abdulmusavvirrohe/movies-loader'

node {
    stage('Checkout') {
        checkout scm
    }
    stage('Unit Tests'){
        def imageTest= docker.build("${imageName}-test", "-f Dockerfile.test .")
        sh "docker run --rm -v $PWD/reports:/app/reports ${imageName}-test"
        junit "$PWD/reports/*.xml"
    }
}
