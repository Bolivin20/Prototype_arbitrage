import logging
from exchanges.Exchange import Exchange
import time

class ArbitrageBot:
    def __init__(self, exchanges, log_filename):
        self.exchanges = exchanges
        self.MIN_PROFIT_PERCENTAGE = 0.00

        self.logger = logging.getLogger(log_filename)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def calculate_profit(self, buy_price, sell_price, quantity):
        return (sell_price - buy_price) * quantity

    def initialize_data(self, symbol):
        data = {}
        for exchange in self.exchanges:
            bid_price, ask_price = exchange.get_bid_ask_prices(symbol)
            bid_qty, ask_qty = exchange.get_bid_ask_quantities(symbol)

            data[exchange] = (bid_price, ask_price, bid_qty, ask_qty)

        return data

    def find_arbitrage(self, data):
        max_profit = 0.0
        best_opportunity = None
        exchanges_list = list(data.keys())

        for i in range(len(exchanges_list)):
            exchange1 = exchanges_list[i]

            for j in range(len(exchanges_list)):
                if i != j:  
                    exchange2 = exchanges_list[j]
                    bid1, ask1, bidQty1, askQty1 = data[exchange1]
                    bid2, ask2, bidQty2, askQty2 = data[exchange2]

                    if ask1 < bid2:
                        possible_buy = min(askQty1, bidQty2)
                        profit = self.calculate_profit(ask1, bid2, possible_buy)

                        if profit > self.MIN_PROFIT_PERCENTAGE * ask1 * possible_buy and profit > max_profit:
                            max_profit = profit
                            best_opportunity = (exchange1, exchange2, ask1, bid2, askQty1, bidQty2, possible_buy, profit)
                            #print(f'min_zysk: {self.MIN_PROFIT_PERCENTAGE * ask1 * possible_buy}')
                            #print(f"{exchange1.name} {bid1} {ask1} {bidQty1} {askQty1} {exchange2.name} {bid2} {ask2} {bidQty2} {askQty2} : {profit}\n")
           
        return best_opportunity

    def execute_best_arbitrage(self, symbol):
        start_time = time.time()
        best_opportunity = self.find_arbitrage(self.initialize_data(symbol))
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.log_info(f"Czas szukania arbitrażu {elapsed_time:.5f} sekund\n")

        if best_opportunity:
            source_exchange, target_exchange, source_ask_price, target_bid_price, source_ask_qty, target_bid_qty, possible_buy, profit = best_opportunity
            self.log_info(
                f"Potencjalna transakcja: Kupiono {possible_buy:.5f} {symbol} na giełdzie {source_exchange.name} po cenie {source_ask_price:.5f} USDT \n"
                f"Sprzedano {possible_buy:.5f} {symbol} na giełdzie {target_exchange.name} po cenie {target_bid_price:.5f} USDT \n"
                f"Potencjalny zysk: {profit:.5f} USDT\n"
                f"Wolumeny: {source_ask_qty:.5f} {symbol} na {source_exchange.name}, {target_bid_qty:.5f} {symbol} na {target_exchange.name}\n\n")
           
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            data_file = f'results/{symbol}_chart_data.csv'
            open(data_file, 'a').write(f'{current_time},{source_exchange.name},{target_exchange.name},{possible_buy},{profit}\n')
            