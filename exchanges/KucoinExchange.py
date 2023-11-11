from exchanges.Exchange import Exchange

class KucoinExchange(Exchange):
    def __init__(self):
        super().__init__('Kucoin', "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT")

    def extract_bid_ask_prices(self, data):
        return float(data['data']['bestBid']), float(data['data']['bestAsk'])
    
    def extract_bid_ask_quantities(self, data):
        return float(data['data']['bestBidSize']), float(data['data']['bestAskSize'])