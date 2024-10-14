def imageName = 'abdulmusavvirrohe/movies-loader'

node {
    stage('Checkout') {
        checkout scm
    }
    stage('Unit Tests'){
        sh "echo ${PWD}"
        sh "echo ${WORKDIR}"
        sh "docker build -t ${imageName}-test -f Dockerfile.test ."
        sh "docker run --rm -v $PWD/reports:/app/reports ${imageName}-test"
    }
}
