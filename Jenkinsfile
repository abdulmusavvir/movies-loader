def imageName = 'abdulmusavvirrohe/movies-loader'
node{
    stage('checkout'){
        checkout scm
    }
    stage('unit test'){
        def imageTest = docker.build("${imageName}-test", "-f Dockerfile.test .")
         docker.image("${imageName}-test").inside{
            sh 'python test_main.py'
        }
        }
    }
