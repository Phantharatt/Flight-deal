#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
dm = DataManager()
fs = FlightSearch()
fd = FlightData()
dm.get_data()
for data in dm.get_data():
    city = data["city"]
    city_id = data["id"]
    iataCode = fs.city_search(city)
    dm.post_data(iataCode,city_id)
    

for data in dm.get_data():
    city = data["city"]
    iatacode = data["iataCode"]
    price = fd.find_price("LON",iatacode)
    print(f"Getting Flights for {city} ...")
    print(f"{city} : {price}")