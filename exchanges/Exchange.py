import requests

class Exchange:
    def __init__(self, name, api_url):
        self.name = name
        self.api_url = api_url

    def get_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_bid_ask_prices(self):
        data = self.get_data()
        if data:
            return self.extract_bid_ask_prices(data)
        else:
            return None

    def extract_bid_ask_prices(self, data):
        raise NotImplementedError
    
    def extract_bid_ask_quantities(self, data):
        raise NotImplementedError
    
    def get_bid_ask_quantities(self):
        data = self.get_data()
        if data:
            return self.extract_bid_ask_quantities(data)
        else:
            return None