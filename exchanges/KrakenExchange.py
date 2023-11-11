from exchanges.Exchange import Exchange

class KrakenExchange(Exchange):
    def __init__(self):
        super().__init__('Kraken', "https://api.kraken.com/0/public/Depth?pair=BTCUSDT")

    def extract_bid_ask_prices(self, data):
        bids = data['result']['XBTUSDT']['bids']
        asks = data['result']['XBTUSDT']['asks']

        bid_price = float(bids[0][0])
        ask_price = float(asks[0][0])

        return bid_price, ask_price
    
    def extract_bid_ask_quantities(self, data):
        bids = data['result']['XBTUSDT']['bids']
        asks = data['result']['XBTUSDT']['asks']

        bid_qty = float(bids[0][1])
        ask_qty = float(asks[0][1])

        return bid_qty, ask_qty