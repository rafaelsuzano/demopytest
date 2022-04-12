import urllib3
import requests
import json
import pytest
urllib3.disable_warnings()

class Test_API():

    @pytest.mark.order(1) 
    def test_Get_Status200(self):

        url ="https://jsonplaceholder.typicode.com/todos/1"
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


        headers= {'Content-type': 'application/json; charset=UTF-8'}

        r = requests.put(url, data=body,headers=headers)
        print("Response:"+str(r.content))
        print("Code HTTP:"+str(r.status_code))
        assert r.status_code == 200, f"Erro no http status code"
    
    @pytest.mark.order(3) 
    def test_Delete_InserirDados(self):
        url= "https://jsonplaceholder.typicode.com/posts/2"
        r1 = requests.delete(url)
        print("Response:"+str(r1.content))
        print("Code HTTP:"+str(r1.status_code))
        assert r1.status_code == 200, f"Erro no http status code"

    @pytest.mark.order(4) 
    def test_Verifica_Dados_Json(self):
        url ="https://jsonplaceholder.typicode.com/todos/1"
        json_data = requests.get(url, verify=False).json()
        print(json_data)
        print(json_data['completed'])
        completed=(json_data['completed'])
        assert completed == True, f"Retorno do completed era esperado True"
