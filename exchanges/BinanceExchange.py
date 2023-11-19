from exchanges.Exchange import Exchange

class BinanceExchange(Exchange):
    def __init__(self):
        super().__init__('Binance', "https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT")

    def extract_bid_ask_prices(self, data):
        return float(data['bidPrice']), float(data['askPrice'])
    
    def extract_bid_ask_quantities(self, data):
        return float(data['bidQty']), float(data['askQty'])
    