import requests

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
        response = requests.get(self.symbolUrl(symbol))
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_bid_ask_prices(self, symbol):
        data = self.get_data(symbol)
        if data:
            return self.extract_bid_ask_prices(data)
        else:
            return None

    def extract_bid_ask_prices(self, data):
        raise NotImplementedError
    
    def extract_bid_ask_quantities(self, data):
        raise NotImplementedError
    
    def get_bid_ask_quantities(self, symbol):
        data = self.get_data(symbol)
        if data:
            return self.extract_bid_ask_quantities(data)
        else:
            return None