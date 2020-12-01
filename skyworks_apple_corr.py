import yfinance as yf
import pandas  as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
stocks = ["AAPL","SWKS"]
start = datetime.datetime(2019,1,1)
end = datetime.datetime(2019,7,17)
#years = [2012,2015,2016,2017,2018,2019]
corr_over_years =  []
for year in range(2012,2020):
    df_ac = yf.download(stocks, start=datetime.datetime(year,1,1))["Adj Close"]
    corr_over_years.append(df_ac.corr()["AAPL"]["SWKS"])

print(corr_over_years)
plt.plot(range(2012,2020),corr_over_years)
