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
        slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "good", message: "Instalando dependencia")
      }
    }
    stage('Running Test') {
      steps {
        sh 'python3  -m pytest -v --tb=line tests/ --disable-warnings --html=report.html --title="Report QAE Test BE"  --self-contained-html '
        slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "good", message: "Executando Testes")
      }
      post {
        
     
        
    always {
        slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "good", message: "Report gerado !!!")
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
}
