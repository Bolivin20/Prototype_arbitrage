import time
import logging
from exchanges.Exchange import Exchange
from exchanges.BinanceExchange import BinanceExchange
from exchanges.HuobiExchange import HuobiExchange

class ArbitrageBot:
    def __init__(self, exchanges):
        self.exchanges = exchanges
        self.MIN_PROFIT_PERCENTAGE = 0.0
        self.QUANTITY_TO_TRADE = {
            'Binance_BTC': 0.5,
            'Binance_USDT': 15000.0,
            'Huobi_BTC': 0.5,
            'Huobi_USDT': 1500.0
        }

        # Initialize logging
        logging.basicConfig(filename="results/log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

    def log_info(self, message):
        logging.info(message)
        print(message)

    def check_balances(self):
        return all(balance >= 0 for balance in self.QUANTITY_TO_TRADE.values())

    def calculate_profit(self, buy_price, sell_price, quantity):
        return (sell_price - buy_price) * quantity

    def arbitrage(self):
        for i in range(len(self.exchanges)):
            exchange1 = self.exchanges[i]
            for j in range(i + 1, len(self.exchanges)):
                exchange2 = self.exchanges[j]
                self.perform_arbitrage(exchange1, exchange2)

    def perform_arbitrage(self, exchange1, exchange2):
        bid1, ask1 = exchange1.get_bid_ask_prices()
        bid2, ask2 = exchange2.get_bid_ask_prices()

        if bid1 < ask2:
            self.execute_arbitrage(exchange1, exchange2, ask1, bid2)
        elif bid2 < ask1:
            self.execute_arbitrage(exchange2, exchange1, ask2, bid1)

    def execute_arbitrage(self, source_exchange, target_exchange, source_ask_price, target_bid_price):
        possible_buy = min(
            self.QUANTITY_TO_TRADE[f'{source_exchange.name}_USDT'] / source_ask_price,
            self.QUANTITY_TO_TRADE[f'{target_exchange.name}_BTC']
        )
        profit = self.calculate_profit(source_ask_price, target_bid_price, possible_buy)

        if profit > self.MIN_PROFIT_PERCENTAGE * self.QUANTITY_TO_TRADE[f'{source_exchange.name}_USDT']:
            source_currency = f'{source_exchange.name}_BTC'
            target_currency = f'{target_exchange.name}_BTC'
            self.QUANTITY_TO_TRADE[source_currency] += possible_buy
            self.QUANTITY_TO_TRADE[target_currency] -= possible_buy
            self.QUANTITY_TO_TRADE[f'{target_exchange.name}_USDT'] += possible_buy * target_bid_price
            self.QUANTITY_TO_TRADE[f'{source_exchange.name}_USDT'] -= possible_buy * source_ask_price

            self.log_info(f"Kupiono {possible_buy:.5f} BTC na giełdzie {source_exchange.name} po cenie {source_ask_price:.5f} USDT \n"
                          f"Sprzedano {possible_buy:.5f} BTC na giełdzie {target_exchange.name} po cenie {target_bid_price:.5f} USDT \n"
                          f"Zysk: {profit:.5f} USDT\n"
                          f"Stan konta na giełdzie {source_exchange.name}: {self.QUANTITY_TO_TRADE[f'{source_exchange.name}_USDT']:.5f} USDT oraz {self.QUANTITY_TO_TRADE[source_currency]:.5f} BTC \n"
                          f"Stan konta na giełdzie {target_exchange.name}: {self.QUANTITY_TO_TRADE[f'{target_exchange.name}_USDT']:.5f} USDT oraz {self.QUANTITY_TO_TRADE[target_currency]:.5f} BTC\n\n")
