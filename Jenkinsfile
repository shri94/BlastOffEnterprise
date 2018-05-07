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
        python3 -m pip install -r requirements.txt
       '''
    }
    stage ("Run Unit/Integration Tests") {
    def testsError = null
    try {
        sh '''
            python3 ./manage.py jenkins
           '''
    }
    catch(err) {
        testsError = err
        currentBuild.result = 'FAILURE'
    }
    finally {
        junit 'reports/junit.xml'

        if (testsError) {
            throw testsError
        }
    }
    }
}