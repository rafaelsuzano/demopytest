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
    post{
        always{
            slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "good", message: "Test Email")
        }
 
 
 
  }     
  }
}
