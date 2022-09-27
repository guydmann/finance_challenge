import pandas as pd


def calculate_data():
    # get the data from the test file and then calculate the 2 portfolios each day
    # then calculate the daily returns
    # use the daily returns to calculate the correlation
    # also get the monthly return when calculating the daily returns
    pd.set_option('mode.chained_assignment', None)
    close_prices = pd.read_csv("MANG_adj_close.csv")
    initial_price = close_prices.iloc[0]
    initial_price["total"] = initial_price[['AMZN', 'GOOG', 'META', 'NFLX']].sum()

    weights = {
        "AMZN": 0.25/(initial_price['AMZN']/initial_price["total"]),
        "GOOG": 0.25/(initial_price['GOOG']/initial_price["total"]),
        "META": 0.25/(initial_price['META']/initial_price["total"]),
        "NFLX": 0.25/(initial_price['NFLX']/initial_price["total"])
    }
    close_prices["ONE_EACH"] = close_prices['AMZN'] + close_prices['GOOG'] + close_prices['META'] + close_prices['NFLX']
    close_prices["EQUAL_START_VALUE"] = (close_prices['AMZN'] * weights['AMZN']) + \
                                        (close_prices['GOOG'] * weights['GOOG']) + \
                                        (close_prices['META'] * weights['META']) + \
                                        (close_prices['NFLX'] * weights['NFLX'])
    close_prices["Portfolio A Daily Returns"] = close_prices["ONE_EACH"].pct_change(1)
    one_each_monthly_return = close_prices["ONE_EACH"].pct_change(20)
    close_prices["Portfolio B Daily Returns"] = close_prices["EQUAL_START_VALUE"].pct_change(1)
    equal_start_value_monthly_return = close_prices["EQUAL_START_VALUE"].pct_change(20)
    print(close_prices[['Date', "Portfolio A Daily Returns", "Portfolio B Daily Returns"]])
    print("Portfolio A Monthly Return for July: {mn_return}".format(mn_return=one_each_monthly_return[20]))
    print("Portfolio B Monthly Return for July: {mn_return}".format(mn_return=equal_start_value_monthly_return[20]))

    correlation = close_prices['Portfolio A Daily Returns'].corr(close_prices['Portfolio B Daily Returns'])
    print("correlation: {correlation}".format(correlation=correlation))


if __name__ == "__main__":
    calculate_data()

