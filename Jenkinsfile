def imageName = 'abdulmusavvirrohe/movies-loader'
node{
    stage('checkout'){
        checkout scm
    }
    stage('unit test'){
        sh "echo $PWD"
        sh "docker build -t ${imageName}-test -f Dockerfile.test ."
        sh "docker run --rm -v ${PWD}/reports:/app/reports ${imageName}-test"
        junit "$PWD/reports/*.xml"
    }
}
