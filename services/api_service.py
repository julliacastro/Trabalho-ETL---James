import requests

class ApiService:
    @staticmethod
    def fetch_data(endpoint):
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Falha ao obter dados da API: {response.status_code}")
