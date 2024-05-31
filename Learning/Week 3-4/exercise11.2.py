stocks = {"info": [600, 630, 620], "ril": [1430,1490,1567], "mtl": [234,180,160]}

def printlist():
    for i in stocks:
        avg = 1
        print(f"{i} ==> {stocks[i]} ==> avg: {avg}")

def add():
    ticker = input("Ticker of stock: ")
    price = int(input("Price of stock: "))
    if ticker in stocks:
        stocks[ticker].append(price)
    else:
        stocks[ticker] = price

printlist()
add()
printlist()

