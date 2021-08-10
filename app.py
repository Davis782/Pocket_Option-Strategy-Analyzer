import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import base64 # So you can download a csv file
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import psycopg2
import requests
import tweepy   #   https://docs.tweepy.org/en/stable/auth_tutorial.html
#import config

# Your imports goes below

markets = ["Crypto","Currency_Pairs","Stocks","Commodities"]
strategies = ["RSI", "TSI", "SO", "CONSOLODATION", "BREAKOUT", "SCHAFF", "GOLDEN_CROSS"]

def main():
    st.title("Pocket Option Trade Analyzer")
    st.markdown("DESCRIPTION")
    st.sidebar.header("Select Your Trading Market")
#    st.sidebar.text_input("Select Your Trading Market")
#    st.sidebar.selectbox("Select Your Trading Market", list(markets))
    st.sidebar.multiselect("Select Your Trading Market", list(markets), default= list(markets))



    st.sidebar.header("Select Your Trading Strategy")
    #    st.sidebar.text_input("Select Your Strategy")
    #    st.sidebar.selectbox("Select Your Trading Strategy", list(strategies))
    st.sidebar.multiselect("Select Your Trading Strategy", list(strategies), default=list(strategies))


# Your code goes below




if __name__ == "__main__":
    main()