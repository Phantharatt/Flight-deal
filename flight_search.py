import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._token_endpoint = os.environ["AMADEUS_TOKEN_ENDPOINT"]
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._secret = os.environ["AMADEUS_API_SECRET"]
        self._amadeus_endpoint = os.environ["AMADEUS_ENDPOINT"] 
        self._token = self.get_api_key()

    def get_api_key(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        params = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._secret
        }

        response = requests.post(url=self._token_endpoint,headers=header,data=params)
        return response.json()["access_token"]
    
    def city_search(self,city):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city
        }
        print(query)
        response = requests.get(url=self._amadeus_endpoint,headers=headers,params=query)
        data = response.json()
        return data["data"][0]["iataCode"]
            
