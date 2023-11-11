from ArbitrageBot import ArbitrageBot
from exchanges.BinanceExchange import BinanceExchange
from exchanges.HuobiExchange import HuobiExchange
from exchanges.MexcExchange import MexcExchange
from exchanges.KrakenExchange import KrakenExchange
from exchanges.CoinbaseExchange import CoinbaseExchange
from exchanges.KucoinExchange import KucoinExchange
from exchanges.UpbitExchange import UpbitExchange

if __name__ == '__main__':
    binance = BinanceExchange()
    huobi = HuobiExchange()
    #mexc = MexcExchange()
    kraken = KrakenExchange()
    coinbase = CoinbaseExchange()
    #kucoin = KucoinExchange()
    upbit = UpbitExchange()

    exchanges = [binance, huobi, kraken, coinbase]

    bot = ArbitrageBot(exchanges)

    while True:
        bot.execute_best_arbitrage()
        #time.sleep(8)