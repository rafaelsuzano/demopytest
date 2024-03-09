# Teste de API - pytest
Projeto demostração de teste de api com pytest

Pré requisitos:
  - Python instalado
  - pip install pytest
  - pip install pytest-reporter
  -  pip install pytest-html
  - pip install urllib3
  - pip  install requests

Command Line para executar o teste:
  - python  -m pytest -v --tb=line tests/ --disable-warnings --html=report.html --title="Report QAE Test Demo"  --self-contained-html 
  - python3 -m pytest  --tb=line tests/ --excelreport=report.xls
Relatório do Teste

Medium : https://medium.com/@rafasuzano/teste-api-pytest-df815f72fa40

Referência: https://docs.pytest.org/en/6.2.x/contents.html
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "default-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' 'unsafe-inline' data:;")
