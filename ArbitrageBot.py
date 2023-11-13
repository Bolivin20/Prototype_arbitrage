import logging
from exchanges.Exchange import Exchange
import time

class ArbitrageBot:
    def __init__(self, exchanges):
        self.exchanges = exchanges
        self.MIN_PROFIT_PERCENTAGE = 0.0

        # Initialize logging
        logging.basicConfig(filename="results/logi1.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

    def log_info(self, message):
        logging.info(message)
        #print(message)

    def calculate_profit(self, buy_price, sell_price, quantity):
        return (sell_price - buy_price) * quantity

    def sort_exchange_data(self, exchange):
        bid_price, ask_price = exchange.get_bid_ask_prices()
        bid_qty, ask_qty = exchange.get_bid_ask_quantities()

    # Sortowanie malejące
        sorted_data = [(bid_price, ask_price, bid_qty, ask_qty)]

        return sorted_data


    def find_best_arbitrage_opportunity(self):
        best_opportunity = None
        max_profit = 0.0

        sorted_data = [self.sort_exchange_data(exchange) for exchange in self.exchanges]

        min_profit_percentage_check = self.MIN_PROFIT_PERCENTAGE

        for i, (exchange1, sorted_data1) in enumerate(zip(self.exchanges, sorted_data)):
            for j, (exchange2, sorted_data2) in enumerate(zip(self.exchanges[i + 1:], sorted_data[i + 1:]), start=i + 1):
                bid1, ask1, bidQty1, askQty1 = sorted_data1[0]
                bid2, ask2, bidQty2, askQty2 = sorted_data2[0]

                if bid1 < ask2:
                    possible_buy = min(askQty1, bidQty2)
                    profit = self.calculate_profit(ask1, bid2, possible_buy)

                    if profit > max_profit and profit > min_profit_percentage_check * ask1 * possible_buy:
                        best_opportunity = (exchange1, exchange2, ask1, bid2, askQty1, bidQty2, possible_buy, profit)
                        max_profit = profit
                elif bid2 < ask1:
                    possible_buy = min(askQty2, bidQty1)
                    profit = self.calculate_profit(ask2, bid1, possible_buy)

                    if profit > max_profit and profit > min_profit_percentage_check * ask2 * possible_buy:
                        best_opportunity = (exchange2, exchange1, ask2, bid1, askQty2, bidQty1, possible_buy, profit)
                        max_profit = profit

        return best_opportunity


    def execute_best_arbitrage(self):
        start_time = time.time()
        best_opportunity = self.find_best_arbitrage_opportunity()
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.log_info(f"Czas szukania arbitrażu {elapsed_time:.5f} sekund\n")

        if best_opportunity:
            source_exchange, target_exchange, source_ask_price, target_bid_price, source_ask_qty, target_bid_qty, possible_buy, profit = best_opportunity
            self.log_info(f"Potencjalna transakcja: Kupiono {possible_buy:.5f} BTC na giełdzie {source_exchange.name} po cenie {source_ask_price:.5f} USDT \n"
                          f"Sprzedano {possible_buy:.5f} BTC na giełdzie {target_exchange.name} po cenie {target_bid_price:.5f} USDT \n"
                          f"Potencjalny zysk: {profit:.5f} USDT\n"
                          f"Wolumeny: {source_ask_qty:.5f} BTC na {source_exchange.name}, {target_bid_qty:.5f} BTC na {target_exchange.name}\n\n")
