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
        source bin/activate
        python3 -m pip install -r requirements.txt
        deactivate
       '''
    }
    stage ("Run Unit/Integration Tests") {
    def testsError = null
    try {
        sh '''
            source ../bin/activate
            python3 ./manage.py jenkins
            deactivate
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
