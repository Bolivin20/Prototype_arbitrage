from exchanges.Exchange import Exchange

class BybitExchange(Exchange):
    def __init__(self):
        super().__init__('Bybit', "https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT")

    def extract_bid_ask_prices(self, data):
        return float(data['result'][0]['bid_price']), float(data['result'][0]['ask_price'])