from ArbitrageBot import ArbitrageBot
from exchanges.BinanceExchange import BinanceExchange
from exchanges.HuobiExchange import HuobiExchange
import time

if __name__ == '__main__':
    binance = BinanceExchange()
    huobi = HuobiExchange()
    exchanges = [binance, huobi]

    bot = ArbitrageBot(exchanges)

    while True:
        bot.arbitrage()
        #time.sleep(8)