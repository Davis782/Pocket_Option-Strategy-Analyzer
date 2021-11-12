
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf


import os, ssl
#
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
#         getattr(ssl, '_create_unverified_context', None)):
ssl._create_default_https_context = ssl._create_unverified_context
#
# #  http://localhost:5997

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")


#===========================Update=================================================
# Create a Google Authentication connection object
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


