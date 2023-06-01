import urllib3
import requests
import json
import pytest
import sys, os

urllib3.disable_warnings()

#python3 -m pytest --markers - --tb=line tests/ --excelreport=report.xls



class Test_API():

    @pytest.mark.order(1) 
    def test_Get_Status200(self):

        url ="https://jsonplaceholder.typicode.com/todos/1"
        print(url)
        r = requests.get(url, verify=False)
        print("Response:"+str(r.content))
        print("Code HTTP:"+str(r.status_code))
        assert r.status_code == 200, f"Erro no http status code"
        
    @pytest.mark.order(2)    
    def test_Put_InserirDados(self):
        url= "https://jsonplaceholder.typicode.com/posts/2"
        body = {
            "id":1,
            "title": 'teste demo',
            "body": 'bar',
            "userId":1
        }
        body = json.dumps(body)
        print(url)

        headers= {'Content-type': 'application/json; charset=UTF-8'}

        r = requests.put(url, data=body,headers=headers)
        print("Response:"+str(r.content))
        print("Code HTTP:"+str(r.status_code))
        assert r.status_code == 200, f"Erro no http status code"
    
    @pytest.mark.order(3) 
    def test_Delete_InserirDados(self):
        url= "https://jsonplaceholder.typicode.com/posts/2"
        r1 = requests.delete(url)
        print(url)
        print("Response:"+str(r1.content))
        print("Code HTTP:"+str(r1.status_code))
        assert r1.status_code == 200, f"Erro no http status code"

    @pytest.mark.order(4) 
    def test_Verifica_Dados_Json(self):
        url ="https://jsonplaceholder.typicode.com/todos/1"
        json_data = requests.get(url, verify=False).json()
        print(url)
        print(json_data)
        print(json_data['completed'])
        completed=(json_data['completed'])
        assert True == True, f"Retorno do completed era esperado True"
        
    @pytest.mark.order(5) 
    def test_Verifica_Dados_Json(self):
        url ="https://jsonplaceholder.typicode.com/todos/1"
        json_data = requests.get(url, verify=False).json()
        print(url)
        print(json_data)
        print(json_data['completed'])
        completed=(json_data['completed'])
        assert True == False, f"Retorno do completed era esperado True"
os._exit(0)       
        
