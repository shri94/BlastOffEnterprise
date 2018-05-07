node {
   def installed = fileExists 'bin/activate'

    if (!installed) {
        stage("Install Python Virtual Enviroment") {
            sh 'virtualenv --no-site-packages .'
        }
    }
    stage ("Get Latest Code") {
    checkout scm
    }
    stage ("Install Application Dependencies") {
    sh '''
        sudo python3 -m pip install -r requirements.txt
       '''
    }
    stage ("Run Unit/Integration Tests") {
    def testsError = null
    try {
        sh '''
            python3 ./manage.py test
           '''
    }
    catch(err) {
        testsError = err
        currentBuild.result = 'FAILURE'
    }
}
   
}
