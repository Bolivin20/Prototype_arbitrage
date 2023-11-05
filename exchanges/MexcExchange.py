from exchanges.Exchange import Exchange

class MexcExchange(Exchange):
    def __init__(self):
        super().__init__('Mexc', "https://api.mexc.com/api/v3/depth?symbol=BTCUSDT")

    def extract_bid_ask_prices(self, data):
        bids = data['bids']
        asks = data['asks']

        bid_price = float(bids[0][0])
        ask_price = float(asks[0][0])

        return bid_price, ask_price
