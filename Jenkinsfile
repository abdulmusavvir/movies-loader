def imageName = 'abdulmusavvirrohe/movies-loader'
node{
    stage('checkout'){
        checkout scm
    }
    stage('unit test'){
        sh "docker build -t ${imageName}-test -f Dockerfile.test ."
        sh "docker run --rm ${imageName}-test python test_main.py"
    }
}
