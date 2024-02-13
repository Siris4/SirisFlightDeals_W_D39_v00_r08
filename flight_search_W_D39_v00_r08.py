import os
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY', 'Custom Message / Key does not exist')

class FlightSearch:
    # this class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # GET request from Tequila API

        headers = {
            "apikey": TEQUILA_API_KEY
            }

        # city_name="City_name test: PRG"

        query_params = {
            "term":city_name,
            "locale":"en-US",
            "location_types":"airport",
            "limit":7,
            "active_only":"true",
        }
        # iata_code = flight_search.get_destination_code(row["city"])
        query_request_url = "https://api.tequila.kiwi.com/locations/query"      #  toss this: f"{TEQUILA_ENDPOINT}/locations/query"
        query_response = requests.get(url=query_request_url, headers=headers, params=query_params)

        query_response.raise_for_status()
        query_data = query_response.json()
        # print(f"The query_data is: {query_data}")

        for city_iteration in range(query_params['limit']):
            global IATA_city_code
            IATA_city_code = query_data['locations'][city_iteration]['code']

            # return "TESTING" code for now, to ensure it's working. We can get Tequila API data later:
            dest_code = IATA_city_code   #entered into IATA Code column of that particular row's city name
            print(dest_code)
            return dest_code