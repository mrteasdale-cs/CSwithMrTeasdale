import config, pprint, json, websocket, talib, csv, numpy as np, get_data#, TradingGui
from binance.client import Client
from binance.enums import *
client = Client(config.API_KEY, config.API_SECRET)

print("Welcome to the Python Trading Bot\n"
      "=================================")

#Setup trade information
TRADE_SYMBOL = "BTCUSDT"
TRADE_QTY = 0.0003
#TRADE_SYMBOL = str(input("\n\nAll symbols for streams are lowercase "
                   #"(e.g ethusdt for Etherium and USD Tether\n"
                   #"Enter the Crypto pair for your stream:"))
#TRADE_QTY = float(input("\nEnter amount to trade with: "))
SPOT_SOCKET = "wss://stream.binance.com/ws/" + TRADE_SYMBOL + "@kline_1h"
#SPOT_SOCKET = "wss://stream.binance.com:9443/ws/manausdt@kline_5m"
#FUTURES_SOCKET = "wss://fstream.binance.com/ws/busdt@kline_1h"
candle_closes = []
in_position = False
#MA
EMA1 = 25
EMA2 = 50
EMA3 = 100
#RSI Indicator
RSI_PERIOD = 14
RSI_OVERBOUGHT = 65
RSI_OVERSOLD = 35


#Import historical candles 
candle_closes = get_data.getHistoricalCandles(TRADE_SYMBOL)

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        #order = client.create_order(symbol=symbol,side=side,type=order_type,quantity=quantity)
        print(order)
        print("Order Successful")
    except Exception as e:
        print("Problem with order!")
        return False
    return True

def on_close(webSoc):
    print("Connection closed")

def on_open(webSoc):
    print("Connection opened")

def on_error(ws, error):
    print(error)

def on_message(webSoc, message):
    global candle_closes
    global in_position
    global order_success
    global max_candle

    json_msg = json.loads(message)
    #pprint.pprint(json_msg)
    print("Previous Closed Candle: {}".format(candle_closes[-1]))
    print("Current Candle\n=============")
    print("PAIR: ",json_msg['s'],"\nHIGH: ",json_msg['k']['h'],"\nLOW: ",json_msg['k']['l'],"\nOPEN: ",json_msg['k']['o'],"\nCLOSE: ",json_msg['k']['c'])

    candle = json_msg['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("Candle closed at {}".format(close))
        candle_closes.append(float(close))
        print("All Candle Closes\n"
              "-------------------")

    if len(candle_closes) > EMA1:
        np_closesEMA = np.array(candle_closes)
        ema25 = talib.EMA(np_closesEMA, timeperiod=25)
        last_ema25 = ema25[-1]
        print("Current 25 ema is: {}".format(ema25[-1]))
        #return ema25[-1]

    if len(candle_closes) > EMA2:
        np_closesEMA = np.array(candle_closes)
        ema50 = talib.EMA(np_closesEMA, timeperiod=50)
        last_ema50 = ema50[-1]
        print("Current 50 ema is: {}".format(ema50[-1]))
        #return ema50[-1]

    if len(candle_closes) > EMA3:
        np_closesEMA = np.array(candle_closes)
        ema100 = talib.EMA(np_closesEMA, timeperiod=100)
        last_ema100 = ema100[-1]
        print("Current 100 ema is: {}".format(ema100[-1]))
        #return ema100[-1]

    if len(candle_closes) > RSI_PERIOD:
        np_closesRSI = np.array(candle_closes)
        rsi = talib.RSI(np_closesRSI, RSI_PERIOD)
        #print("RSI's so far: ",rsi)
        last_rsi = rsi[-1]
        print("The current RSI is {}".format(last_rsi))
        #return rsi[-1]
    
        #buy logic
    #Check market in an uptrend (long position)
    #if (ema100 < ema50) and (ema100 < ema25) and (ema50 < ema25):
    #if candle_closes:

    #if closed candle is above the 25 moving average and the RSI is overbought/oversold
        
    order_success = False
    if candle_closes[-1] < last_ema25:
        if last_rsi < RSI_OVERSOLD:
            print("BUY!!! BUY!!! BUY!!!")
            if in_position:
                #order_success = order(SIDE_BUY, TRADE_QTY, TRADE_SYMBOL, ORDER_TYPE_MARKET)
                order_success = True
                print("Buy order successful")
                return order_success
                if (order_success):
                    in_position = True
            else:
                print("Coin is oversold and below 25 EMA but we are not in position")

    if candle_closes[-1] > last_ema25:
        if candle_closes[-1] > last_ema50:
                if last_rsi < RSI_OVERBOUGHT:
                    print("BUY!!! BUY!!! BUY!!!")
                    if in_position:
                        order_success = True
                        #order_success = order(SIDE_BUY, TRADE_QTY, TRADE_SYMBOL, ORDER_TYPE_MARKET)
                        print("Buy order successful")
                        #return order_success
                    if (order_success):
                        in_position = True
                    else:
                        print("Coin is oversold and below 25 EMA but we are not in position")

        percentAboveema25 = last_ema25*1.05
        if candle_closes[-1] > percentAboveema25 or last_rsi > RSI_OVERBOUGHT:
            print("SELL!!! SELL!!! SELL!!!")
            if in_position:
               #order_success = order(SIDE_SELL, TRADE_QTY, TRADE_SYMBOL, ORDER_TYPE_MARKET)
               order_success = True
               print("Sell order successful")
               return order_success
               if (order_success):
                    in_position = False
            else:
                print("Coin is overbought and above the 25&50 EMA but we are currently not in position.")


webSoc = websocket.WebSocketApp(SPOT_SOCKET, on_close=on_close, on_open=on_open, on_message=on_message, on_error=on_error)
webSoc.run_forever()