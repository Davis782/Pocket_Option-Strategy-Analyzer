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
    st.subheader("twitter dashboard logic")

#=============================The Beginning=========================================================================================

#====================================The End================================================================================

    # if Options == "Stocks":
    #     st.subheader("this is the chart dashboard logic")
    #
    # if Options == "Commodities":
    #     st.subheader("this is the chart dashboard logic")
    #
    # if Options == "Chart":
    #     pass
