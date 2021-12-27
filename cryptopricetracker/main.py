import requests
import tkinter as tk 
from datetime import datetime


def tracklrc():
    url = "https://min-api.cryptocompare.com/data/price?fsym=LRC&tsyms=USD"
    response = requests.get(url).json()
    price = response["USD"]
    
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price) + "$")
    labelTime.config(text = "updated at:  " + time )

    canvas.after(1000, tracklrc)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Loopring  Tracker")

labelPrice = tk.Label(canvas, text = "Loopring price:")
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas)
labelTime.pack(pady=20)


tracklrc()
canvas.mainloop()