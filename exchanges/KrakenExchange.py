from exchanges.Exchange import Exchange

class KrakenExchange(Exchange):
    def __init__(self):
        super().__init__('Kraken', "https://api.kraken.com/0/public/Depth?pair=BTCUSDT")

    def extract_bid_ask_prices(self, data):

        if "XBTUSDT" in data['result']:
            bids = data['result']['XBTUSDT']['bids']
            asks = data['result']['XBTUSDT']['asks']
        elif "ETHUSDT" in data['result']:
            bids = data['result']['ETHUSDT']['bids']
            asks = data['result']['ETHUSDT']['asks']
        

        bid_price = float(bids[0][0])
        ask_price = float(asks[0][0])

        return bid_price, ask_price
    
    def extract_bid_ask_quantities(self, data):

        if "XBTUSDT" in data['result']:
            bids = data['result']['XBTUSDT']['bids']
            asks = data['result']['XBTUSDT']['asks']
        elif "ETHUSDT" in data['result']:
            bids = data['result']['ETHUSDT']['bids']
            asks = data['result']['ETHUSDT']['asks']

        bid_qty = float(bids[0][1])
        ask_qty = float(asks[0][1])

        return bid_qty, ask_qty