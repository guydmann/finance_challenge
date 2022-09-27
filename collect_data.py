import yfinance as yf


def collect_data():
    data = yf.download("META AMZN NFLX GOOG", start="2017-06-30", end="2017-07-31")
    print(data["Adj Close"])
    data["Adj Close"].to_csv("MANG_adj_close.csv")


if __name__ == "__main__":
    collect_data()









