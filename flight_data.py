import requests
import os
from dotenv import load_dotenv
from flight_search import FlightSearch
from data_manager import DataManager
import datetime

load_dotenv()
class FlightData:
    
    def __init__(self):
        flight_search = FlightSearch()
        self._endpoint = os.environ["AMADEUS_OFFERS_ENDPOINT"]
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._secret = os.environ["AMADEUS_API_SECRET"]
        self._token = flight_search.get_api_key()
    
    def find_price(self,start_city,end_city):
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            "originLocationCode": start_city,
            "destinationLocationCode": end_city,
            "departureDate": self.date_now(),
            "adults": 1
        }
        response = requests.get(url=self._endpoint,headers=headers,params=params)
        try:
            price_data = response.json()["data"][0]["price"]["total"]
        except:
            print_data = "N/A"
        return price_data
    
    def date_now(self):
        timenow = datetime.datetime.now()
        timenow_fomat =  str(timenow).split(" ")[0]
        return timenow_fomat