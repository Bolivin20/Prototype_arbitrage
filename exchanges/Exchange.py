import requests
from requests.exceptions import ConnectionError, RequestException
import time

class Exchange:
    def __init__(self, name, api_url):
        self.name = name
        self.api_url = api_url

    def symbolUrl(self,symbol):
        if "btc" in self.api_url:
            symbol = symbol.lower()
            universalUrl = self.api_url.replace("btc", symbol)
        elif "BTC" in self.api_url:
            symbol = symbol.upper()
            universalUrl = self.api_url.replace("BTC", symbol)

        return universalUrl
    
    def get_data(self, symbol):
        delay = 10
        attempts = 0
        while attempts < 5:
            try:
                response = requests.get(self.symbolUrl(symbol))
                response.raise_for_status()
                return response.json()
            except ConnectionError as ce:
                print(f"Błąd połączenia: {ce}")
            except RequestException as re:
                print(f"Inny błąd żądania: {re}")
            except Exception as e:
                print(f"Inny nieobsługiwany błąd: {e}")

            attempts += 1
            time.sleep(delay)
            delay += 10

        print(f"Nie udało się pobrać danych po 5 próbach.")
        return None

    def get_bid_ask_prices(self, symbol):
        delay = 10
        attempts = 0

        while attempts < 5:
            data = self.get_data(symbol)
            
            if data:
                return self.extract_bid_ask_prices(data)
            else:
                attempts += 1
                print(f"Nie udało się pobrać danych. Ponawiam próbę.")
                time.sleep(delay)
                delay += 10

        print(f"Nie udało się pobrać danych po 5 próbach.")
        return None

    def extract_bid_ask_prices(self, data):
        raise NotImplementedError
    
    def extract_bid_ask_quantities(self, data):
        raise NotImplementedError
    
    def get_bid_ask_quantities(self, symbol):
        delay = 10
        attempts = 0

        while attempts < 5:
            data = self.get_data(symbol)
            
            if data:
                return self.extract_bid_ask_quantities(data)
            else:
                attempts += 1
                print(f"Nie udało się pobrać danych. Ponawiam próbę.")
                time.sleep(delay)
                delay += 10

        print(f"Nie udało się pobrać danych po 5 próbach.")
        return None