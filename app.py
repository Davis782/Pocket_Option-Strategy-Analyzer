import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
#import base64 # So you can download a csv file
#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly
#import psycopg2
#import requests
#import tweepy   #   https://docs.tweepy.org/en/stable/auth_tutorial.html
#import config

# Your imports goes below

markets = ["Crypto","Currency_Pairs","Stocks","Commodities"]
strategies = ["RSI", "TSI", "SO", "CONSOLODATION", "BREAKOUT", "SCHAFF", "GOLDEN_CROSS"]

st.sidebar.title("Select Your Trading Market")

def main():
    st.title("Pocket Option Trade Analyzer")
    st.markdown(""" This app is meant to analyze the markets with strategies that can be plotted and ranked on compliance.  
    * **[PocketOption](https://pocketoption.com/en/cabinet/demo-high-low/?)
    * **A account with your broker is required if you are making trades
    No advise for trading is done on this site, but for educational and coding example purposes.""")

#    st.sidebar.text_input("Select Your Trading Market")
#    st.sidebar.selectbox("Select Your Trading Market", list(markets))
#    st.sidebar.multiselect("Select Your Trading Market", list(markets))





    st.sidebar.header("Select Your Trading Strategy")
    #    st.sidebar.text_input("Select Your Strategy")
    st.sidebar.multiselect("Select Your Trading Strategy", list(strategies), default=list(strategies))


#
#
# # Your code goes below
#
#

Options = st.sidebar.selectbox("Select Your Trading Market", list(markets))


if __name__ == "__main__":
    main()


    st.header("Display of Market Data in Table form")

    st.header(Options)
    #
    # if Options == "Crypto":
    #     st.subheader("this is the chart dashboard logic")
    #
if Options == "Currency_Pairs":
    st.subheader("Currency_Pairs logic")

#=============================The Beginning=========================================================================================

    @st.cache
    def load_data():
        INCREMENTS=[{
                '1m': 1,
                '2m': 2,
                '5m': 5,
                '15m': 15,
                '30m': 3,
                '60m': 60,
                '90m': 90,
                '1h': 1,
                '1d': 1,
                #    '5d ': 5,
                #    '1wk': 1,
                #    '1mo': 1,
                #    '3mo': 3
                }]

        CURRENCY = ["GBP", "JPY", "CAD", "USD", "EUR", "CHF", "NZD"]

        start_date = datetime(2021, 7, 27)
        end_date = datetime(2021, 8, 3)

        N = 1000000000

        list_of_pairs = [(CURRENCY[p1] + "" + CURRENCY[p2] + "=X") for p1 in range(len(CURRENCY)) for p2 in
                         range(p1 + 1, len(CURRENCY))]

        list_of_pairs = pd.DataFrame(list_of_pairs)
        pairs = list_of_pairs.replace('"', '')
        pairs = pd.DataFrame(pairs)
        pairs = pairs.rename(columns={0: "Names1"})
        pairs = pairs["Names1"]

        keys = pd.DataFrame.from_dict(INCREMENTS).keys()

        pair_list = []
        for p1 in pairs:
            for p2 in keys:
                p = f"{p1}_{p2}"
                data2 = yf.download(p1, start=start_date, end=end_date, interval=p2)

                # # Tickers list
                # # We can add and delete any ticker from the list to get desired ticker live data
                # ticker_list = ["DJIA", "DOW", "LB", "EXPE", "PXD", "MCHP", "CRM", "JEC", "NRG", "HFC", "NOW"]
                # today = date.today()

                df2 = pd.DataFrame(data2, columns=['DateTime', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
                df2['DateTime'] = pd.to_datetime(df2['DateTime'], unit='m')
                filename = ("data/{}_{}.csv").format(p1, p2)
                df2.to_csv(filename)
                #       plot2_("{}{}").format(p1,p2) = mpf.plot(data2,type='candle',mav=(20, 50, 200),volume=True,show_nontrading=True, warn_too_much_data=N)

                if p not in pairs:
                    pair_list.append(p)

        pair_list = pd.DataFrame(pair_list)
        return (pair_list)

        pair_list = load_data()
    #st.dataframe(pair_list)
    st.dataframe()

#====================================The End================================================================================

    # if Options == "Stocks":
    #     st.subheader("this is the chart dashboard logic")
    #
    # if Options == "Commodities":
    #     st.subheader("this is the chart dashboard logic")
    #
    # if Options == "Chart":
    #     pass
