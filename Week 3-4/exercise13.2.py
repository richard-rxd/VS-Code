import csv

with open("/Users/richardwittich/VS Code/stocks.csv", "r") as stock, open("/Users/richardwittich/VS Code/data.csv", "w") as data:
    reader = csv.reader(stock)
    writer = csv.writer(data)
    writer.writerow(["Company Name", "P/E-Ratio", "P/B Value"])
    next(reader, None)
    for row in reader:
        company_name, price, earnings_per_share, book_value = row
        price = float(price)
        earnings_per_share = float(earnings_per_share)
        book_value = float(book_value)
        peratio = price/earnings_per_share
        ptobvalue = price/book_value
        writer.writerow([company_name, peratio, ptobvalue])

print("Ratios calculation and saving to CSV completed.")
