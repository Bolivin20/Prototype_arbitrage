from exchanges.Exchange import Exchange

class UpbitExchange(Exchange):
    def __init__(self):
        super().__init__('Upbit', "https://api.upbit.com/v1/orderbook?markets=USDT-BTC")

    def extract_bid_ask_prices(self, data):
        return float(data[0]['orderbook_units'][0]['bid_price']), float(data[0]['orderbook_units'][0]['ask_price'])
    
    def extract_bid_ask_quantities(self, data):
        return float(data[0]['orderbook_units'][0]['bid_size']), float(data[0]['orderbook_units'][0]['ask_size'])