from exchanges.Exchange import Exchange

class OkxExchange(Exchange):
    def __init__(self):
        super().__init__('Okx', "https://www.okex.com/api/spot/v3/instruments/BTC-USDT/book?size=1")

    def extract_bid_ask_prices(self, data):
        return float(data['bids'][0][0]), float(data['asks'][0][0])
    
    def extract_bid_ask_quantities(self, data):
        return float(data['bids'][0][1]), float(data['asks'][0][1])