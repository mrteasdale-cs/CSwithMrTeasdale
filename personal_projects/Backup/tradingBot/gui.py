from tkinter import *
import bot as tb

def beginTrading():
    symbol = str(symbol_text.get())
    qty = float(qty_text.get())
    result = ""

def clearAll():
    symbol_text.delete('0',END)
    qty_text.delete('0',END)
    resultLabel.config(text='',bg='linen')

def createGUI(ema1, ema2, ema3, rsi):

    window = Tk()
    window.title("Python Trading Bot")
    #window.geometry('450x350')
    window.config(bg='linen')

    instruc = Label(window, width=30, height=2, text='Welcome to the trading bot v1.0, please set your trade SYBMOL and QUANTIY to trade before you begin', bg='linen')
    instruc.grid(row=1, column=0, columnspan=2)

    symbol_label = Label(window, width=20, height=1, text='Symbol', bg='yellow')
    symbol_label.grid(row=2, column=0)
    symbol_text = Entry(window, width=5)
    symbol_text.grid(row=2, column=1)

    #label and text box for max marks
    qty_label = Label(window, width=10, height=1, text='Quantity', bg='yellow')
    qty_label.grid(row=3, column=0)
    qty_text = Entry(window, width=5)
    qty_text.grid(row=3, column=1)

    #buttons
    begin_Button = Button(window, text='Begin!', width=10, command=beginTrading)
    begin_Button.grid(row=5, column=0)
    clear_Button = Button(window, text='Clear', width=10, command=clearAll)
    clear_Button.grid(row=5, column=1)

    output_label1 = Label(window, width=100, height=100, text='EMA 25', bg='linen')
    output_label1.grid(row=6)
    resultLabel1 = Label(window, width=15, height=2, text='', bg='linen')
    resultLabel1.grid(row=6, column=1)
    output_label2 = Label(window, width=100, height=100, text='EMA 50', bg='linen')
    output_label2.grid(row=6)
    resultLabel2 = Label(window, width=15, height=2, text='', bg='linen')
    resultLabel2.grid(row=6, column=1)
    output_label3 = Label(window, width=100, height=100, text='EMA 100', bg='linen')
    output_label3.grid(row=6)
    resultLabel3 = Label(window, width=15, height=2, text='', bg='linen')
    resultLabel3.grid(row=6, column=1)
    output_label4 = Label(window, width=100, height=100, text='RSI', bg='linen')
    output_label4.grid(row=6)
    resultLabel4 = Label(window, width=15, height=2, text='', bg='linen')
    resultLabel4.grid(row=6, column=1)

    output_label1.config(text=ema1)
    output_label2.config(text=ema2)
    output_label3.config(text=ema3)
    output_label4.config(text=rsi)

    window.mainloop()