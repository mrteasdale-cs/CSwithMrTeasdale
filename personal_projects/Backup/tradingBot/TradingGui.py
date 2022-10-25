import tkinter as tk, matplotlib, matplotlib.animation as animation #,get_data, bot
from tkinter import ttk
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
style.use("ggplot")



class TradingGui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Python Trading Bot")
        tk.Frame(bg='linen')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MainPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to the Auto Trading Bot", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="a tool to automate trading of cryptocurrencies on the binance exchange",
                          font=NORMAL_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Go to main page",
                            comman=lambda: controller.show_frame(MainPage))
        button1.pack()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def beginTrading():
            symbol = str(symbol_text.get())
            qty = float(qty_text.get())
            result = "Working with: "+symbol+" pair @ "+str(qty)+" quantity"
            labelInfo.config(text=result,bg='linen')
            
            #bot.runWebSocket()
            
            return symbol, qty

        def exit():
            tk._exit()

        labelIntro1 = tk.Label(self, text="Welcome!", font=LARGE_FONT)
        labelIntro1.grid(row=0, columnspan=5, pady=5)
        labelIntro2 = tk.Label(self,
                                text="to get started, type in a trading SYMBOL and QUANTITY you wish to trade with",
                                font=NORMAL_FONT)
        labelIntro2.grid(row=1, columnspan=5, pady=5)        

        symbol_label = tk.Label(self, width=10, height=1, text='Symbol')
        symbol_label.grid(row=2, column=0, pady=10)
        symbol_text = tk.Entry(self, width=10)
        symbol_text.grid(row=2, column=1)

        # label and text box for max marks
        qty_label = tk.Label(self, width=10, height=1, text='Quantity')
        qty_label.grid(row=3, column=0)
        qty_text = tk.Entry(self, width=10)
        qty_text.grid(row=3, column=1)

        # buttons
        begin_Button = ttk.Button(self, text='Begin!', width=10, command=beginTrading)
        begin_Button.grid(row=2, column=3)
        clear_Button = ttk.Button(self, text='Exit', width=10, command=exit)
        clear_Button.grid(row=3, column=3)

        labelInfo = tk.Label(self,
                                text="NOT STARTED",
                                font=NORMAL_FONT)
        labelInfo.grid(row=4, rowspan=2, columnspan=5, pady=2)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, columnspan=5)

        #toolbar = NavigationToolbar2Tk(canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack()



app = TradingGui()
app.mainloop()