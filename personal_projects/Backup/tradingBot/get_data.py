import csv, config, numpy as np
from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)

def getHistoricalCandles(TRADE_SYMBOL):
    #fetch 5 minute klines
    print("Getting historical candles first...")
    fileName = "histCandles.csv"
    hist_candle_closes = []
    #Gets candels between specific dates
    #candles = client.get_historical_klines(TRADE_SYMBOL, Client.KLINE_INTERVAL_5MINUTE, "13 Mar, 2021", current_date+", 2021")
    #Gets candle from past day
    try:
        UPPER = TRADE_SYMBOL.upper()
        candles = client.get_historical_klines(UPPER, Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC+8")
        candlestick_file = open(fileName, 'w', newline='')
        candlestick_writer = csv.writer(candlestick_file, delimiter=',')
        for candlesticks in candles:
            candlestick_writer.writerow(candlesticks)

        candlestick_file = open (fileName, 'r', newline='')
        hist_candle_numpy = np.genfromtxt('histCandles.csv', delimiter=',', usecols=4)
        #colnames = ['time','open', 'high', 'low', 'close']
        #data = pd.read_csv(fileName, names=colnames)
        #hist_candle_closes = data.close.tolist()

        for candles in hist_candle_numpy:
            hist_candle_closes.append(float(candles))

        print("Done. Closing file.")
        candlestick_file.close()
        
        return hist_candle_closes

    except Exception as e:
        print("Something went wrong. Nothing retrieved")
        failedtoopenfile = True
        return failedtoopenfile


