pipeline {
  agent any

  
  stages {
    stage('Version') {
      steps {
        sh 'python3 --version'
      }

    }
 
    stage('Install dependency') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Running Test') {
      steps {
        sh 'python3  -m pytest -v --tb=line tests/ --disable-warnings --html=report.html --title="Report QAE Test BE"  --self-contained-html '
      }
      post {
    always {
        publishHTML (target: [

              allowMissing: false,
              alwaysLinkToLastBuild: false,
              keepAll: true,
              reportDir: '',
              reportFiles: "pytest_html_report.html",
              reportName: "Report"])
    }
  }      
 }     
  }

def notifySlack(String buildStatus = 'STARTED') {
    // Build status of null means success.
    buildStatus = buildStatus ?: 'SUCCESS'

    def color

    if (buildStatus == 'STARTED') {
        color = '#D4DADF'
    } else if (buildStatus == 'SUCCESS') {
        color = '#BDFFC3'
    } else if (buildStatus == 'UNSTABLE') {
        color = '#FFFE89'
    } else {
        color = '#FF9FA1'
    }

    def msg = "${buildStatus}: `${env.JOB_NAME}` #${env.BUILD_NUMBER}:\n${env.BUILD_URL}"

    slackSend(color: color, message: msg)
}

node {
    try {
        notifySlack()

        // Existing build steps.
    } catch (e) {
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        notifySlack(currentBuild.result)
    }
}



}
