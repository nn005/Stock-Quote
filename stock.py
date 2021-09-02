import requests
from tkinter import *


# Configuration and creation of the gui window
root = Tk()
root.geometry('600x400')
root.resizable(0,0)
root.title("Python Stock Quote")
root.configure(bg='#F9FCFF')

# Label of the title of the gui
title_label = Label(root,text = 'Python Stock Quote Search', font ='arial 20 bold', bg='#F9FCFF')
title_label.pack( anchor="center")

# SymbolGui is a StringVar() variable to receive the stock symbol from the entry widget
SymbolGui = StringVar()

# Label to direct where to input the desired symbol
entry_label = Label(root, text = 'Input Stock Symbol Below', font = 'arial 15 bold', bg='#F9FCFF')
entry_label.pack( anchor="center", pady=30)

# Entry widget which receives the input from the user and passes it to the SymbolGui variable
SymbolGui_enter = Entry(root, width = 20, textvariable = SymbolGui, justify = 'center')
SymbolGui_enter.pack(anchor="center")

# Search function extracts stock symbol from the SymbolGui variable and calls on the api and displays the most recent available
# price of the inputted stock and the date of that data.
def Search():

    # Uses the get method and stores the value of the stock symbol entered in the entry widget as a string in the symbol variable
    Symbol = str(SymbolGui.get())

    # Calls the alphaadvantage api and converts the recieved data into json
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+Symbol+'&apikey=DYJ9J1YRV5NZAQJZ'
    r = requests.get(url)
    data = r.json()

    # Extracting the date when the data was last refreshed in the dictionary and storing it in the y variable
    y =  data.get('Meta Data',{}).get('3. Last Refreshed')
    print(y)

    # Inputs the y variable to extract the latest price data from the dictionary
    x = data.get('Time Series (Daily)',{}).get(y,{}).get('4. close')
    print(x)

    # Label is created which displays the x and y variables
    price_label = Label(root, text = ('Price of '+Symbol.upper()+' as of '+str(y)+': ' + str(x)), font = 'arial 15 bold')
    price_label.pack(anchor = "center", pady=3)

# Search button calls the search function when clicked
search_button = Button(root,text = 'Get Price', font = 'arial 15 bold', padx = 2, command = Search)
search_button.pack(anchor="center", pady=3)

