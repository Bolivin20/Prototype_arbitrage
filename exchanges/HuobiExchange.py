from exchanges.Exchange import Exchange

class HuobiExchange(Exchange):
    def __init__(self):
        super().__init__('Huobi', "https://api.huobi.pro/market/depth?symbol=btcusdt&type=step0")

    def extract_bid_ask_prices(self, data):
        bid_price = float(data['tick']['bids'][0][0])
        ask_price = float(data['tick']['asks'][0][0])
        return bid_price, ask_price