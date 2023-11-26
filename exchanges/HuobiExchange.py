from exchanges.Exchange import Exchange

class HuobiExchange(Exchange):
    def __init__(self):
        super().__init__('Huobi', "https://api.huobi.pro/market/depth?symbol=btcusdt&type=step0")

    def extract_bid_ask_prices(self, data):
        try:
            bid_price = float(data['tick']['bids'][0][0])
            ask_price = float(data['tick']['asks'][0][0])
            return bid_price, ask_price
        except KeyError as e:
            print(f"Wystąpił KeyError: {e}. Brak klucza 'tick' lub jego podkluczy w danych.")
            return -1, -1
    
    def extract_bid_ask_quantities(self, data):
        try:
            bid_qty = float(data['tick']['bids'][0][1])
            ask_qty = float(data['tick']['asks'][0][1])
            return bid_qty, ask_qty
        except KeyError as e:
            print(f"Wystąpił KeyError: {e}. Brak klucza 'tick' lub jego podkluczy w danych.")
            return -1, -1