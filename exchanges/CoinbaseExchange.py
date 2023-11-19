from exchanges.Exchange import Exchange

class CoinbaseExchange(Exchange):
    def __init__(self):
        super().__init__('Coinbase', "https://api.pro.coinbase.com/products/BTC-USDT/book?level=2")

    def extract_bid_ask_prices(self, data):
        bids = data['bids']
        asks = data['asks']

        bid_price = float(bids[0][0])
        ask_price = float(asks[0][0])

        return bid_price, ask_price
    
    def extract_bid_ask_quantities(self, data):
        bids = data['bids']
        asks = data['asks']

        bid_qty = float(bids[0][1])
        ask_qty = float(asks[0][1])

        return bid_qty, ask_qty