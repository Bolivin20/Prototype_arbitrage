from ArbitrageBot import ArbitrageBot
from exchanges.BinanceExchange import BinanceExchange
from exchanges.HuobiExchange import HuobiExchange
from exchanges.MexcExchange import MexcExchange
from exchanges.KrakenExchange import KrakenExchange
from exchanges.CoinbaseExchange import CoinbaseExchange
from exchanges.KucoinExchange import KucoinExchange
from exchanges.UpbitExchange import UpbitExchange
import threading
import time

if __name__ == '__main__':
    binance = BinanceExchange()
    huobi = HuobiExchange()
    #mexc = MexcExchange()
    kraken = KrakenExchange()
    coinbase = CoinbaseExchange()
    kucoin = KucoinExchange()
    upbit = UpbitExchange()

    exchanges = [binance, huobi, kraken, coinbase, upbit, kucoin]

    def run_bot_with_symbol(symbol):
        log_filename = f"results/{symbol}_log.txt"
        bot = ArbitrageBot(exchanges, log_filename)

        while True:
            bot.execute_best_arbitrage(symbol)
    
    thread1 = threading.Thread(target=run_bot_with_symbol, args=('BTC',))
    thread2 = threading.Thread(target=run_bot_with_symbol, args=('ETH',))
    thread3 = threading.Thread(target=run_bot_with_symbol, args=('DOGE',))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
