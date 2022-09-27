import pandas as pd


def calculate_data():
    #collect the data from yfinance and and write it to a text file
    close_prices = pd.read_csv("MANG_adj_close.csv")
    print(close_prices)


if __name__ == "__main__":
    calculate_data()

