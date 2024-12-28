import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
load_dotenv()

class DataManager:
    
    def __init__(self):
        self._sheety_endpoint = os.getenv("SHEETY_ENDPOINT") 
        self._username = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._auth = HTTPBasicAuth(self._username, self._password)
        self.sheet_data = []
        
    def get_data(self):
        response = requests.get(self._sheety_endpoint,auth=self._auth)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def post_data(self,iataCode,city_id):
        new_data = { 
            "price":{
                "iataCode": iataCode
            }
        }
        response = requests.put(url=f"{self._sheety_endpoint}/{city_id}",json=new_data,auth=self._auth)
        print(response.text)
        