pipeline {
  agent any

  
  stages {
    stage('Version') {
      steps {
        bat  'python3 --version'
      }

    }



    stage('Install dependency') {
      steps {
        bat  'pip install -r requirements.txt'
        slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "0046FF", message: "Instalando dependencia ${env.JOB_NAME}  build ${env.BUILD_NUMBER} ")
      }
    }
    stage('Running Test') {
      steps {
              slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "F7FF00", message: "Executando Testes ${env.JOB_NAME} build ${env.BUILD_NUMBER} ")
        bat  'python3  -m pytest -v --tb=line tests/ --disable-warnings --html=report.html --title="Report QAE Test BE"  --self-contained-html '
  
      }
      post {

           success {
           slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "good", message: "Report gerado com sucesso ${env.JOB_NAME} build ${env.BUILD_NUMBER} ")
                   publishHTML (target: [

              allowMissing: false,
              alwaysLinkToLastBuild: false,
              keepAll: true,
              reportDir: '',
              reportFiles: "pytest_html_report.html",
              reportName: "Report"]) 
           
           
           }
        
        
          failure {
            
            slackSend( channel: "#testejenkins", token: "yLgYXC6q0hURolpnHGx5cjAi", color: "FF2E00", message: "Report gerado com erro ${env.JOB_NAME}  build ${env.BUILD_NUMBER}")
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
