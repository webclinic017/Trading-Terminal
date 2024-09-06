#Full stack streamlit import
import streamlit as st

#Page config
st.set_page_config(page_title='Trading Terminal', page_icon="📈", layout="wide") 
from  project_about import about


#Migrate to submodules for readability

import yfinance as yf
import scipy.optimize as sco
import matplotlib.dates as mpl_dates
from scipy.stats import zscore
from factor_analyzer import FactorAnalyzer, calculate_bartlett_sphericity, calculate_kmo
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns
from pypfopt import risk_models
from pypfopt import expected_returns
from pandas.plotting import register_matplotlib_converters
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from scipy.stats import ttest_ind
from scipy.stats import norm
from ta import add_all_ta_features
from alpaca_trade_api.rest import REST, TimeFrame
import backtrader as bt
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from yahoo_earnings_calendar import YahooEarningsCalendar
from pandas_datareader._utils import RemoteDataError
from matplotlib import dates as mdates
from socket import gaierror
from mplfinance.original_flavor import candlestick_ohlc
import nltk 
nltk.download('vader_lexicon')
from bs4 import BeautifulSoup
import os
from math import sqrt
import quandl as q
from pylab import rcParams
import pylab as pl
import calendar
import yfinance as yf
import pandas as pd
import seaborn as sns
from scipy.stats import gmean
import numpy as np
import plotly.figure_factory as ff
import tickers as ti
import string
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from IPython.display import clear_output
import requests
from pandas_datareader import data as pdr
import sys
from websocket import create_connection
import os
import ta_functions as ta
import ta as taf
import tickers as ti
from email.message import EmailMessage
import datetime as dt
import time
import statsmodels.api as sm
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from sklearn.decomposition import PCA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.stats import norm
import warnings
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import plotly.express as px
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.pylab import rcParams
from fastai.tabular.all import add_datepart
import tensorflow as tf
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
import numpy as np
from mplfinance.original_flavor import candlestick_ohlc
from bs4 import BeautifulSoup
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from pandas_datareader import data as pdr
import yfinance as yf
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from keras import Sequential, layers
from keras._tf_keras.keras.preprocessing import sequence
from keras.src.layers import Embedding, LSTM, Dense, Dropout
from keras.src.metrics.metrics_utils import confusion_matrix
from keras.src.utils import to_categorical
import networkx as nx
from sklearn.covariance import GraphicalLassoCV
warnings.filterwarnings("ignore")
from autoscraper import AutoScraper
from lxml import html
import requests
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import math
import mplfinance as mpl
import subprocess
import smtplib
import alpaca_trade_api as alpaca

#Env variables
from dotenv import load_dotenv
load_dotenv()


#secrets the application
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
API_FMPCLOUD = os.environ.get("API_FMPCLOUD")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
BASE_URL = os.environ.get("BASE_URL")
API_KEY_ALPACA = os.environ.get("API_KEY_ALPACA")
SECRET_KEY_ALPACA =os.environ.get("SECRET_KEY_ALPACA")

KRAKEN_CONFIG =  "PASS"
ALPACA_CONFIG = alpaca.REST(API_KEY_ALPACA, SECRET_KEY_ALPACA, base_url= BASE_URL, api_version = 'v2')


#Al Trading recs
from lumibot.brokers import Alpaca
from lumibot.entities import Asset, Order
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from lumibot.backtesting import YahooDataBacktesting #TODO - Move to strategies
from lumibot.backtesting import CcxtBacktesting
from lumibot.example_strategies.crypto_important_functions import ImportantFunctions
from lumibot.entities import TradingFee



#Main tools for stock finding
from langchain_core.tools import tool
from StockFinder.analyze_idb_rs_rating import analyze_idb_rs_rating, tool_analyze_idb_rs_rating
from StockFinder.correlated_stocks import correlated_stocks, tool_correlated_stocks
from StockFinder.finviz_growth_screener import tool_growth_screener
from StockFinder.fundamental_screener import tool_fundamental_screener
from StockFinder.rsi_tickers import tool_rsi_tickers,normal_rsi_tickers
from StockFinder.green_line_valuation import tool_green_line_valuation
from StockFinder.Minervini_screener import tool_miniverini_screener, minervini_screener
from StockFinder.pricing_email_alerter import tool_price_alerter, normal_price_alerter
from StockFinder.trading_view_signals import tool_trading_view_signals, norm_trading_view_signals
from StockFinder.Twitter_Screener import tool_twitter_screener
from StockFinder.Yahoo_recommendations import tool_yahoo_recommendation_pipeline

#Main tools for stock predictions
from StockPredictions.time_series_arima import tool_arima_time_series, arima_time_series
from StockPredictions.stock_recommendations import tool_stock_recommendations_using_moving_averages, normal_stock_recommendations_using_moving_averages
from StockPredictions.stock_regression import tool_stock_regression, normal_stock_regression
from StockPredictions.stock_probabilty import tool_stock_probability, norm_stock_probability
from StockPredictions.stock_pca_analysis import tool_pca_analysis,norm_pca_analysis
from StockPredictions.Technical_indicators_clustering import tool_technical_indicators_clustering, norm_technical_indicators_clustering
from StockPredictions.lstm_predictions import tool_lstm_predictions, normal_lstm_predictions
from StockPredictions.etf_graphical_lasso import tool_etf_graphical_lasso,normal_etf_graphical_lasso
from StockPredictions.kmeans_clustering import tool_kmeans_clustering, normal_kmeans_clustering

#Main tools for stock data
from StockData.dividend_history import tool_dividend_history, norm_dividend_history
from StockData.Fibonacci_retracement import tool_fibonacci_retracement, norm_fibonacci_retracement
from StockData.finviz_scraper import tool_finviz_scraper
from StockData.finviz_insider_trading_scraper import tool_finviz_insider_scraper
from StockData.finviz_stock_data_scraper import tool_finviz_scraper_stock_data
from StockData.get_dividend_calendar import tool_get_dividend_calendar, norm_get_dividends
from StockData.greenline_test import tool_greenline_test, norm_greenline_test
from StockData.high_dividend_yield import tool_high_dividend_yield
from StockData.main_indicators import tool_main_indicators, norm_main_indicators
from StockData.pivots_calculator import tool_pivots_calculator, norm_pivots_calculator
from StockData.email_top_movers import tool_scrape_top_winners
from StockData.stock_vwap import tool_stock_vwap, norm_stock_vwap
from StockData.stock_sms import tool_stock_sms, norm_stock_sms
from StockData.stock_earnings import tool_stock_earnings, norm_stock_earnings
from StockData.trading_view_intraday import tool_trading_view_intraday
from StockData.trading_view_recommendations import tool_trading_view_recommendations, norm_trading_view_recommendations

#Main tools for stock Analysis
from StockAnalysis.backtest_all_indicators import tool_backtest_all_indicators, norm_backtest_all_indicators
from StockAnalysis.capm_analysis import tool_capm_analysis, norm_capm_analysis

tools = [tool_analyze_idb_rs_rating,tool_correlated_stocks, tool_growth_screener, 
         tool_fundamental_screener, tool_rsi_tickers,tool_green_line_valuation, 
         tool_miniverini_screener, tool_price_alerter, tool_trading_view_signals,
         tool_twitter_screener, tool_yahoo_recommendation_pipeline, tool_arima_time_series,
         tool_stock_recommendations_using_moving_averages,tool_stock_regression,
         tool_stock_probability, tool_pca_analysis, tool_technical_indicators_clustering,
         tool_lstm_predictions, tool_etf_graphical_lasso,tool_kmeans_clustering,
         tool_dividend_history, tool_fibonacci_retracement, tool_finviz_scraper, tool_finviz_insider_scraper,
         tool_finviz_scraper_stock_data, tool_get_dividend_calendar, tool_greenline_test,
         tool_high_dividend_yield,tool_pivots_calculator,tool_main_indicators,
         tool_scrape_top_winners, tool_stock_vwap, tool_stock_sms,
         tool_stock_earnings, tool_trading_view_intraday,tool_trading_view_recommendations,
         tool_backtest_all_indicators, tool_capm_analysis]



# Multimodial agent bot configuration
from openai import OpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
import getpass
from langchain_openai import ChatOpenAI
# Set your API key here
api_key = os.environ.get("LANGSMITH_KEY")
if 'conversation' not in st.session_state:
    st.session_state.conversation = ""



##Terminal config
import time 

def main():
    #Main app
    st.title("📈 Frankline and Co. LP Trading Terminal Beta")
    st.sidebar.info('Welcome to my Algorithmic Trading App. Choose your options below. This application is backed over by 100 mathematically powered algorithms handpicked from the internet and modified for different Trading roles')
    # Create a two-column layout
    left_column, right_column = st.columns([2, 2])

    with left_column:
        option = st.sidebar.radio("Make a choice",('About',"Algorithmic Trading",'Find stocks', 'Portfolio Strategies','Stock Data', 'Stock Analysis','Technical Indicators', 'Stock Predictions'))
        if option =='About':
            about()
        if option == 'Find stocks':
            options = st.selectbox("Choose a stock finding method:", ["IDB_RS_Rating", "Correlated Stocks", "Finviz_growth_screener", "Fundamental_screener", "RSI_Stock_tickers", "Green_line Valuations", "Minervini_screener", "Pricing Alert Email", "Trading View Signals", "Twitter Screener", "Yahoo Recommendations"])
            if options == "IDB_RS_Rating":
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button('Start Analysis'):
                    analyze_idb_rs_rating(start_date, end_date)

            if options == "Correlated Stocks":
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")                
                sectors = {
                    "Technology": ['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'INTC', 'CSCO', 'ADBE', 'AVGO', 'PYPL'],
                    "Health Care": ['JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'TMO', 'MDT', 'DHR', 'AMGN', 'LLY'],
                    "Financials": ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'AXP', 'BLK', 'SPGI', 'USB'],
                    "Consumer Discretionary": ['AMZN', 'TSLA', 'HD', 'MCD', 'DIS', 'NKE', 'SBUX', 'BKNG', 'LOW', 'CMG'],
                    "Communication Services": ['GOOGL', 'META', 'DIS', 'CMCSA', 'NFLX', 'T', 'CHTR', 'DISCA', 'FOXA', 'VZ'],
                    "Industrials": ['BA', 'HON', 'UNP', 'UPS', 'CAT', 'LMT', 'MMM', 'GD', 'GE', 'CSX'],
                    "Consumer Staples": ['PG', 'KO', 'PEP', 'WMT', 'COST', 'CL', 'MO', 'EL', 'KHC', 'MDLZ'],
                    "Utilities": ['NEE', 'DUK', 'SO', 'D', 'EXC', 'AEP', 'SRE', 'PEG', 'XEL', 'ED'],
                    "Real Estate": ['AMT', 'PLD', 'CCI', 'EQIX', 'WY', 'PSA', 'DLR', 'BXP', 'O', 'SBAC'],
                    "Materials": ['LIN', 'APD', 'SHW', 'DD', 'ECL', 'DOW', 'NEM', 'PPG', 'VMC', 'FCX']
                }

                selected_sector = st.selectbox('Select Sector', list(sectors.keys()))
                if st.button("Start Analysis"):
                    correlated_stocks(start_date, end_date, selected_sector)
            
            if options == "Finviz_growth_screener":
                if st.button("Scan"):
                    # Execute the screener and store the result
                    tool_input = {}  
                    df = tool_growth_screener(tool_input)
                    st.write('\nGrowth Stocks Screener:')
                    st.write(df)
                    # Extract and print list of tickers
                    tickers = df.index
                    st.write('\nList of Tickers:')
                    st.write(tickers)
                
            if options == "Fundamental_screener":
                st.success("This portion allows you to sp500 for base overview")
                if st.button("Scan"):
                    fund_tool_input = {} 
                    tool_fundamental_screener(fund_tool_input) 

            if options == "RSI_Stock_tickers":
                st.success("This program allows you to view which tickers are overbrought and which ones are over sold")
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                # Get dates for the past year

                if st.button("Check"):
                    normal_rsi_tickers(start_date, end_date)
                   
                    
            if options=="Green_line Valuations":
                st.success("This programme analyzes all tickers to help identify the Green Value ones")
                if st.button("Scan"):
                    # Execute the screener and store the result
                    green_line_tool_input = {}  # Replace with actual input required by the tool
                    tool_fundamental_screener(green_line_tool_input)

            if options == "Minervini_screener":
                # Setting up variables
                st.success("This program allows you to view which tickers are overbrought and which ones are over sold")
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                # Get dates for the past year

                if st.button("Check"):
                    minervini_screener(start_date, end_date)

            if options == "Pricing Alert Email":
                # Email credentials from environment variables
                st.success("This segment allows you to track the pricing of a certain stock to your email if it hits your target price")
                stock = st.text_input("Enter the ticker you want to monitor")
                if stock:
                    message = (f"Ticker captured : {stock}")
                    st.success(message)
                # Stock and target price settings
                target_price = st.number_input("Enter the target price")
                if target_price:
                    message_two = (f"Target price captured at : {target_price}")
                    st.success(message_two)
                email_address = st.text_input("Enter your Email address")
                if email_address:
                    message_three = (f"Email address captured is {email_address}")
                    st.success(message_three)

                if st.button("Check"):
                    normal_price_alerter(start_date, end_date, stock, email_address, target_price)

            if options=="Trading View Signals":
                st.success("This program allows you to view the Trading view signals of a particular ticker")
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Simulate signals"):
                    norm_trading_view_signals(start_date, end_date)

            if options == "Twitter Screener":
                st.write("This segment allows you to screen for stocks based on Twitter sentiment")
                if st.button("Analyze"):
                    twitter_tool = {}  # Replace with actual input required by the tool
                    tool_twitter_screener(twitter_tool)

            if options=="Yahoo Recommendations":

                st.success("This segment returns the stocks recommended by Yahoo Finance")
                if st.button("Check Recommendations"):
                    yahoo_tool = {}  # Replace with actual input required by the tool
                    tool_yahoo_recommendation_pipeline(yahoo_tool)
        
                    
        elif option == 'Stock Predictions':

            pred_option = st.selectbox('Make a choice', ['sp500 PCA Analysis','Arima_Time_Series','Stock Probability Analysis','Stock regression Analysis',
                                                        'Stock price predictions','Technical Indicators Clustering', 'LSTM Predictions', 'ETF Graphical Lasso', 'Kmeans Clustering', 
                                                        'ETF Graphical Lasso', 'Kmeans Clustering'])
            
            if pred_option == "Arima_Time_Series":
                st.success("This segment allows you to Backtest using Arima")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                   arima_time_series(start_date, end_date, ticker)

            if pred_option == "Stock price predictions":
                st.success("This segment allows you to predict the pricing using Linear Regression")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                    normal_stock_recommendations_using_moving_averages(ticker, start_date, end_date)

            if pred_option == "Stock regression Analysis":

                st.success("This segment allows you to predict the next day price of a stock")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                    normal_stock_regression(start_date, end_date, ticker)

            if pred_option == "Stock Probability Analysis":

                st.success("This segment allows you to predict the movement of a stock ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                    norm_stock_probability(start_date, end_date, ticker)
                    
            if pred_option == "sp500 PCA Analysis":
                st.write("This segment analyzes the s&p 500 stocks and identifies those with high/low PCA weights")
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                if st.button("Check"):
                    norm_pca_analysis(start_date, end_date, ticker)
                               
            if pred_option == "Technical Indicators Clustering":
                #Fix the segmentation of all tickers on the graph
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                if st.button("Check"):
                    norm_technical_indicators_clustering(start_date, end_date, ticker)

            if pred_option == "LSTM Predictions":

                st.success("This segment allows you to predict the movement of a stock ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                # Prompt user to enter a stock ticker
                    normal_lstm_predictions(start_date, end_date, ticker)

            if pred_option == "ETF Graphical Lasso":
                st.success("This segment allows you to predict the relations of various ETFS")
                number_of_years = st.text_input("How many years do you want to investigate the ETF correlations(min 10)")
                if number_of_years:
                    st.success(f"The number of years captured : {number_of_years}")
                col1, col2 = st.columns([2, 2])
                with col1:
                    end_date = st.date_input("End date:")
            
                if st.button("Check"):
                    num_years = int(number_of_years)
                    start_date = dt.datetime.now() - dt.timedelta(days=num_years * 365.25)
                    end_date = dt.datetime.now()
                    normal_etf_graphical_lasso(start_date, end_date,number_of_years)
                    
            if pred_option == "Kmeans Clustering":
                
                st.success("This segment allows you to predict the price of a stock ticker using Kmeans clustering")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                    normal_kmeans_clustering(start_date, end_date)

        elif option =='Stock Data':
            pred_option_data = st.selectbox("Choose a Data finding method:", ["High Dividend yield","Dividend History", "Fibonacci Retracement", 
                                                                            "Finviz Home scraper", "Finviz Insider Trading scraper", "Finviz stock scraper", 
                                                                            "Get Dividend calendar", "Green Line Test", "Main Indicators", "Pivots Calculator", 
                                                                            "Email Top Movers", "Stock VWAP", "Data SMS stock", "Stock Earnings", "Trading view Intraday", 
                                                                            "Trading view Recommendations", "Yahoo Finance Intraday Data"])
        
            if pred_option_data == "Dividend History": 
                st.success("This segment allows you to get the dividends of a particular ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                    norm_dividend_history(start_date, end_date, ticker)
            
            if pred_option_data == "Fibonacci Retracement":
                st.success("This segment allows you to do Fibonnacci retracement max price of a particular ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Simulate"):
                    norm_fibonacci_retracement(ticker, start_date, end_date)


            if pred_option_data == "Finviz Home scraper":
                st.success("This segment allows you to find gainers/losers today and relevant news from Finviz")
                if st.button("Confirm"):
                    finviz_data_tool = {}  # Replace with actual input required by the tool
                    tool_finviz_scraper(finviz_data_tool)
                    

            if pred_option_data == "Finviz Insider Trading scraper":
                st.success("This segment allows you to check the latest insider trades of the market and relevant parties")
                # Set display options for pandas
                if st.button("Check"):
                    insider_trading_tool = {}  # Replace with actual input required by the tool
                    tool_finviz_insider_scraper(insider_trading_tool)

            if pred_option_data == "Finviz stock scraper":

                st.success("This segment allows to analyze overview a ticker from finviz")
                stock = st.text_input("Please type the stock ticker")
                if stock:
                    st.success(f"Stock ticker captured : {stock}")
                if st.button("check"):
                    tool_finviz_scraper_stock_data(stock)
            
            if pred_option_data == "Get Dividend calendar":
                st.success("This segment allows you to observe the Dividend companies of some companies")     

                month = st.date_input("Enter the Month to test")
                if month:
                    # Convert the selected date to a string in the format "%Y-%m-%d"
                    month_str = month.strftime("%Y-%m-%d")
                    # Split the string into year and month
                    year, month, _ = month_str.split('-')
                    st.success(f"Month captured: Year - {year}, Month - {month}")

                if st.button("Check"):
                    norm_get_dividends(year, month)
                
            if pred_option_data == "Green Line Test":

                st.success("This segment allows you to see if a ticker hit a greenline")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                
                min_date = datetime(1980, 1, 1)

                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                # Button to trigger the simulation
                if st.button("Simulate"):
                    st.success("Simulation started...")
                    norm_greenline_test(start_date , end_date , ticker)
                 


            if pred_option_data == "High Dividend yield":
                st.success("This program allows you to simulate the Dividends given by a company")
                if st.button("Check"):
                    high_dividend_yield_tooler = {}  # Replace with actual input required by the tool
                    tool_high_dividend_yield(high_dividend_yield_tooler)



            if pred_option_data == "Main Indicators":
                st.success("This segment allows you to see if a ticker hit a greenline")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                
                min_date = datetime(1980, 1, 1)

                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                # Button to trigger the simulation
                if st.button("Simulate"):
                    # Convert dates to strings
                    start_date_str = start_date.strftime('%Y-%m-%d')
                    end_date_str = end_date.strftime('%Y-%m-%d')
                    norm_main_indicators(ticker, start_date_str, end_date_str)

            if pred_option_data == "Pivots Calculator":
                st.write("This part calculates the pivot shifts within one day")
                # Prompt user for stock ticker input
                stock = st.text_input('Enter a ticker: ')
                interval = st.text_input('Enter an Interval : default for 1d')
                
                if st.button("Check") :
                    # Fetch historical data for the specified stock using yfinance
                    norm_pivots_calculator(stock, interval)
                                
            if pred_option_data == "Email Top Movers":

                st.success("This segment allows you to get updates on Top stock movers")
                email_address = st.text_input("Enter your Email address")
                if email_address:
                    message_three = (f"Email address captured is {email_address}")
                    st.success(message_three)

                if st.button("Check"):
                    # Function to scrape top winner stocks from Yahoo Finance
                    email_top_movers_tool = {}  # Replace with actual input required by the tool
                    tool_scrape_top_winners(email_top_movers_tool)

            if pred_option_data == "Stock VWAP":
                st.success("This segment allows us to analyze the Volume Weighted Average Price of a ticker")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                    norm_stock_vwap(ticker, start_date, end_date)

            if pred_option_data == "Data SMS stock":
                st.success("This segment allows us to get the stock data SMS")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                email_address = st.text_input("Enter your Email address")
                if email_address:
                    message_three = (f"Email address captured is {email_address}")
                    st.success(message_three)

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                   norm_stock_sms(ticker, start_date, end_date, email_address)


            if pred_option_data == "Stock Earnings":

                #TODO - fix the meta error from earnings df directly
                st.success("This segment allows us to get the stock data SMS")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                email_address = st.text_input("Enter your Email address")
                if email_address:
                    message_three = (f"Email address captured is {email_address}")
                    st.success(message_three)

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                    norm_stock_earnings(start_date, end_date)


            if pred_option_data == "Trading view Intraday":
                if st.button("Check"):
                    trading_intraday_test = {}  # Replace with actual input required by the tool
                    tool_trading_view_intraday(trading_intraday_test)
                    
            if pred_option_data == "Trading view Recommendations":
                
                st.success("This segment allows us to get recommendations fro Trading View")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                    norm_trading_view_recommendations(ticker, start_date, end_date)




                    
        elif option =='Stock Analysis':
            pred_option_analysis = st.selectbox('Make a choice', ['Backtest All Indicators',
                                                        'CAPM Analysis',
                                                        'Earnings Sentiment Analysis',
                                                        'Intrinsic Value analysis',
                                                        'Kelly Criterion',
                                                        'MA Backtesting',
                                                        'Ols Regression',
                                                        'Perfomance Risk Analysis',
                                                        'Risk/Returns Analysis',
                                                        'Seasonal Stock Analysis',
                                                        'SMA Histogram',
                                                        'SP500 COT Sentiment Analysis',
                                                        'SP500 Valuation',
                                                        'Stock Pivot Resistance',
                                                        'Stock Profit/Loss Analysis',
                                                        'Stock Return Statistical Analysis',
                                                        'VAR Analysis',
                                                        'Stock Returns'])

            if pred_option_analysis == "Backtest All Indicators":
                st.success("This segment allows us to Backtest Most Technical Indicators of a ticker")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Backtest"):
                    norm_backtest_all_indicators(ticker, start_date, end_date)

            if pred_option_analysis == "CAPM Analysis": 
                #TODO fix the CAPM analysis quagmire of returning empty datasets from the NASDAQ index
                st.success("This segment allows you to do CAPM Analysis")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):

                # Fetches stock data for a given ticker.
                    norm_capm_analysis(ticker, start_date, end_date)



            if pred_option_analysis == "Earnings Sentiment Analysis":
                # Retrieves earnings call transcript from API
                # TODO identify the error with the API with key error 0
                def get_earnings_call_transcript(api_key, company, quarter, year):
                    url = f'https://financialmodelingprep.com/api/v3/earning_call_transcript/{company}?quarter={quarter}&year={year}&apikey={api_key}'
                    response = requests.get(url)
                    return response.json()[0]['content']

                # Performs sentiment analysis on the transcript.
                def analyze_sentiment(transcript):
                    sentiment_call = TextBlob(transcript)
                    return sentiment_call

                # Counts the number of positive, negative, and neutral sentences.
                def count_sentiments(sentiment_call):
                    positive, negative, neutral = 0, 0, 0
                    all_sentences = []

                    for sentence in sentiment_call.sentences:
                        polarity = sentence.sentiment.polarity
                        if polarity < 0:
                            negative += 1
                        elif polarity > 0:
                            positive += 1
                        else:
                            neutral += 1
                        all_sentences.append(polarity)

                    return positive, negative, neutral, np.array(all_sentences)

                st.success("This segment allows us to get The sentiments of a company's earnings")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                    api_key = API_FMPCLOUD
                    company = ticker

                    # Get transcript and perform sentiment analysis
                    transcript = get_earnings_call_transcript(api_key, company, 3, 2020)
                    sentiment_call = analyze_sentiment(transcript)

                    # Count sentiments and calculate mean polarity
                    positive, negative, neutral, all_sentences = count_sentiments(sentiment_call)
                    mean_polarity = all_sentences.mean()

                    # Print results
                    st.write(f"Earnings Call Transcript for {company}:\n{transcript}\n")
                    st.write(f"Overall Sentiment: {sentiment_call.sentiment}")
                    st.write(f"Positive Sentences: {positive}, Negative Sentences: {negative}, Neutral Sentences: {neutral}")
                    st.write(f"Average Sentence Polarity: {mean_polarity}")

                    # Print very positive sentences
                    print("\nHighly Positive Sentences:")
                    for sentence in sentiment_call.sentences:
                        if sentence.sentiment.polarity > 0.8:
                            st.write(sentence)

            if pred_option_analysis == "Estimating Returns":

                # Fetches stock data and calculates annual returns.
                def get_stock_returns(ticker, start_date, end_date):
                    stock_data = yf.download(ticker,start_date, end_date)
                    stock_data = stock_data.reset_index()
                    open_prices = stock_data['Open'].tolist()
                    open_prices = open_prices[::253]  # Annual data, assuming 253 trading days per year
                    df_returns = pd.DataFrame({'Open': open_prices})
                    df_returns['Return'] = df_returns['Open'].pct_change()
                    return df_returns.dropna()

                # Plots the normal distribution of returns.
                def plot_return_distribution(returns, ticker):
                    # Calculate mean and standard deviation
                    mean, std = np.mean(returns), np.std(returns)
                    
                    # Create x values
                    x = np.linspace(min(returns), max(returns), 100)
                    
                    # Calculate probability density function values
                    y = norm.pdf(x, mean, std)
                    
                    # Create interactive plot with Plotly
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution'))
                    fig.update_layout(title=f'Normal Distribution of Returns for {ticker.upper()}',
                                    xaxis_title='Returns',
                                    yaxis_title='Frequency')
                    st.plotly_chart(fig)

                # Estimates the probability of returns falling within specified bounds.
                def estimate_return_probability(returns, lower_bound, higher_bound):
                    mean, std = np.mean(returns), np.std(returns)
                    prob = round(norm(mean, std).cdf(higher_bound) - norm(mean, std).cdf(lower_bound), 4)
                    return prob
                st.success("This segment allows us to get The returns of a company and see whether it would be between 2 and 3 for a specified period")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                    stock_ticker = ticker
                    higher_bound, lower_bound = 0.3, 0.2


                    # Retrieve and process stock data
                    df_returns = get_stock_returns(stock_ticker, start_date, end_date)
                    plot_return_distribution(df_returns['Return'], stock_ticker)

                    # Estimate probability
                    prob = estimate_return_probability(df_returns['Return'], lower_bound, higher_bound)
                    st.write(f'The probability of returns falling between {lower_bound} and {higher_bound} for {stock_ticker.upper()} is: {prob}')
                    
            if pred_option_analysis == "Kelly Criterion":
                st.success("This segment allows us to determine the optimal size of our investment based on a series of bets or investments in order to maximize long-term growth of capital")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                    # Define stock symbol and time frame for analysis
                    symbol = ticker

                    # Download stock data using yfinance package
                    stock_data = yf.download(symbol, start=start_date, end=end_date)

                    # Calculate daily returns and drop rows with missing data
                    stock_data['Returns'] = stock_data['Adj Close'].pct_change()
                    stock_data.dropna(inplace=True)

                    # Display the first few rows of the data for verification
                    st.write(stock_data.head())

                    # Calculate Kelly Criterion
                    # Extract positive (wins) and negative (losses) returns
                    wins = stock_data['Returns'][stock_data['Returns'] > 0]
                    losses = stock_data['Returns'][stock_data['Returns'] <= 0]

                    # Calculate win ratio and win-loss ratio
                    win_ratio = len(wins) / len(stock_data['Returns'])
                    win_loss_ratio = np.mean(wins) / np.abs(np.mean(losses))

                    # Apply Kelly Criterion formula
                    kelly_criterion = win_ratio - ((1 - win_ratio) / win_loss_ratio)

                    # Print the Kelly Criterion percentage
                    st.write('Kelly Criterion: {:.3f}%'.format(kelly_criterion * 100))

            if pred_option_analysis == "Intrinsic Value analysis":
                st.success("This segment allows us to determine the optimal size of our investment based on a series of bets or investments in order to maximize long-term growth of capital")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                # Set options for pandas display
                    pd.set_option('float_format', '{:f}'.format)

                    # API and stock configuration
                    base_url = "https://financialmodelingprep.com/api/v3/"
                    apiKey = "demo"  # Note: Demo API only works for AAPL stock
                    ticker = 'AAPL'
                    current_price = yf.download(ticker)['Adj Close'][-1]

                    # Function to retrieve JSON data from URL
                    def json_data(url):
                        response = urlopen(url)
                        data = response.read().decode("utf-8")
                        return json.loads(data)

                    # Retrieve financial statements
                    def get_financial_statements():
                        # Income statement
                        income = pd.DataFrame(json_data(f'{base_url}income-statement/{ticker}?apikey={apiKey}'))
                        income = income.set_index('date').apply(pd.to_numeric, errors='coerce')

                        # Cash flow statement
                        cash_flow = pd.DataFrame(json_data(f'{base_url}cash-flow-statement/{ticker}?apikey={apiKey}'))
                        cash_flow = cash_flow.set_index('date').apply(pd.to_numeric, errors='coerce')

                        # Balance sheet
                        balance_sheet = pd.DataFrame(json_data(f'{base_url}balance-sheet-statement/{ticker}?apikey={apiKey}'))
                        balance_sheet = balance_sheet.set_index('date').apply(pd.to_numeric, errors='coerce')

                        return income, cash_flow, balance_sheet

                    income, cash_flow, balance_sheet = get_financial_statements()

                    # Retrieve and process metrics from finviz
                    def get_finviz_data(ticker):
                        url = f"http://finviz.com/quote.ashx?t={ticker}"
                        headers = {'User-Agent': 'Mozilla/5.0'}
                        soup = BeautifulSoup(requests.get(url, headers=headers).content, features="lxml")

                        metrics = ['Beta', 'EPS next 5Y', 'Shs Outstand']
                        finviz_dict = {}
                        for m in metrics:   
                            finviz_dict[m] = soup.find(text=m).find_next(class_='snapshot-td2').text

                        # Process and convert metrics to appropriate formats
                        for key, value in finviz_dict.items():
                            if value[-1] in ['%', 'B', 'M']:
                                value = float(value[:-1])
                                if value[-1] == 'B':
                                    value *= 1e9
                                elif value[-1] == 'M':
                                    value *= 1e6
                            finviz_dict[key] = float(value)
                        return finviz_dict

                    finviz_data = get_finviz_data(ticker)
                    beta = finviz_data['Beta']

                    # Determine the discount rate based on beta
                    discount = 7 + beta * 2.5
                    if beta < 1:
                        discount = 6

                    # Calculate intrinsic value
                    def calc_intrinsic_value(cash_flow, total_debt, liquid_assets, eps_growth_5Y, eps_growth_6Y_to_10Y, eps_growth_11Y_to_20Y, shs_outstanding, discount):   
                        eps_growth_5Y /= 100
                        eps_growth_6Y_to_10Y /= 100
                        eps_growth_11Y_to_20Y /= 100
                        discount /= 100

                        cf_list = []
                        for year in range(1, 21):
                            growth_rate = eps_growth_5Y if year <= 5 else eps_growth_6Y_to_10Y if year <= 10 else eps_growth_11Y_to_20Y
                            cash_flow *= (1 + growth_rate)
                            discounted_cf = cash_flow / ((1 + discount)**year)
                            cf_list.append(discounted_cf)

                        intrinsic_value = (sum(cf_list) - total_debt + liquid_assets) / shs_outstanding
                        return intrinsic_value

                    intrinsic_value = calc_intrinsic_value(cash_flow.iloc[-1]['freeCashFlow'],
                                                        balance_sheet.iloc[-1]['totalDebt'],
                                                        balance_sheet.iloc[-1]['cashAndShortTermInvestments'],
                                                        finviz_data['EPS next 5Y'],
                                                        finviz_data['EPS next 5Y'] / 2,
                                                        np.minimum(finviz_data['EPS next 5Y'] / 2, 4),
                                                        finviz_data['Shs Outstand'],
                                                        discount)

                    # Calculate deviation from intrinsic value
                    percent_from_intrinsic_value = round((1 - current_price / intrinsic_value) * 100, 2)

                    # Display data in a DataFrame
                    data = {
                        'Attributes': ['Intrinsic Value', 'Current Price', 'Intrinsic Value % from Price', 'Free Cash Flow', 'Total Debt', 'Cash and ST Investments', 'EPS Growth 5Y', 'EPS Growth 6Y to 10Y', 'EPS Growth 11Y to 20Y', 'Discount Rate', 'Shares Outstanding'],
                        'Values': [intrinsic_value, current_price, percent_from_intrinsic_value, cash_flow.iloc[-1]['freeCashFlow'], balance_sheet.iloc[-1]['totalDebt'], balance_sheet.iloc[-1]['cashAndShortTermInvestments'], finviz_data['EPS next 5Y'], finviz_data['EPS next 5Y'] / 2, np.minimum(finviz_data['EPS next 5Y'] / 2, 4), discount, finviz_data['Shs Outstand']]
                    }
                    df = pd.DataFrame(data).set_index('Attributes')
                    st.write(df)

            if pred_option_analysis == "MA Backtesting":
                st.success("This segment allows us to determine the optimal size of our investment based on a series of bets or investments in order to maximize long-term growth of capital")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                initial_capital = st.text_input("Enter the initial amount you want to backtest with")
                if initial_capital:
                    message_four = (f"Amount captured : {initial_capital}")
                    st.success(message_four)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                # Configure the stock symbol, moving average windows, initial capital, and date range
                    symbol = ticker
                    short_window = 20
                    long_window = 50
                    initial_capital = 10000  # Starting capital

                    # Download stock data
                    stock_data = yf.download(symbol, start=start_date, end=end_date)

                    # Calculate short and long moving averages
                    stock_data['Short_MA'] = stock_data['Adj Close'].rolling(window=short_window).mean()
                    stock_data['Long_MA'] = stock_data['Adj Close'].rolling(window=long_window).mean()

                    # Generate trading signals (1 = buy, 0 = hold/sell)
                    stock_data['Signal'] = np.where(stock_data['Short_MA'] > stock_data['Long_MA'], 1, 0)
                    stock_data['Positions'] = stock_data['Signal'].diff()

                    # Calculate daily and cumulative portfolio returns
                    stock_data['Daily P&L'] = stock_data['Adj Close'].diff() * stock_data['Signal']
                    stock_data['Total P&L'] = stock_data['Daily P&L'].cumsum()
                    stock_data['Positions'] *= 100  # Position size for each trade

                    # Construct a portfolio to keep track of holdings and cash
                    portfolio = pd.DataFrame(index=stock_data.index)
                    portfolio['Holdings'] = stock_data['Positions'] * stock_data['Adj Close']       
                    portfolio['Cash'] = initial_capital - portfolio['Holdings'].cumsum()
                    portfolio['Total'] = portfolio['Cash'] + stock_data['Positions'].cumsum() * stock_data['Adj Close']
                    portfolio['Returns'] = portfolio['Total'].pct_change()

                    # Create matplotlib plot
                    fig = plt.figure(figsize=(14, 10))
                    ax1 = fig.add_subplot(2, 1, 1)
                    stock_data[['Short_MA', 'Long_MA', 'Adj Close']].plot(ax=ax1, lw=2.)
                    ax1.plot(stock_data.loc[stock_data['Positions'] == 1.0].index, stock_data['Short_MA'][stock_data['Positions'] == 1.0],'^', markersize=10, color='g', label='Buy Signal')
                    ax1.plot(stock_data.loc[stock_data['Positions'] == -1.0].index, stock_data['Short_MA'][stock_data['Positions'] == -1.0],'v', markersize=10, color='r', label='Sell Signal')
                    ax1.set_title(f'{symbol} Moving Average Crossover Strategy')
                    ax1.set_ylabel('Price in $')
                    ax1.grid()
                    ax1.legend()

                    # Convert matplotlib figure to Plotly figure
                    plotly_fig = go.Figure()

                    # Adding stock data to Plotly figure
                    for column in ['Short_MA', 'Long_MA', 'Adj Close']:
                        plotly_fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data[column], mode='lines', name=column))
                        buy_signals = stock_data.loc[stock_data['Positions'] == 1.0]
                        sell_signals = stock_data.loc[stock_data['Positions'] == -1.0]
                        plotly_fig.add_trace(go.Scatter(x=buy_signals.index, y=buy_signals['Short_MA'], mode='markers', marker=dict(symbol='triangle-up', size=10, color='green'), name='Buy Signal'))
                        plotly_fig.add_trace(go.Scatter(x=sell_signals.index, y=sell_signals['Short_MA'], mode='markers', marker=dict(symbol='triangle-down', size=10, color='red'), name='Sell Signal'))

                    # Set layout
                    plotly_fig.update_layout(
                        title=f'{symbol} Moving Average Crossover Strategy',
                        xaxis_title='Date',
                        yaxis_title='Price in $',
                        legend=dict(x=0, y=1, traceorder='normal', font=dict(family='sans-serif', size=12, color='black')),
                        height=600  # Adjust the height as needed
                    )

                    # Display Plotly figure using st.pyplot()
                    st.plotly_chart(plotly_fig)

                    # Subplot 1: Moving Average Crossover Strategy
                    ax1 = fig.add_subplot(2, 1, 1)
                    stock_data[['Short_MA', 'Long_MA', 'Adj Close']].plot(ax=ax1, lw=2.)
                    ax1.plot(stock_data.loc[stock_data['Positions'] == 1.0].index, stock_data['Short_MA'][stock_data['Positions'] == 1.0],'^', markersize=10, color='g', label='Buy Signal')
                    ax1.plot(stock_data.loc[stock_data['Positions'] == -1.0].index, stock_data['Short_MA'][stock_data['Positions'] == -1.0],'v', markersize=10, color='r', label='Sell Signal')
                    ax1.set_title(f'{symbol} Moving Average Crossover Strategy')
                    ax1.set_ylabel('Price in $')
                    ax1.grid()
                    ax1.legend()

                    # Subplot 2: Portfolio Value
                    ax2 = fig.add_subplot(2, 1, 2)
                    portfolio['Total'].plot(ax=ax2, lw=2.)
                    ax2.set_ylabel('Portfolio Value in $')
                    ax2.set_xlabel('Date')
                    ax2.grid()

                    plotly_fig = go.Figure()
                    line = ax2.get_lines()[0]  # Assuming there's only one line in the plot
                    x = line.get_xdata()
                    y = line.get_ydata()
                    plotly_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Portfolio Value Fluctuation in USD'))
                    plotly_fig.update_layout(
                        title=f'Portfolio Value in USD',
                        xaxis_title='Date',
                        yaxis_title=f'{ticker} Daily Returns',
                        legend=dict(x=0, y=1, traceorder='normal', font=dict(family='sans-serif', size=12, color='black'))
                    )
                    
                    # Display Plotly figure using st.pyplot()
                    st.plotly_chart(plotly_fig)

            if pred_option_analysis == "Ols Regression":
                st.success("This segment allows us to determine the optimal size of our investment based on a series of bets or investments in order to maximize long-term growth of capital")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                
                if st.button("Check"):
                    # Configure the stock symbol, start, and end dates for data
                    stock = ticker

                    # Fetch stock and S&P 500 data
                    stock_data = yf.download(stock, start_date, end_date)['Close']
                    sp500_data = yf.download('^GSPC',start_date, end_date)['Close']

                    # Combine data into a single DataFrame and calculate monthly returns
                    combined_data = pd.concat([stock_data, sp500_data], axis=1)
                    combined_data.columns = [stock, 'S&P500']
                    monthly_returns = combined_data.pct_change().dropna()

                    # Define dependent and independent variables for regression
                    X = monthly_returns['S&P500']  # Independent variable (S&P500 returns)
                    y = monthly_returns[stock]  # Dependent variable (Stock returns)

                    # Ordinary Least Squares (OLS) Regression using statsmodels
                    X_sm = sm.add_constant(X)  # Adding a constant
                    model = sm.OLS(y, X_sm)  # Model definition
                    results = model.fit()  # Fit the model
                    print(results.summary())  # Print the results summary

                    # Linear Regression using scipy
                    slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)

                    # Create matplotlib plot
                    plt.figure(figsize=(14, 7))
                    plt.scatter(X, y, alpha=0.5, label='Daily Returns')
                    plt.plot(X, intercept + slope * X, color='red', label='Regression Line')
                    plt.title(f'Regression Analysis: {stock} vs S&P 500')
                    plt.xlabel('S&P 500 Daily Returns')
                    plt.ylabel(f'{stock} Daily Returns')
                    plt.legend()
                    plt.grid(True)

                    # Convert matplotlib figure to Plotly figure
                    plotly_fig = go.Figure()
                    plotly_fig.add_trace(go.Scatter(x=X, y=y, mode='markers', name='Daily Returns'))
                    plotly_fig.add_trace(go.Scatter(x=X, y=intercept + slope * pd.Series(X), mode='lines', name='Regression Line'))

                    plotly_fig.update_layout(
                        title=f'Regression Analysis: {stock} vs S&P 500',
                        xaxis_title='S&P 500 Daily Returns',
                        yaxis_title=f'{stock} Daily Returns',
                        legend=dict(x=0, y=1, traceorder='normal', font=dict(family='sans-serif', size=12, color='black'))
                    )

                    # Display Plotly figure using st.pyplot()
                    st.plotly_chart(plotly_fig)

                    # Calculate beta and alpha
                    beta = slope
                    alpha = intercept
                    st.write(f'alpha (intercept) = {alpha:.4f}')
                    st.write(f'beta (slope) = {beta:.4f}')

            if pred_option_analysis == "Perfomance Risk Analysis":
                st.success("This segment allows us to determine the perfomance risk of a ticker against S&P 500 using Alpha, beta and R squared")
                ticker = st.text_input("Enter the ticker you want to test")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):
                    index = '^GSPC'
                    stock = ticker
                    # Fetching data for the stock and S&P 500 index
                    df_stock =yf.download(stock,start_date, end_date)
                    df_index =yf.download(index,start_date, end_date)

                    # Resampling the data to a monthly time series
                    df_stock_monthly = df_stock['Adj Close'].resample('M').last()
                    df_index_monthly = df_index['Adj Close'].resample('M').last()

                    # Calculating monthly returns
                    stock_returns = df_stock_monthly.pct_change().dropna()
                    index_returns = df_index_monthly.pct_change().dropna()

                    # Computing Beta, Alpha, and R-squared
                    cov_matrix = np.cov(stock_returns, index_returns)
                    beta = cov_matrix[0, 1] / cov_matrix[1, 1]
                    alpha = np.mean(stock_returns) - beta * np.mean(index_returns)

                    y_pred = alpha + beta * index_returns
                    r_squared = 1 - np.sum((y_pred - stock_returns) ** 2) / np.sum((stock_returns - np.mean(stock_returns)) ** 2)

                    # Calculating Volatility and Momentum
                    volatility = np.std(stock_returns) * np.sqrt(12)  # Annualized volatility
                    momentum = np.prod(1 + stock_returns.tail(12)) - 1  # 1-year momentum

                    # Printing the results
                    st.write(f'Beta: {beta:.4f}')
                    st.write(f'Alpha: {alpha:.4f} (annualized)')
                    st.write(f'R-squared: {r_squared:.4f}')
                    st.write(f'Volatility: {volatility:.4f}')
                    st.write(f'1-Year Momentum: {momentum:.4f}')

                    # Calculating the average volume over the last 60 days
                    average_volume = df_stock['Volume'].tail(60).mean()
                    st.write(f'Average Volume (last 60 days): {average_volume:.2f}')
                
            if pred_option_analysis == "Risk/Returns Analysis":

                st.success("This code allows us to see the contextual risk of related tickers")
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                # Replace this with your actual sectors and tickers
                sectors = {
                    "Technology": ['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'INTC', 'CSCO', 'ADBE', 'AVGO', 'PYPL'],
                    "Health Care": ['JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'TMO', 'MDT', 'DHR', 'AMGN', 'LLY'],
                    "Financials": ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'AXP', 'BLK', 'SPGI', 'USB'],
                    "Consumer Discretionary": ['AMZN', 'TSLA', 'HD', 'MCD', 'DIS', 'NKE', 'SBUX', 'BKNG', 'LOW', 'CMG'],
                    "Communication Services": ['GOOGL', 'META', 'DIS', 'CMCSA', 'NFLX', 'T', 'CHTR', 'DISCA', 'FOXA', 'VZ'],
                    "Industrials": ['BA', 'HON', 'UNP', 'UPS', 'CAT', 'LMT', 'MMM', 'GD', 'GE', 'CSX'],
                    "Consumer Staples": ['PG', 'KO', 'PEP', 'WMT', 'COST', 'CL', 'MO', 'EL', 'KHC', 'MDLZ'],
                    "Utilities": ['NEE', 'DUK', 'SO', 'D', 'EXC', 'AEP', 'SRE', 'PEG', 'XEL', 'ED'],
                    "Real Estate": ['AMT', 'PLD', 'CCI', 'EQIX', 'WY', 'PSA', 'DLR', 'BXP', 'O', 'SBAC'],
                    "Materials": ['LIN', 'APD', 'SHW', 'DD', 'ECL', 'DOW', 'NEM', 'PPG', 'VMC', 'FCX']
                }

                pred_option_analysis = st.selectbox("Select Analysis", ["Risk/Returns Analysis"])
                selected_sector = st.selectbox('Select Sector', list(sectors.keys()))
                if st.button("Start Analysis"):
                    # Downloading and processing stock data
                    df = pd.DataFrame()
                    for symbol in sectors[selected_sector]:
                        df[symbol] = yf.download(symbol, start_date, end_date)['Adj Close']
                    # Dropping rows with missing values
                    df = df.dropna()
                    # Calculating percentage change in stock prices
                    rets = df.pct_change(periods=3)

                    # Creating correlation matrix heatmap
                    corr = rets.corr()
                    fig = go.Figure(data=go.Heatmap(
                        z=corr.values,
                        x=corr.index,
                        y=corr.columns,
                        colorscale='Blues'
                    ))
                    fig.update_layout(
                        title="Correlation Matrix Heatmap",
                        xaxis_title="Stock Symbols",
                        yaxis_title="Stock Symbols"
                    )
                    st.plotly_chart(fig)

                    # Plotting bar charts for risk and average returns
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=rets.columns, y=rets.std(), name='Risk (Std. Dev.)', marker_color='red'))
                    fig.add_trace(go.Bar(x=rets.columns, y=rets.mean(), name='Average Returns', marker_color='blue'))
                    fig.update_layout(
                        title="Risk and Average Returns",
                        xaxis_title="Stock Symbols",
                        yaxis_title="Value",
                        barmode='group'
                    )
                    st.plotly_chart(fig)

                    # Stacked bar chart for risk vs return
                    fig = go.Figure()
                    for i, symbol in enumerate(sectors[selected_sector]):
                        fig.add_trace(go.Bar(x=[symbol], y=[rets.mean()[i]], name='Average of Returns', marker_color='blue'))
                        fig.add_trace(go.Bar(x=[symbol], y=[rets.std()[i]], name='Risk of Returns', marker_color='red'))
                    fig.update_layout(
                        title='Risk vs Average Returns',
                        xaxis_title='Stock Symbols',
                        yaxis_title='Value',
                        barmode='stack'
                    )
                    st.plotly_chart(fig)

                    # Scatter plot for expected returns vs risk
                    fig = go.Figure()
                    for i in range(len(rets.columns)):
                        fig.add_trace(go.Scatter(x=rets.mean(), y=rets.std(), mode='markers', text=rets.columns))
                        fig.update_layout(
                            title='Risk vs Expected Returns',
                            xaxis_title='Expected Returns',
                            yaxis_title='Risk'
                        )
                        st.plotly_chart(fig)

                    # Display table with risk vs expected returns
                    risk_returns_table = pd.DataFrame({'Risk': rets.std(), 'Expected Returns': rets.mean()})
                    st.write("Table: Risk vs Expected Returns")
                    st.write(risk_returns_table)
            if pred_option_analysis == "Seasonal Stock Analysis":
                st.write("This segment allows us to analyze the seasonal returns of s&p 500")
                if st.button("Analyze"):
                    # Scrape a list of the S&P 500 components using your ticker function
                    sp500_tickers = ti.tickers_sp500()
                    threshold = 0.80
                    # Upload a list of the S&P 500 components downloaded from Wikipedia using your ticker function
                    df_sp500_tickers = pd.DataFrame(sp500_tickers, columns=["Symbol"])

                    # Loops through the S&P 500 tickers, downloads the data from Yahoo and creates a DataFrame for each ticker.
                    dfs = []
                    for ticker in ti.tickers_sp500():
                        yf_ticker = yf.Ticker(ticker)
                        data = yf_ticker.history(period="max")
                        data.reset_index(inplace=True)
                        data.drop_duplicates(subset="Date", keep="first", inplace=True)
                        data['Symbol'] = ticker
                        dfs.append(data)

                    # Concatenate all DataFrames into a single DataFrame
                    df_combined = pd.concat(dfs, ignore_index=True)

                    # Creates the dataframe container for the stats data.
                    df_tradelist = pd.DataFrame(
                        index=[],
                        columns=[
                            "my_ticker",
                            "hold_per",
                            "pct_uprows",
                            "max_up_return",
                            "min_up_return",
                            "avg_up_return",
                            "avg_down_return",
                            "exp_return",
                            "stdev_returns",
                            "pct_downside",
                            "worst_return",
                            "least_pain_pt",
                            "total_years",
                            "max_consec_beat",
                            "best_buy_date",
                            "best_sell_date",
                            "analyzed_years",
                        ],
                    )
                    df_tradelist.head()

                    # Separate out the date column into separate month, year and day values.
                    def separate_date_column():
                        global dfr
                        dfr["Month"] = pd.DatetimeIndex(dfr["Date"]).month
                        dfr["Day"] = pd.DatetimeIndex(dfr["Date"]).day
                        dfr["Year"] = pd.DatetimeIndex(dfr["Date"]).year
                        dfr["M-D"] = dfr["Month"].astype(str) + "-" + dfr["Day"].astype(str)
                        pd.set_option("display.max_rows", len(dfr))

                    # Pivot the table to show years across the top and Month-Day values in the first column on the left.
                    def pivot_the_table():
                        global dfr_pivot
                        dfr_pivot = dfr.pivot(index="M-D", columns="Year", values="Returns")
                        dfr_pivot.reset_index(level=0, inplace=True)
                        dfr_pivot = pd.DataFrame(dfr_pivot)
                        dfr_pivot.columns.name = "Index"
                        dfr_pivot.fillna(method="ffill", inplace=True)

                    # Add additional calculated columns to facilitate statistic calculations for each stock.
                    def add_calculated_items():
                        global dfr_pivot
                        global lookback
                        global start

                        # The lookback figure is the number (must be an integer) of years back from last year that you want to include
                        lookback = 20
                        start = 1
                        if lookback > len(dfr_pivot.columns) - 1:
                            start = 1
                        else:
                            start = len(dfr_pivot.columns) - lookback
                        dfr_pivot["YearCount"] = dfr_pivot.count(axis=1, numeric_only=True)
                        dfr_pivot["Lookback"] = lookback
                        dfr_pivot["UpCount"] = dfr_pivot[
                            dfr_pivot.iloc[:, start: len(dfr_pivot.columns) - 2] > 0
                        ].count(axis=1)
                        dfr_pivot["DownCount"] = dfr_pivot[
                            dfr_pivot.iloc[:, start: len(dfr_pivot.columns)] < 0
                        ].count(axis=1)
                        dfr_pivot["PctUp"] = dfr_pivot["UpCount"] / dfr_pivot["Lookback"]
                        dfr_pivot["PctDown"] = dfr_pivot["DownCount"] / dfr_pivot["Lookback"]
                        dfr_pivot["AvgReturn"] = dfr_pivot.iloc[:, start: len(dfr_pivot.columns) - 6].mean(
                            axis=1
                        )
                        dfr_pivot["StDevReturns"] = dfr_pivot.iloc[
                            :, start: len(dfr_pivot.columns) - 7
                        ].std(axis=1)
                        dfr_pivot["67PctDownside"] = dfr_pivot["AvgReturn"] - dfr_pivot["StDevReturns"]
                        dfr_pivot["MaxReturn"] = dfr_pivot.iloc[:, start: len(dfr_pivot.columns) - 9].max(
                            axis=1
                        )
                        dfr_pivot["MinReturn"] = dfr_pivot.iloc[:, start: len(dfr_pivot.columns) - 10].min(
                            axis=1
                        )

                    # Calculate the trading statistics for the rolling holding periods for the stock.
                    def calc_trading_stats():
                        global interval
                        global dfr_pivot
                        global pct_uprows
                        global max_up_return
                        global min_up_return
                        global avg_up_return
                        global avg_down_return
                        global exp_return
                        global stdev_returns
                        global pct_downside
                        global worst_return
                        global least_pain_pt
                        global total_years
                        global n_consec
                        global max_n_consec
                        global max_consec_beat
                        global best_sell_date
                        global best_buy_date
                        global analyzed_years
                        global lookback

                        pct_uprows = (
                            (
                                dfr_pivot.loc[dfr_pivot["PctUp"] > threshold, "PctUp"].count()
                                / dfr_pivot.loc[:, "PctUp"].count()
                            )
                            .astype(float)
                            .round(4)
                        )
                        max_up_return = dfr_pivot.loc[dfr_pivot["PctUp"] > threshold, "MaxReturn"].max()
                        min_up_return = dfr_pivot.loc[dfr_pivot["PctUp"] > threshold, "MinReturn"].min()
                        avg_up_return = dfr_pivot.loc[dfr_pivot["PctUp"] > 0.5, "AvgReturn"].mean()
                        avg_up_return = np.float64(avg_up_return).round(4)
                        avg_down_return = dfr_pivot.loc[dfr_pivot["PctDown"] > 0.5, "AvgReturn"].mean()
                        avg_down_return = np.float64(avg_down_return).round(4)
                        exp_return = round(dfr_pivot["AvgReturn"].mean(), 4)
                        stdev_returns = dfr_pivot["StDevReturns"].mean()
                        stdev_returns = np.float64(stdev_returns).round(4)
                        worst_return = dfr_pivot["MinReturn"].min()
                        pct_downside = exp_return - stdev_returns
                        pct_downside = np.float64(pct_downside).round(4)
                        least_pain_pt = dfr_pivot.loc[dfr_pivot["PctUp"] > threshold, "67PctDownside"].max()
                        total_years = dfr_pivot["YearCount"].max()
                        analyzed_years = lookback
                        n_consec = 0
                        max_n_consec = 0

                        for x in dfr_pivot["PctUp"]:
                            if x > threshold:
                                n_consec += 1
                            else:  # check for new max, then start again from 1
                                max_n_consec = max(n_consec, max_n_consec)
                                n_consec = 1
                        max_consec_beat = max_n_consec
                        try:
                            best_sell_date = dfr_pivot.loc[
                                dfr_pivot["67PctDownside"] == least_pain_pt, "M-D"
                            ].iloc[0]
                        except:
                            best_sell_date = "nan"
                        try:
                            row = (
                                dfr_pivot.loc[dfr_pivot["M-D"] == best_sell_date, "M-D"].index[0] - interval
                            )
                            col = dfr_pivot.columns.get_loc("M-D")
                            best_buy_date = dfr_pivot.iloc[row, col]
                        except:
                            best_buy_date = "nan"

                    # Convert prices to holding period returns based on a specified number of trading days.
                    def convert_prices_to_periods():
                        global dfr
                        global dperiods
                        dfr = df.pct_change(periods=dperiods)
                        dfr.reset_index(level=0, inplace=True)
                        dfr.rename(columns={"Close": "Returns"}, inplace=True)
                        dfr = dfr.round(4)
                    # Reset the index and round the float values to 4 decimals.
                    def sortbydate_resetindex_export():
                        global dfr_pivot
                        dfr_pivot["Date"] = "2000-" + dfr_pivot["M-D"].astype(str)
                        dfr_pivot["Date"] = pd.to_datetime(dfr_pivot["Date"], infer_datetime_format=True)
                        dfr_pivot.sort_values(by="Date", ascending=True, inplace=True)
                        dfr_pivot.reset_index(inplace=True)
                        dfr_pivot = dfr_pivot.round(4)
                    # This module grabs each ticker file, transforms it, and calculates the statistics needed for a 90-day holding period.
                    def calc_3month_returns():
                        global dfr
                        global dfr_pivot
                        global df_tradelist
                        global dfr_3mo
                        global df_statsdata_3mo
                        global threshold
                        global hold_per
                        global dperiods
                        global interval
                        dperiods = 60
                        hold_per = "3 Mos"
                        interval = 90
                        convert_prices_to_periods()
                        separate_date_column()
                        pivot_the_table()
                        add_calculated_items()
                        sortbydate_resetindex_export()

                        dfr_3mo = pd.DataFrame(dfr_pivot)
                        calc_trading_stats()
                        filter_and_append_stats()

                        df_statsdata_3mo = df_statsdata.copy()


                    # This module grabs each ticker file, transforms it, and calculates the statistics needed for a 60-day holding period.
                    def calc_2month_returns():
                        global dfr
                        global dfr_pivot
                        global df_tradelist
                        global dfr_2mo
                        global df_statsdata_2mo
                        global threshold
                        global hold_per
                        global dperiods
                        global interval
                        dperiods = 40
                        hold_per = "2 Mos"
                        interval = 60
                        convert_prices_to_periods()
                        separate_date_column()
                        pivot_the_table()
                        add_calculated_items()
                        sortbydate_resetindex_export()

                        dfr_2mo = pd.DataFrame(dfr_pivot)
                        calc_trading_stats()
                        filter_and_append_stats()

                        df_statsdata_2mo = df_statsdata.copy()


                    # This module grabs each ticker file, transforms it, and calculates the statistics needed for a 30-day holding period.
                    def calc_1month_returns():
                        global dfr
                        global dfr_pivot
                        global df_tradelist
                        global dfr_1mo
                        global df_statsdata_1mo
                        global threshold
                        global hold_per
                        global dperiods
                        global interval
                        dperiods = 20
                        hold_per = "1 Mo"
                        interval = 30
                        convert_prices_to_periods(df)
                        separate_date_column()
                        pivot_the_table()
                        add_calculated_items()
                        sortbydate_resetindex_export()

                        dfr_1mo = pd.DataFrame(dfr_pivot)
                        calc_trading_stats()
                        filter_and_append_stats()

                        df_statsdata_1mo = df_statsdata.copy()

                    # If the pct_uprows and history conditions are met, then create the array of stat values and append it to the recommended trade list.
                    def filter_and_append_stats():
                        global statsdata
                        global df_statsdata
                        global df_tradelist

                        # Save the stats data separately to export to Excel for further research on each ticker if desired.
                        statsdata = np.array(
                            [
                                my_ticker,
                                hold_per,
                                pct_uprows,
                                max_up_return,
                                min_up_return,
                                avg_up_return,
                                avg_down_return,
                                exp_return,
                                stdev_returns,
                                pct_downside,
                                worst_return,
                                least_pain_pt,
                                total_years,
                                max_consec_beat,
                                best_buy_date,
                                best_sell_date,
                                analyzed_years,
                            ]
                        )
                        df_statsdata = pd.DataFrame(
                            statsdata.reshape(-1, len(statsdata)),
                            columns=[
                                "my_ticker",
                                "hold_per",
                                "pct_uprows",
                                "max_up_return",
                                "min_up_return",
                                "avg_up_return",
                                "avg_down_return",
                                "exp_return",
                                "stdev_returns",
                                "pct_downside",
                                "worst_return",
                                "least_pain_pt",
                                "total_years",
                                "max_consec_beat",
                                "best_buy_date",
                                "best_sell_date",
                                "analyzed_years",
                            ],
                        )
                        if pct_uprows > 0.1:
                            if total_years > 9:
                                df_tradelist = df_tradelist.append(
                                    dict(zip(df_tradelist.columns, statsdata)), ignore_index=True
                                )

                    for index, ticker in df_sp500_tickers.iterrows():
                        my_ticker = ticker["Symbol"]
                        calc_1month_returns()
                        calc_2month_returns()
                        calc_3month_returns()
                        filter_and_append_stats()

                    # Make a copy and convert the trade list to a Pandas dataframe.
                    df_tradelist = pd.DataFrame(df_tradelist)

                    # Clean it up by removing rows with NaN's and infinity values and dropping duplicates.
                    df_tradelist.replace("inf", np.nan, inplace=True)
                    df_tradelist.dropna(inplace=True)
                    df_tradelist = df_tradelist[~df_tradelist.max_up_return.str.contains("nan")]
                    df_tradelist = df_tradelist[~df_tradelist.avg_down_return.str.contains("nan")]
                    df_tradelist.sort_values(by=["pct_uprows"], ascending=False)
                    df_tradelist.drop_duplicates(subset="my_ticker", keep="first", inplace=True)
                    df_tradelist.tail(10)
                    df_tradelist.head()


        
            if pred_option_analysis == "SMA Histogram":

                st.success("This segment allows you to see the SMA movement of the stock")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)

                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                    stock = ticker
                    # Fetch stock data
                    df = yf.download(stock, start_date, end_date)

                    # Calculate Simple Moving Average (SMA)
                    sma = 50
                    df['SMA' + str(sma)] = df['Adj Close'].rolling(window=sma).mean()
                    
                    # Calculate percentage change from SMA
                    df['PC'] = ((df["Adj Close"] / df['SMA' + str(sma)]) - 1) * 100

                    # Calculating statistics
                    mean = df["PC"].mean()
                    stdev = df["PC"].std()
                    current = df["PC"].iloc[-1]
                    yday = df["PC"].iloc[-2]

                    # Histogram settings
                    bins = np.arange(-100, 100, 1)

                    # Plotting histogram
                    fig = go.Figure()

                    # Add histogram trace
                    fig.add_trace(go.Histogram(x=df["PC"], histnorm='percent', nbinsx=len(bins), name='Count'))

                    # Adding vertical lines for mean, std deviation, current and yesterday's percentage change
                    for i in range(-3, 4):
                        fig.add_shape(
                            dict(type="line", x0=mean + i * stdev, y0=0, x1=mean + i * stdev, y1=100, line=dict(color="gray", dash="dash"),
                                opacity=0.5 + abs(i)/6)
                        )
                    fig.add_shape(
                        dict(type="line", x0=current, y0=0, x1=current, y1=100, line=dict(color="red"), name='Today')
                    )
                    fig.add_shape(
                        dict(type="line", x0=yday, y0=0, x1=yday, y1=100, line=dict(color="blue"), name='Yesterday')
                    )

                    # Update layout
                    fig.update_layout(
                        title=f"{stock} - % From {sma} SMA Histogram since {start_date.year}",
                        xaxis_title=f'Percent from {sma} SMA (bin size = 1)',
                        yaxis_title='Percentage of Total',
                        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
                    )

                    st.plotly_chart(fig)

            if pred_option_analysis == "SP500 COT Sentiment Analysis":
                st.success("This segment allows us to look at COT Sentiment analysis of tickers for the past 1 or more years")
                    # Function to download and extract COT file
                def download_and_extract_cot_file(url, file_name):
                    # Download and extract COT file
                    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                    with zipfile.ZipFile(file_name) as zf:
                        zf.extractall()

                    # Download and process COT data for the last 5 years
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):
                    this_year = end_date.year
                    start_year = start_date.year
                    frames = []
                    for year in range(start_year, this_year):
                        #TODO - fix the link CFTC link
                        url = f'https://www.cftc.gov/files/dea/history/fut_fin_xls_{year}.zip'
                        download_and_extract_cot_file(url, f'{year}.zip')
                        os.rename('FinFutYY.xls', f'{year}.xls')

                        data = pd.read_excel(f'{year}.xls')
                        data = data.set_index('Report_Date_as_MM_DD_YYYY')
                        data.index = pd.to_datetime(data.index)
                        data = data[data['Market_and_Exchange_Names'] == 'E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE']
                        frames.append(data)

                    # Concatenate yearly data frames
                    df = pd.concat(frames)
                    df.to_csv('COT_sp500_data.csv')

                    # Read data for plotting
                    df = pd.read_csv('COT_sp500_data.csv', index_col=0)
                    df.index = pd.to_datetime(df.index)

                    # Plotting Line Chart
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df['Pct_of_OI_Dealer_Long_All'], mode='lines', name='Dealer Long'))
                    fig1.add_trace(go.Scatter(x=df.index, y=df['Pct_of_OI_Lev_Money_Long_All'], mode='lines', name='Leveraged Long'))
                    fig1.add_trace(go.Scatter(x=df.index, y=df['Pct_of_OI_Dealer_Short_All'], mode='lines', name='Dealer Short'))
                    fig1.add_trace(go.Scatter(x=df.index, y=df['Pct_of_OI_Lev_Money_Short_All'], mode='lines', name='Leveraged Short'))
                    fig1.update_layout(title='Net Positions - Line Chart', xaxis_title='Date', yaxis_title='Percentage')
                    st.plotly_chart(fig1)

                    # Box Plot
                    fig2 = go.Figure()
                    fig2.add_trace(go.Box(y=df['Pct_of_OI_Dealer_Long_All'], name='Dealer Long'))
                    fig2.add_trace(go.Box(y=df['Pct_of_OI_Dealer_Short_All'], name='Dealer Short'))
                    fig2.add_trace(go.Box(y=df['Pct_of_OI_Lev_Money_Long_All'], name='Leveraged Money Long'))
                    fig2.add_trace(go.Box(y=df['Pct_of_OI_Lev_Money_Short_All'], name='Leveraged Money Short'))
                    fig2.update_layout(title='Distribution of Open Interest by Category', yaxis_title='Percentage')
                    st.plotly_chart(fig2)

                    filtered_df = df.loc[start_date:end_date]
                    # Plotting Line Chart
                    fig3 = go.Figure()
                    fig3.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['Pct_of_OI_Dealer_Long_All'], mode='lines', name='Dealer Long'))
                    fig3.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['Pct_of_OI_Lev_Money_Long_All'], mode='lines', name='Leveraged Long'))
                    fig3.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['Pct_of_OI_Dealer_Short_All'], mode='lines', name='Dealer Short'))
                    fig3.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['Pct_of_OI_Lev_Money_Short_All'], mode='lines', name='Leveraged Short'))
                    fig3.update_layout(title='Net Positions - Line Chart', xaxis_title='Date', yaxis_title='Percentage')
                    st.plotly_chart(fig3)

            if pred_option_analysis == "SP500 Valuation":
                if st.button("Check"):
                    # Load the S&P 500 data
                    #sp_df = pd.read_excel("http://www.stern.nyu.edu/~adamodar/pc/datasets/spearn.xls", sheet_name="Sheet1")
                    sp_df = []
                    for ticker in ti.tickers_sp500():
                        yf_ticker = yf.Ticker(ticker)
                        data = yf_ticker.history(period="max")
                        data.reset_index(inplace=True)
                        data.drop_duplicates(subset="Date", keep="first", inplace=True)
                        data['Symbol'] = ticker
                        sp_df.append(data)

                    clean_df = sp_df
                    # Clean the data
                    '''
                    clean_df = sp_df.drop([i for i in range(6)], axis=0)
                    rename_dict = {}
                    for i in sp_df.columns:
                        rename_dict[i] = sp_df.loc[6, i]
                    clean_df = clean_df.rename(rename_dict, axis=1)
                    clean_df = clean_df.drop(6, axis=0)
                    clean_df = clean_df.drop(clean_df.index[-1], axis=0)
                    clean_df = clean_df.set_index("Year")
                    '''
                    # Calculate earnings and dividend growth rates
                    clean_df["earnings_growth"] = clean_df["Earnings"] / clean_df["Earnings"].shift(1) - 1
                    clean_df["dividend_growth"] = clean_df["Dividends"] / clean_df["Dividends"].shift(1) - 1

                    # Calculate 10-year mean growth rates for earnings and dividends
                    clean_df["earnings_10yr_mean_growth"] = clean_df["earnings_growth"].expanding(10).mean()
                    clean_df["dividends_10yr_mean_growth"] = clean_df["dividend_growth"].expanding(10).mean()

                    # Plot earnings growth rates and 10-year mean growth rates
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=clean_df.index, y=clean_df["earnings_growth"], mode='lines', name='Year over Year Earnings Growth'))
                    fig.add_trace(go.Scatter(x=clean_df.index, y=clean_df["earnings_10yr_mean_growth"], mode='lines', name='Rolling 10 Year Mean'))
                    fig.update_layout(title="Earnings Growth Rates", xaxis_title="Year", yaxis_title="Earnings Growth")
                    st.plotly_chart(fig)

                    # Base case valuation of S&P 500
                    valuations = []

                    # Slower recovery
                    eps_growth_2020 = (11.88 + 17.76 + 25 + 25) / (34.95 + 35.08 + 33.99 + 35.72) - 1
                    bad_eps_2020 = clean_df.iloc[-1]["Earnings"] * (1 + eps_growth_2020)
                    eps_next = 24 * 4
                    eps_growth = [0, 0.15, 0.22, 0.20, 0.16, 0.13, 0.11, 0.09, 0.08, 0.08]

                    bad_df = pd.DataFrame()
                    bad_df["earnings"] = (np.array(eps_growth) + 1).cumprod() * eps_next
                    bad_df["dividends"] = 0.50 * bad_df["earnings"]
                    bad_df["year"] = [i for i in range(2021, 2031)]
                    bad_df.set_index("year", inplace=True)

                    pv_dividends = 0
                    for i in range(bad_df.shape[0]):
                        pv_dividends += bad_df["dividends"].iloc[i] / (1 + 0.08) ** i

                    terminal_value = (bad_df["dividends"].iloc[-1] * (1 + 0.04) / (0.08 - 0.04))
                    valuations.append(pv_dividends + terminal_value / (1 + 0.08) ** 10)

                    # Double dip
                    eps_growth_2020 = (11.88 + 17.76 + 25 + 25) / (34.95 + 35.08 + 33.99 + 35.72) - 1
                    worst_eps_2020 = clean_df.iloc[-1]["Earnings"] * (1 + eps_growth_2020)
                    eps_next = 24 * 4
                    eps_growth = [0, -0.1, 0, 0.25, 0.25, 0.15, 0.12, 0.10, 0.08, 0.08]

                    worst_df = pd.DataFrame()
                    worst_df["earnings"] = (np.array(eps_growth) + 1).cumprod() * eps_next
                    worst_df["dividends"] = 0.50 * worst_df["earnings"]
                    worst_df["year"] = [i for i in range(2021, 2031)]
                    worst_df.set_index("year", inplace=True)

                    pv_dividends = 0
                    for i in range(worst_df.shape[0]):
                        pv_dividends += worst_df["dividends"].iloc[i] / (1 + 0.08) ** i

                    terminal_value = (worst_df["dividends"].iloc[-1] * (1 + 0.04) / (0.08 - 0.04))
                    valuations.append(pv_dividends + terminal_value / (1 + 0.08) ** 10)

                    # V-shaped EPS growth
                    eps_growth_2020 = (11.88 + 17.76 + 28.27 + 31.78) / (34.95 + 35.08 + 33.99 + 35.72) - 1
                    eps_2020 = clean_df.iloc[-1]["Earnings"] * (1 + eps_growth_2020)
                    eps_next = 28.27 + 31.78 + 32.85 + 36.77
                    eps_growth = [
                        0,
                        (clean_df.iloc[-1]["Earnings"]) / eps_next - 1,
                        0.18,
                        0.14,
                        0.10,
                        0.08,
                        0.08,
                        0.08,
                        0.08,
                        0.08,
                    ]

                    value_df = pd.DataFrame()
                    value_df["earnings"] = (np.array(eps_growth) + 1).cumprod() * eps_next
                    value_df["dividends"] = 0.50 * value_df["earnings"]
                    value_df["year"] = [i for i in range(2021, 2031)]
                    value_df.set_index("year", inplace=True)

                    pv_dividends = 0
                    for i in range(value_df.shape[0]):
                        pv_dividends += value_df["dividends"].iloc[i] / (1 + 0.08) ** i

                    terminal_value = (value_df["dividends"].iloc[-1] * (1 + 0.04) / (0.08 - 0.04))
                    valuations.append(pv_dividends + terminal_value / (1 + 0.08) ** 10)

                    # Interactive visualization of earnings scenarios
                    earnings_scenarios = pd.DataFrame()
                    earnings_scenarios["Actual"] = pd.concat([clean_df.tail(15)["Earnings"], pd.Series([eps_2020], index=[2020]), value_df["earnings"]], axis=0)
                    earnings_scenarios["Base Estimate"] = pd.concat([clean_df.tail(15)["Earnings"] * 0, pd.Series([eps_2020], index=[2020]) * 0, value_df["earnings"]], axis=0)
                    earnings_scenarios["Bad Estimate"] = pd.concat([clean_df.tail(15)["Earnings"] * 0, pd.Series([bad_eps_2020], index=[2020]) * 0, bad_df["earnings"]], axis=0)
                    earnings_scenarios["Worst Estimate"] = pd.concat([clean_df.tail(15)["Earnings"] * 0, pd.Series([worst_eps_2020], index=[2020]) * 0, worst_df["earnings"]], axis=0)

                    fig = go.Figure()
                    for column in earnings_scenarios.columns:
                        fig.add_trace(go.Bar(x=earnings_scenarios.index, y=earnings_scenarios[column], name=column))

                    fig.update_layout(title="S&P 500 Earnings Per Share Scenarios", xaxis_title="Year", yaxis_title="Earnings Per Share")
                    st.plotly_chart(fig)

                    # Interactive visualization of valuations
                    valuation_data = pd.DataFrame(valuations, columns=["Valuation"], index=["Slower Recovery", "Double Dip", "V-shaped"])

                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=valuation_data.index, y=valuation_data["Valuation"], name="Valuation", marker_color="blue"))

                    fig.update_layout(title="S&P 500 Valuations", xaxis_title="Scenario", yaxis_title="Valuation")
                    st.plotly_chart(fig)

            if pred_option_analysis == "Stock Pivot Resistance":
                # Function to fetch and plot stock data with pivot points
                def plot_stock_pivot_resistance(stock_symbol, start_date, end_date):
                    df = yf.download(stock_symbol, start_date, end_date)
                    # Plot high prices
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["High"], mode='lines', name='High'))
                    
                    # Initialize variables to find and store pivot points
                    pivots = []
                    dates = []
                    counter = 0
                    last_pivot = 0
                    window_size = 10
                    window = [0] * window_size
                    date_window = [0] * window_size

                    # Identify pivot points
                    for i, high_price in enumerate(df["High"]):
                        window = window[1:] + [high_price]
                        date_window = date_window[1:] + [df.index[i]]

                        current_max = max(window)
                        if current_max == last_pivot:
                            counter += 1
                        else:
                            counter = 0

                        if counter == 5:
                            last_pivot = current_max
                            last_date = date_window[window.index(last_pivot)]
                            pivots.append(last_pivot)
                            dates.append(last_date)
                    # Plot resistance levels for each pivot point
                    for i in range(len(pivots)):
                        time_delta = dt.timedelta(days=30)
                        fig.add_shape(type="line",
                                    x0=dates[i], y0=pivots[i],
                                    x1=dates[i] + time_delta, y1=pivots[i],
                                    line=dict(color="red", width=4, dash="solid")
                                    )
                    # Configure plot settings
                    fig.update_layout(title=stock_symbol.upper() + ' Resistance Points', xaxis_title='Date', yaxis_title='Price')
                    st.plotly_chart(fig)
            
                st.write ("This segment allows us to analyze the pivot resistance points of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    plot_stock_pivot_resistance(ticker,start_date, end_date)


            if pred_option_analysis == "Stock Profit/Loss Analysis":

                def calculate_stock_profit_loss(symbol, start_date, end_date, initial_investment):
                    # Download stock data
                    dataset = yf.download(symbol, start_date, end_date)

                    # Calculate the number of shares and investment values
                    shares = initial_investment / dataset['Adj Close'][0]
                    current_value = shares * dataset['Adj Close'][-1]

                    # Calculate profit or loss and related metrics
                    profit_or_loss = current_value - initial_investment
                    percentage_gain_or_loss = (profit_or_loss / current_value) * 100
                    percentage_returns = (current_value - initial_investment) / initial_investment * 100
                    net_gains_or_losses = (dataset['Adj Close'][-1] - dataset['Adj Close'][0]) / dataset['Adj Close'][0] * 100
                    total_return = ((current_value / initial_investment) - 1) * 100

                    # Calculate profit and loss for each day
                    dataset['PnL'] = shares * (dataset['Adj Close'].diff())

                    # Visualize the profit and loss
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=dataset.index, y=dataset['PnL'], mode='lines', name='Profit/Loss'))
                    fig.update_layout(title=f'Profit and Loss for {symbol} Each Day', xaxis_title='Date', yaxis_title='Profit/Loss')
                    st.plotly_chart(fig)

                    # Display financial analysis
                    st.write(f"Financial Analysis for {symbol}")
                    st.write('-' * 50)
                    st.write(f"Profit or Loss: ${profit_or_loss:.2f}")
                    st.write(f"Percentage Gain or Loss: {percentage_gain_or_loss:.2f}%")
                    st.write(f"Percentage of Returns: {percentage_returns:.2f}%")
                    st.write(f"Net Gains or Losses: {net_gains_or_losses:.2f}%")
                    st.write(f"Total Returns: {total_return:.2f}%")

                st.write ("This segment allows us to analyze the stock profit/loss returns")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio_one = st.number_input("Enter your initial investment")
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):

                    calculate_stock_profit_loss(ticker, start_date, end_date, portfolio_one)
                
            if pred_option_analysis == "Stock Return Statistical Analysis":
                def analyze_stock_returns(symbol, start, end):
                    # Download stock data
                    df = yf.download(symbol, start, end)

                    # Calculate daily returns
                    returns = df['Adj Close'].pct_change().dropna()
                    # Calculate and print various statistics
                    mean_return = np.mean(returns)
                    median_return = np.median(returns)
                    mode_return = stats.mode(returns)[0] #work on the mean more [0][0]
                    arithmetic_mean_return = returns.mean()
                    geometric_mean_return = stats.gmean(returns)
                    std_deviation = returns.std()
                    harmonic_mean_return = len(returns) / np.sum(1.0/returns)
                    skewness = stats.skew(returns)
                    kurtosis = stats.kurtosis(returns)
                    jarque_bera_results = stats.jarque_bera(returns)
                    is_normal = jarque_bera_results[1] > 0.05

                    st.write('Mean of returns:', mean_return)
                    st.write('Median of returns:', median_return)
                    st.write('Mode of returns:', mode_return)
                    st.write('Arithmetic average of returns:', arithmetic_mean_return)
                    st.write('Geometric mean of returns:', geometric_mean_return)
                    st.write('Standard deviation of returns:', std_deviation)
                    st.write('Harmonic mean of returns:', harmonic_mean_return)
                    st.write('Skewness:', skewness)
                    st.write('Kurtosis:', kurtosis)
                    st.write("Jarque-Bera p-value:", jarque_bera_results[1])
                    st.write('Are the returns normal?', is_normal)

                    # Histogram of returns
                    hist_fig = px.histogram(returns, nbins=30, title=f'Histogram of Returns for {symbol.upper()}')
                    st.plotly_chart(hist_fig)

                st.write ("This segment allows you to view stock returns using some statistcal methods")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):

                    analyze_stock_returns(ticker, start_date, end_date)

            if pred_option_analysis == "VAR Analysis":
                def calculate_var(stock, start, end):
                # Download data from Yahoo Finance
                    df = yf.download(stock, start, end)
                    
                    # Calculate daily returns
                    returns = df['Adj Close'].pct_change().dropna()

                    # VaR using historical bootstrap method
                    hist_fig = px.histogram(returns, nbins=40, title="Histogram of stock daily returns")
                    st.plotly_chart(hist_fig)

                    # VaR using variance-covariance method
                    tdf, tmean, tsigma = stats.t.fit(returns)
                    support = np.linspace(returns.min(), returns.max(), 100)
                    pdf = stats.t.pdf(support, loc=tmean, scale=tsigma, df=tdf)
                    cov_fig = go.Figure(go.Scatter(x=support, y=pdf, mode='lines', line=dict(color='red')))
                    cov_fig.update_layout(title="VaR using variance-covariance method")
                    st.plotly_chart(cov_fig)

                    # Calculate VaR using normal distribution at 95% confidence level
                    mean, sigma = returns.mean(), returns.std()
                    VaR = stats.norm.ppf(0.05, mean, sigma)
                    st.write("VaR using normal distribution at 95% confidence level:", VaR)

                st.write ("This segment allows you to view the average stock returns monthly")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                if st.button("Check"):
                    st.write(years)
                    calculate_var(ticker, start_date, end_date)


            if pred_option_analysis == "Stock Returns":
                def view_stock_returns(symbol, num_years):
                    # Fetch stock data for the given number of years
                    start_date = dt.date.today() - dt.timedelta(days=365 * num_years)
                    end_date = dt.date.today()
                    dataset = yf.download(symbol, start_date, end_date)
                    
                    # Plot Adjusted Close Price over time
                    fig_adj_close = go.Figure()
                    fig_adj_close.add_trace(go.Scatter(x=dataset.index, y=dataset['Adj Close'], mode='lines', name='Adj Close'))
                    fig_adj_close.update_layout(title=f'{symbol} Closing Price Chart', xaxis_title='Date', yaxis_title='Price', showlegend=True)

                    # Monthly Returns Analysis
                    monthly_dataset = dataset.asfreq('BM')
                    monthly_dataset['Returns'] = dataset['Adj Close'].pct_change().dropna()
                    monthly_dataset['Month_Name'] = monthly_dataset.index.strftime('%b-%Y')
                    monthly_dataset['ReturnsPositive'] = monthly_dataset['Returns'] > 0
                    colors = monthly_dataset['ReturnsPositive'].map({True: 'g', False: 'r'})
                    
                    fig_monthly_returns = px.bar(monthly_dataset, x=monthly_dataset.index, y='Returns', color=colors,
                                                labels={'x': 'Month', 'y': 'Returns'}, title='Monthly Returns')
                    fig_monthly_returns.update_xaxes(tickvals=monthly_dataset.index, ticktext=monthly_dataset['Month_Name'], tickangle=45)

                    # Yearly Returns Analysis
                    yearly_dataset = dataset.asfreq('BY')
                    yearly_dataset['Returns'] = dataset['Adj Close'].pct_change().dropna()
                    yearly_dataset['ReturnsPositive'] = yearly_dataset['Returns'] > 0
                    colors_year = yearly_dataset['ReturnsPositive'].map({True: 'g', False: 'r'})
                    
                    fig_yearly_returns = px.bar(yearly_dataset, x=yearly_dataset.index.year, y='Returns', color=colors_year,
                                                labels={'x': 'Year', 'y': 'Returns'}, title='Yearly Returns')

                    # Show the interactive plots
                    st.plotly_chart(fig_adj_close)
                    st.plotly_chart(fig_monthly_returns)
                    st.plotly_chart(fig_yearly_returns)

                st.write ("This segment allows you to view the average stock returns yearly")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                if st.button("Check"):
                    st.write(years)
                    view_stock_returns(ticker, years)
        


        elif option =='Technical Indicators':
            pred_option_Technical_Indicators = st.selectbox('Make a choice', [
                                                                    'Exponential Moving Average (EMA)',
                                                                    'EMA Volume',
                                                                    'Positive Volume Trend (PVT)',
                                                                    'Exponential Weighted Moving Average (EWMA)',
                                                                    'Weighted Smoothing Moving Average (WSMA)',
                                                                    'Z Score Indicator (Z Score)',
                                                                    'Absolute Price Oscillator (APO)',
                                                                    'Acceleration Bands',
                                                                    'Accumulation Distribution Line',
                                                                    'Aroon',
                                                                    'Aroon Oscillator',
                                                                    'Average Directional Index (ADX)',
                                                                    'Average True Range (ATR)',
                                                                    'Balance of Power',
                                                                    'Beta Indicator',
                                                                    'Bollinger Bands',
                                                                    'Bollinger Bandwidth',
                                                                    'Breadth Indicator',
                                                                    'Candle Absolute Returns',
                                                                    'GANN lines angles',
                                                                    'GMMA',
                                                                    'Moving Average Convergence Divergence (MACD)',
                                                                    'MA high low',
                                                                    'Price Volume Trend Indicator (PVI)',
                                                                    'Price Volume Trend (PVT)',
                                                                    'Rate of Change (ROC)',
                                                                    'Return on Investment (ROI)',
                                                                    'Relative Strength Index (RSI)',
                                                                    'RSI BollingerBands',
                                                                    'Simple Moving Average (SMA)',
                                                                    'Weighted Moving Average (WMA)',
                                                                    'Triangular Moving Average (TRIMA)',
                                                                    'Time-Weighted Average Price (TWAP)',
                                                                    'Volume Weighted Average Price (VWAP)',
                                                                    'Central Pivot Range (CPR)',
                                                                    'Chaikin Money Flow',
                                                                    'Chaikin Oscillator',
                                                                    'Commodity Channel Index (CCI)',
                                                                    'Correlation Coefficient',
                                                                    'Covariance',
                                                                    'Detrended Price Oscillator (DPO)',
                                                                    'Donchain Channel',
                                                                    'Double Exponential Moving Average (DEMA)',
                                                                    'Dynamic Momentum Index',
                                                                    'Ease of Movement',
                                                                    'Force Index',
                                                                    'Geometric Return Indicator',
                                                                    'Golden/Death Cross',
                                                                    'High Minus Low',
                                                                    'Hull Moving Average',
                                                                    'Keltner Channels',
                                                                    'Linear Regression',
                                                                    'Linear Regression Slope',
                                                                    'Linear Weighted Moving Average (LWMA)',
                                                                    'McClellan Oscillator',
                                                                    'Momentum',
                                                                    'Moving Average Envelopes',
                                                                    'Moving Average High/Low',
                                                                    'Moving Average Ribbon',
                                                                    'Moving Average Envelopes (MMA)',
                                                                    'Moving Linear Regression',
                                                                    'New Highs/New Lows',
                                                                    'Pivot Point',
                                                                    'Money Flow Index (MFI)',
                                                                    'Price Channels',
                                                                    'Price Relative',
                                                                    'Realized Volatility',
                                                                    'Relative Volatility Index',
                                                                    'Smoothed Moving Average',
                                                                    'Speed Resistance Lines',
                                                                    'Standard Deviation Volatility',
                                                                    'Stochastic RSI',
                                                                    'Stochastic Fast',
                                                                    'Stochastic Full',
                                                                    'Stochastic Slow',
                                                                    'Super Trend',
                                                                    'True Strength Index',
                                                                    'Ultimate Oscillator',
                                                                    'Variance Indicator',
                                                                    'Volume Price Confirmation Indicator',
                                                                    'Volume Weighted Moving Average (VWMA)'])

            if pred_option_Technical_Indicators == "Exponential Moving Average (EMA)":
                st.success("This program allows you to view the Exponential Moving Average of a stock ")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):
                        symbol = ticker
                        start = start_date
                        end = end_date

                        # Read data
                        df = yf.download(symbol, start, end)

                        n = 15
                        df["EMA"] = (
                            df["Adj Close"].ewm(ignore_na=False, span=n, min_periods=n, adjust=True).mean()
                        )

                        dfc = df.copy()
                        dfc["VolumePositive"] = dfc["Open"] < dfc["Adj Close"]
                        # dfc = dfc.dropna()
                        dfc = dfc.reset_index()
                        dfc["Date"] = mdates.date2num(dfc["Date"].tolist())
                        dfc["Date"] = pd.to_datetime(dfc["Date"])  # Convert Date column to datetime
                        dfc["Date"] = dfc["Date"].apply(mdates.date2num)

                        # Plotting Moving Average using Plotly
                        trace_adj_close = go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close')
                        trace_ema = go.Scatter(x=df.index, y=df["EMA"], mode='lines', name='EMA')
                        layout_ma = go.Layout(title="Stock Closing Price of " + str(n) + "-Day Exponential Moving Average",
                                            xaxis=dict(title="Date"), yaxis=dict(title="Price"))
                        fig_ma = go.Figure(data=[trace_adj_close, trace_ema], layout=layout_ma)

                        # Plotting Candlestick with EMA using Plotly
                        dfc = df.copy()
                        dfc["VolumePositive"] = dfc["Open"] < dfc["Adj Close"]

                        trace_candlestick = go.Candlestick(x=dfc.index,
                                                        open=dfc['Open'],
                                                        high=dfc['High'],
                                                        low=dfc['Low'],
                                                        close=dfc['Close'],
                                                        name='Candlestick')

                        trace_ema = go.Scatter(x=df.index, y=df["EMA"], mode='lines', name='EMA')


                        trace_volume = go.Bar(x=dfc.index, y=dfc['Volume'], marker=dict(color=dfc['VolumePositive'].map({True: 'green', False: 'red'})),
                                            name='Volume')

                        layout_candlestick = go.Layout(title="Stock " + symbol + " Closing Price",
                                                    xaxis=dict(title="Date", type='date', tickformat='%d-%m-%Y'),
                                                    yaxis=dict(title="Price"),
                                                    yaxis2=dict(title="Volume", overlaying='y', side='right'))
                        fig_candlestick = go.Figure(data=[trace_candlestick, trace_ema, trace_volume], layout=layout_candlestick)


                        # Display Plotly figures in Streamlit
                        st.plotly_chart(fig_ma)
                        st.warning("Click candlestick, EMA or Volume to tinker with the graph")
                        st.plotly_chart(fig_candlestick)                

            if pred_option_Technical_Indicators == "EMA Volume":
                st.success("This program allows you to view EMA But focusing on Volume of a stock ")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):
                        symbol = ticker
                        start = start_date
                        end = end_date

                        # Read data
                        df = yf.download(symbol, start, end)

                        n = 15
                        df["EMA"] = (
                            df["Adj Close"].ewm(ignore_na=False, span=n, min_periods=n, adjust=True).mean()
                        )

                        df["EMA"] = df["Adj Close"].ewm(span=n, adjust=False).mean()  # Recalculate EMA
                        df["VolumePositive"] = df["Open"] < df["Adj Close"]

                        # Create traces
                        trace_candlestick = go.Candlestick(x=df.index,
                                                        open=df['Open'],
                                                        high=df['High'],
                                                        low=df['Low'],
                                                        close=df['Close'],
                                                        name='Candlestick')

                        trace_volume = go.Bar(x=df.index, y=df['Volume'],
                                            marker=dict(color=df['VolumePositive'].map({True: 'green', False: 'red'})),
                                            name='Volume')

                        trace_ema = go.Scatter(x=df.index, y=df["EMA"], mode='lines', name='EMA', line=dict(color='green'))

                        # Create layout
                        layout = go.Layout(title="Stock " + symbol + " Closing Price",
                                        xaxis=dict(title="Date", type='date', tickformat='%d-%m-%Y'),
                                        yaxis=dict(title="Price"),
                                        yaxis2=dict(title="Volume", overlaying='y', side='right'))

                        # Create figure
                        fig = go.Figure(data=[trace_candlestick, trace_ema, trace_volume], layout=layout)

                        # Display Plotly figure in Streamlit
                        st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Exponential Weighted Moving Average (EWMA)":

                st.success("This program allows you to view the WMA But focusing on Volume of a stock ")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):
                        symbol = ticker
                        start = start_date
                        end = end_date
                        df = yf.download(symbol, start, end)

                        n = 7
                        df["EWMA"] = df["Adj Close"].ewm(ignore_na=False, min_periods=n - 1, span=n).mean()
                        # Plotting Candlestick with EWMA
                        fig_candlestick = go.Figure()

                        # Plot candlestick
                        fig_candlestick.add_trace(go.Candlestick(x=df.index,
                                                                open=df['Open'],
                                                                high=df['High'],
                                                                low=df['Low'],
                                                                close=df['Close'],
                                                                name='Candlestick'))
                        # Plot volume
                        volume_color = df['Open'] < df['Close']  # Color based on close > open
                        volume_color = volume_color.map({True: 'green', False: 'red'}) 
                        fig_candlestick.add_trace(go.Bar(x=df.index,
                                                        y=df['Volume'],
                                                        marker_color=volume_color,  
                                                        name='Volume'))

                        # Plot EWMA
                        fig_candlestick.add_trace(go.Scatter(x=df.index,
                                                            y=df['EWMA'],
                                                            mode='lines',
                                                            name='EWMA',
                                                            line=dict(color='red')))

                        # Update layout
                        fig_candlestick.update_layout(title="Stock " + symbol + " Closing Price",
                                                    xaxis=dict(title="Date"),
                                                    yaxis=dict(title="Price"),
                                                    yaxis2=dict(title="Volume", overlaying='y', side='right'),
                                                    legend=dict(yanchor="top", y=1, xanchor="left", x=0))

                        # Display Plotly figure in Streamlit
                        st.plotly_chart(fig_candlestick)

            if pred_option_Technical_Indicators == "GANN lines angles":

                st.success("This program allows you to view the GANN lines of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Line Chart
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))

                    # Add diagonal line
                    x_lim = [df.index[0], df.index[-1]]
                    y_lim = [df["Adj Close"].iloc[0], df["Adj Close"].iloc[-1]]
                    fig_line.add_trace(go.Scatter(x=x_lim, y=y_lim, mode='lines', line=dict(color='red'), name='45 degree'))

                    fig_line.update_layout(title="Stock of GANN Angles", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig_line)

                    # GANN Angles
                    angles = [82.5, 75, 71.25, 63.75, 45, 26.25, 18.75, 15, 7.5]

                    fig_gann = go.Figure()
                    fig_gann.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))

                    for angle in angles:
                        angle_radians = np.radians(angle)
                        y_values = np.tan(angle_radians) * np.arange(len(df))
                        fig_gann.add_trace(go.Scatter(x=df.index, y=y_values, mode='markers', name=str(angle)))

                    fig_gann.update_layout(title="Stock of GANN Angles", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig_gann)

                    # Candlestick with GANN Lines Angles
                    fig_candlestick = go.Figure()

                    # Candlestick
                    fig_candlestick.add_trace(go.Candlestick(x=df.index,
                                                            open=df['Open'],
                                                            high=df['High'],
                                                            low=df['Low'],
                                                            close=df['Close'],
                                                            name='Candlestick'))

                    # GANN Angles
                    for angle in angles:
                        angle_radians = np.radians(angle)
                        y_values = np.tan(angle_radians) * np.arange(len(df))
                        fig_candlestick.add_trace(go.Scatter(x=df.index, y=y_values, mode='markers', name=str(angle)))

                    # Volume
                    fig_candlestick.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color=np.where(df['Open'] < df['Close'], 'green', 'red')))

                    fig_candlestick.update_layout(title="Stock Closing Price", xaxis_title="Date", yaxis_title="Price", 
                                                yaxis2=dict(title="Volume", overlaying='y', side='right', tickformat=',.0f'))
                    st.plotly_chart(fig_candlestick)

            if pred_option_Technical_Indicators == "GMMA":

                st.success("This program allows you to view the GANN lines of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Short-term for EMA
                    df["EMA3"] = df["Adj Close"].ewm(span=3, adjust=False).mean()
                    df["EMA5"] = df["Adj Close"].ewm(span=5, adjust=False).mean()
                    df["EMA8"] = df["Adj Close"].ewm(span=8, adjust=False).mean()
                    df["EMA10"] = df["Adj Close"].ewm(span=10, adjust=False).mean()
                    df["EMA12"] = df["Adj Close"].ewm(span=12, adjust=False).mean()
                    df["EMA15"] = df["Adj Close"].ewm(span=15, adjust=False).mean()

                    # Long-term for EMA
                    df["EMA30"] = df["Adj Close"].ewm(span=30, adjust=False).mean()
                    df["EMA35"] = df["Adj Close"].ewm(span=35, adjust=False).mean()
                    df["EMA40"] = df["Adj Close"].ewm(span=40, adjust=False).mean()
                    df["EMA45"] = df["Adj Close"].ewm(span=45, adjust=False).mean()
                    df["EMA50"] = df["Adj Close"].ewm(span=50, adjust=False).mean()
                    df["EMA60"] = df["Adj Close"].ewm(span=60, adjust=False).mean()

                    EMA_Short = df[["EMA3", "EMA5", "EMA8", "EMA10", "EMA12", "EMA15"]]
                    EMA_Long = df[["EMA30", "EMA35", "EMA40", "EMA45", "EMA50", "EMA60"]]

                    # Short-term for SMA
                    df["SMA3"] = df["Adj Close"].rolling(window=3).mean()
                    df["SMA5"] = df["Adj Close"].rolling(window=5).mean()
                    df["SMA8"] = df["Adj Close"].rolling(window=8).mean()
                    df["SMA10"] = df["Adj Close"].rolling(window=10).mean()
                    df["SMA12"] = df["Adj Close"].rolling(window=12).mean()
                    df["SMA15"] = df["Adj Close"].rolling(window=15).mean()

                    # Long-term for SMA
                    df["SMA30"] = df["Adj Close"].rolling(window=30).mean()
                    df["SMA35"] = df["Adj Close"].rolling(window=35).mean()
                    df["SMA40"] = df["Adj Close"].rolling(window=40).mean()
                    df["SMA45"] = df["Adj Close"].rolling(window=45).mean()
                    df["SMA50"] = df["Adj Close"].rolling(window=50).mean()
                    df["SMA60"] = df["Adj Close"].rolling(window=60).mean()

                    SMA_Short = df[["SMA3", "SMA5", "SMA8", "SMA10", "SMA12", "SMA15"]]
                    SMA_Long = df[["SMA30", "SMA35", "SMA40", "SMA45", "SMA50", "SMA60"]]

                    # Plot EMA
                    fig_ema = go.Figure()
                    fig_ema.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    for col in EMA_Short.columns:
                        fig_ema.add_trace(go.Scatter(x=df.index, y=EMA_Short[col], mode='lines', name=col, line=dict(color='blue')))
                    for col in EMA_Long.columns:
                        fig_ema.add_trace(go.Scatter(x=df.index, y=EMA_Long[col], mode='lines', name=col, line=dict(color='orange')))
                    fig_ema.update_layout(title="Guppy Multiple Moving Averages of EMA", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig_ema)

                    # Plot SMA
                    fig_sma = go.Figure()
                    fig_sma.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    for col in SMA_Short.columns:
                        fig_sma.add_trace(go.Scatter(x=df.index, y=SMA_Short[col], mode='lines', name=col, line=dict(color='blue')))
                    for col in SMA_Long.columns:
                        fig_sma.add_trace(go.Scatter(x=df.index, y=SMA_Long[col], mode='lines', name=col, line=dict(color='orange')))
                    fig_sma.update_layout(title="Guppy Multiple Moving Averages of SMA", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig_sma)

                    st.warning("Untick the volume to view the candlesticks and the movement lines")

                    # Candlestick with GMMA
                    fig_candlestick = go.Figure()

                    # Candlestick
                    fig_candlestick.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Candlestick'))

                    # Plot EMA on Candlestick
                    for col in EMA_Short.columns:
                        fig_candlestick.add_trace(go.Scatter(x=df.index, y=EMA_Short[col], mode='lines', name=col, line=dict(color='orange')))
                    for col in EMA_Long.columns:
                        fig_candlestick.add_trace(go.Scatter(x=df.index, y=EMA_Long[col], mode='lines', name=col, line=dict(color='blue')))

                    # Volume
                    fig_candlestick.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color=np.where(df['Open'] < df['Close'], 'green', 'red')))

                    fig_candlestick.update_layout(title="Stock Closing Price", xaxis_title="Date", yaxis_title="Price",
                                                yaxis2=dict(title="Volume", overlaying='y', side='right', tickformat=',.0f'))  # Set tick format to not show in millions
                    st.plotly_chart(fig_candlestick)


            if pred_option_Technical_Indicators == "Moving Average Convergence Divergence (MACD)":
                st.success("This program allows you to view the GANN lines of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)
                    # Read data
                    df = yf.download(symbol, start, end)

                    df["macd"], df["macdsignal"], df["macdhist"] = ta.MACD(
                        df["Adj Close"], fastperiod=12, slowperiod=26, signalperiod=9
                    )
                    df = df.dropna()
                    df = add_all_ta_features(df, open="Open", high="High", low="Low", close="Close", volume="Volume")

                    # Line Chart
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig_line.add_hline(y=df["Adj Close"].mean(), line_dash="dash", line_color="red", name='Mean')

                    # Volume
                    fig_volume = go.Figure()
                    fig_volume.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color=df['Volume'].map(lambda x: 'green' if x > 0 else 'red')))
                    # MACD
                    fig_macd = go.Figure()
                    fig_macd.add_trace(go.Scatter(x=df.index, y=df["macd"], mode='lines', name='MACD'))
                    fig_macd.add_trace(go.Scatter(x=df.index, y=df["macdsignal"], mode='lines', name='Signal'))
                    fig_macd.add_trace(go.Bar(x=df.index, y=df["macdhist"], name='Histogram', marker_color=df['macdhist'].map(lambda x: 'green' if x > 0 else 'red')))

                    st.plotly_chart(fig_line)
                    st.plotly_chart(fig_volume)
                    st.plotly_chart(fig_macd)
                
            if pred_option_Technical_Indicators == "Money Flow Index (MFI)":
                st.success("This program allows you to view the GANN lines of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Money Flow Index (MFI)
                    def calculate_mfi(high, low, close, volume, period=14):
                        typical_price = (high + low + close) / 3
                        raw_money_flow = typical_price * volume
                        positive_flow = (raw_money_flow * (close > close.shift(1))).rolling(window=period).sum()
                        negative_flow = (raw_money_flow * (close < close.shift(1))).rolling(window=period).sum()
                        money_ratio = positive_flow / negative_flow
                        mfi = 100 - (100 / (1 + money_ratio))
                        return mfi

                    df["MFI"] = calculate_mfi(df["High"], df["Low"], df["Close"], df["Volume"])    
            
                    # Plot interactive chart for closing price
                    fig_close = go.Figure()
                    fig_close.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name="Close"))
                    fig_close.update_layout(
                        title="Interactive Chart for Closing Price",
                        xaxis=dict(title="Date"),
                        yaxis=dict(title="Price"),
                        legend=dict(x=0, y=1),
                    )

                    # Find min and max price
                    min_price = df["Close"].min()
                    max_price = df["Close"].max()

                    # Plot interactive chart for MFI
                    fig_mfi = go.Figure()
                    fig_mfi.add_trace(go.Scatter(x=df.index, y=df["MFI"], mode="lines", name="MFI"))
                    fig_mfi.update_layout(
                        title="Interactive Chart for Money Flow Index (MFI)",
                        xaxis=dict(title="Date"),
                        yaxis=dict(title="MFI"),
                        legend=dict(x=0, y=1),
                        shapes=[
                            dict(
                                type="line",
                                x0=df.index[0],
                                y0=min_price,
                                x1=df.index[-1],
                                y1=min_price,
                                line=dict(color="blue", width=1, dash="dash"),
                            ),
                            dict(
                                type="line",
                                x0=df.index[0],
                                y0=max_price,
                                x1=df.index[-1],
                                y1=max_price,
                                line=dict(color="red", width=1, dash="dash"),
                            ),
                        ],
                    )
                    
                    # Plot interactive chart
                    fig_main = go.Figure()

                    # Add closing price trace
                    fig_main.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name="Close"))

                    # Add MFI trace
                    fig_main.add_trace(go.Scatter(x=df.index, y=df["MFI"], mode="lines", name="MFI"))

                    # Update layout
                    fig_main.update_layout(
                        title="Interactive Chart with Money Flow Index (MFI)",
                        xaxis=dict(title="Date"),
                        yaxis=dict(title="Price"),
                        yaxis2=dict(title="MFI", overlaying="y", side="right"),
                        legend=dict(x=0, y=1),
                    )

                    # Show interactive chart
                    st.plotly_chart(fig_close)
                    st.plotly_chart(fig_mfi)
                    st.plotly_chart(fig_main) 


            if pred_option_Technical_Indicators == "MA high low":
                st.success("This program allows you to view the MA High/low of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    
                    # Read data
                    df = yf.download(symbol, start, end)

                    df["MA_High"] = df["High"].rolling(10).mean()
                    df["MA_Low"] = df["Low"].rolling(10).mean()
                    df = df.dropna()

                    # Moving Average Line Chart
                    fig1 = px.line(df, x=df.index, y=["Adj Close", "MA_High", "MA_Low"], title="Moving Average of High and Low for Stock")
                    fig1.update_xaxes(title_text="Date")
                    fig1.update_yaxes(title_text="Price")
                    st.plotly_chart(fig1)

                    # Candlestick with Moving Averages High and Low
                    fig2 = go.Figure(data=[go.Candlestick(x=df.index,
                                                        open=df['Open'],
                                                        high=df['High'],
                                                        low=df['Low'],
                                                        close=df['Adj Close'])])

                    fig2.add_trace(go.Scatter(x=df.index, y=df['MA_High'], mode='lines', name='MA High'))
                    fig2.add_trace(go.Scatter(x=df.index, y=df['MA_Low'], mode='lines', name='MA Low'))

                    fig2.update_layout(title="Candlestick with Moving Averages High and Low",
                                    xaxis_title="Date",
                                    yaxis_title="Price")

                    st.plotly_chart(fig2)
            if pred_option_Technical_Indicators == "Price Volume Trend Indicator (PVI)":
                st.success("This program allows you to visualize the PVI of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date  
                    # Read data
                    df = yf.download(symbol, start, end)

                    returns = df["Adj Close"].pct_change()
                    vol_increase = df["Volume"].shift(1) < df["Volume"]
                    pvi = pd.Series(data=np.nan, index=df["Adj Close"].index, dtype="float64")

                    pvi.iloc[0] = 1000
                    for i in range(1, len(pvi)):
                        if vol_increase.iloc[i]:
                            pvi.iloc[i] = pvi.iloc[i - 1] * (1.0 + returns.iloc[i])
                        else:
                            pvi.iloc[i] = pvi.iloc[i - 1]

                    pvi = pvi.replace([np.inf, -np.inf], np.nan).fillna(1000)

                    df["PVI"] = pd.Series(pvi)

                    # Line Chart with PVI
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig1.add_trace(go.Scatter(x=df.index, y=df["PVI"], mode='lines', name='Positive Volume Index'))

                    fig1.update_layout(title="Adj Close and Positive Volume Index (PVI) Over Time",
                                    xaxis_title="Date",
                                    yaxis_title="Price/PVI")

                    st.plotly_chart(fig1)

                    # Candlestick with PVI
                    dfc = df.copy()
                    dfc["VolumePositive"] = dfc["Open"] < dfc["Adj Close"]
                    dfc = dfc.reset_index()
                    dfc["Date"] = mdates.date2num(dfc["Date"].tolist())

                    fig2 = go.Figure()

                    # Candlestick chart
                    fig2.add_trace(go.Candlestick(x=dfc['Date'],
                                    open=dfc['Open'],
                                    high=dfc['High'],
                                    low=dfc['Low'],
                                    close=dfc['Adj Close'], name='Candlestick'))

                    # Volume bars
                    fig2.add_trace(go.Bar(x=dfc['Date'], y=dfc['Volume'], marker_color=dfc.VolumePositive.map({True: "green", False: "red"}), name='Volume'))

                    fig2.add_trace(go.Scatter(x=df.index, y=df["PVI"], mode='lines', name='Positive Volume Index', line=dict(color='green')))

                    fig2.update_layout(title="Candlestick Chart with Positive Volume Index (PVI)",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    xaxis_rangeslider_visible=False)

                    st.plotly_chart(fig2)

            if pred_option_Technical_Indicators == "Positive Volume Trend (PVT)":
                st.success("This program allows you to view the PVT trend of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    df = yf.download(symbol, start, end)

                    # Calculate Price Volume Trend (PVT)
                    df["Momentum_1D"] = (df["Adj Close"] - df["Adj Close"].shift(1)).fillna(0)
                    df["PVT"] = (df["Momentum_1D"] / df["Adj Close"].shift(1)) * df["Volume"]
                    df["PVT"] = df["PVT"] - df["PVT"].shift(1)
                    df["PVT"] = df["PVT"].fillna(0)

                    # Line Chart with PVT
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig1.add_trace(go.Scatter(x=df.index, y=df["PVT"], mode='lines', name='Price Volume Trend'))

                    fig1.update_layout(title="Adj Close and Price Volume Trend (PVT) Over Time",
                                    xaxis_title="Date",
                                    yaxis_title="Price/PVT")

                    st.plotly_chart(fig1)

                    # Candlestick with PVT
                    dfc = df.copy()
                    dfc["VolumePositive"] = dfc["Open"] < dfc["Adj Close"]
                    dfc = dfc.reset_index()
                    dfc["Date"] = mdates.date2num(dfc["Date"].tolist())

                    fig2 = go.Figure()

                    # Candlestick chart
                    fig2.add_trace(go.Candlestick(x=dfc['Date'],
                                    open=dfc['Open'],
                                    high=dfc['High'],
                                    low=dfc['Low'],
                                    close=dfc['Adj Close'], name='Candlestick'))

                    # Volume bars
                    fig2.add_trace(go.Bar(x=dfc['Date'], y=dfc['Volume'], marker_color=dfc.VolumePositive.map({True: "green", False: "red"}), name='Volume'))

                    fig2.add_trace(go.Scatter(x=df.index, y=df["PVT"], mode='lines', name='Price Volume Trend', line=dict(color='blue')))

                    fig2.update_layout(title="Candlestick Chart with Price Volume Trend (PVT)",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    xaxis_rangeslider_visible=False)

                    st.plotly_chart(fig2)

            if pred_option_Technical_Indicators == "Rate of Change (ROC)":
                st.success("This program allows you to view the ROC of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Rate of Change (ROC)
                    n = 12
                    df["ROC"] = ((df["Adj Close"] - df["Adj Close"].shift(n)) / df["Adj Close"].shift(n)) * 100

                    # Line Chart with ROC
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig1.add_trace(go.Scatter(x=df.index, y=df["ROC"], mode='lines', name='Rate of Change'))

                    fig1.update_layout(title="Adj Close and Rate of Change (ROC) Over Time",
                                    xaxis_title="Date",
                                    yaxis_title="Price/ROC")

                    st.plotly_chart(fig1)

                    # Candlestick with ROC
                    dfc = df.copy()
                    dfc["VolumePositive"] = dfc["Open"] < dfc["Adj Close"]
                    dfc = dfc.reset_index()
                    dfc["Date"] = mdates.date2num(dfc["Date"].tolist())

                    fig2 = go.Figure()

                    # Candlestick chart
                    fig2.add_trace(go.Candlestick(x=dfc['Date'],
                                    open=dfc['Open'],
                                    high=dfc['High'],
                                    low=dfc['Low'],
                                    close=dfc['Adj Close'], name='Candlestick'))

                    # Volume bars
                    fig2.add_trace(go.Bar(x=dfc['Date'], y=dfc['Volume'], marker_color=dfc.VolumePositive.map({True: "green", False: "red"}), name='Volume'))

                    fig2.add_trace(go.Scatter(x=df.index, y=df["ROC"], mode='lines', name='Rate of Change', line=dict(color='blue')))

                    fig2.update_layout(title="Candlestick Chart with Rate of Change (ROC)",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    xaxis_rangeslider_visible=False)

                    st.plotly_chart(fig2)

            if pred_option_Technical_Indicators == "Return on Investment (ROI)":
                st.success("This program allows you to view the ROI over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Return on Investment (ROI)
                    df["ROI"] = ((df["Adj Close"] - df["Adj Close"].shift(1)) / df["Adj Close"].shift(1) * 100)

                    # Line Chart with ROI
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig1.add_trace(go.Scatter(x=df.index, y=df["ROI"], mode='lines', name='Return on Investment'))

                    fig1.update_layout(title="Adj Close and Return on Investment (ROI) Over Time",
                                    xaxis_title="Date",
                                    yaxis_title="Price/ROI")

                    st.plotly_chart(fig1)

                    # Candlestick with ROI
                    dfc = df.copy()
                    dfc["VolumePositive"] = dfc["Open"] < dfc["Adj Close"]
                    dfc = dfc.reset_index()
                    dfc["Date"] = pd.to_datetime(dfc["Date"])
                    dfc["Date"] = dfc["Date"].apply(mdates.date2num)

                    fig2 = go.Figure()

                    # Candlestick chart
                    fig2.add_trace(go.Candlestick(x=dfc['Date'],
                                    open=dfc['Open'],
                                    high=dfc['High'],
                                    low=dfc['Low'],
                                    close=dfc['Adj Close'], name='Candlestick'))

                    # Volume bars
                    fig2.add_trace(go.Bar(x=dfc['Date'], y=dfc['Volume'], marker_color=dfc.VolumePositive.map({True: "green", False: "red"}), name='Volume'))

                    fig2.add_trace(go.Scatter(x=df.index, y=df["ROI"], mode='lines', name='Return on Investment', line=dict(color='red')))

                    fig2.update_layout(title="Candlestick Chart with Return on Investment (ROI)",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    xaxis_rangeslider_visible=False)

                    st.plotly_chart(fig2)

                    
            if pred_option_Technical_Indicators == "Relative Strength Index (RSI)":
                st.success("This program allows you to view the RSI over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    n = 14  # Number of period
                    change = df["Adj Close"].diff(1)
                    df["Gain"] = change.mask(change < 0, 0)
                    df["Loss"] = abs(change.mask(change > 0, 0))
                    df["AVG_Gain"] = df.Gain.rolling(n).mean()
                    df["AVG_Loss"] = df.Loss.rolling(n).mean()
                    df["RS"] = df["AVG_Gain"] / df["AVG_Loss"]
                    df["RSI"] = 100 - (100 / (1 + df["RS"]))

                    # Create RSI plot
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))

                    fig1.add_trace(go.Scatter(x=df.index, y=df["RSI"], mode='lines', name='Relative Strength Index'))

                    fig1.update_layout(title=symbol + " Closing Price and Relative Strength Index (RSI)",
                                    xaxis_title="Date",
                                    yaxis_title="Price/RSI")

                    st.plotly_chart(fig1)

                    # Candlestick with RSI
                    dfc = df.copy()
                    dfc["VolumePositive"] = dfc["Open"] < dfc["Adj Close"]
                    dfc = dfc.reset_index()
                    dfc["Date"] = pd.to_datetime(dfc["Date"])
                    dfc["Date"] = dfc["Date"].apply(mdates.date2num)

                    fig2 = go.Figure()

                    # Candlestick chart
                    fig2.add_trace(go.Candlestick(x=dfc['Date'],
                                    open=dfc['Open'],
                                    high=dfc['High'],
                                    low=dfc['Low'],
                                    close=dfc['Adj Close'], name='Candlestick'))

                    # Volume bars
                    fig2.add_trace(go.Bar(x=dfc['Date'], y=dfc['Volume'], marker_color=dfc.VolumePositive.map({True: "green", False: "red"}), name='Volume'))

                    fig2.add_trace(go.Scatter(x=df.index, y=df["RSI"], mode='lines', name='Relative Strength Index', line=dict(color='blue')))

                    fig2.update_layout(title=symbol + " Candlestick Chart with Relative Strength Index (RSI)",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    xaxis_rangeslider_visible=False)

                    st.plotly_chart(fig2)

            if pred_option_Technical_Indicators == "RSI BollingerBands":
                st.success("This program allows you to view the RSI with emphasis on BollingerBands over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Simple Line Chart
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig1.update_layout(title=symbol + " Closing Price", xaxis_title="Date", yaxis_title="Price")

                    st.plotly_chart(fig1)

                    # RSI
                    rsi = ta.RSI(df["Adj Close"], timeperiod=14)
                    rsi = rsi.dropna()

                    # Bollinger Bands
                    df["20 Day MA"] = df["Adj Close"].rolling(window=20).mean()
                    df["20 Day STD"] = df["Adj Close"].rolling(window=20).std()
                    df["Upper Band"] = df["20 Day MA"] + (df["20 Day STD"] * 2)
                    df["Lower Band"] = df["20 Day MA"] - (df["20 Day STD"] * 2)

                    fig2 = go.Figure()
                    fig2.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig2.add_trace(go.Scatter(x=df.index, y=df["20 Day MA"], mode='lines', name='20 Day MA'))
                    fig2.add_trace(go.Scatter(x=df.index, y=df["Upper Band"], mode='lines', name='Upper Band'))
                    fig2.add_trace(go.Scatter(x=df.index, y=df["Lower Band"], mode='lines', name='Lower Band'))
                    fig2.update_layout(title=f"30 Day Bollinger Band for {symbol.upper()}", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig2)

                    dfc = df.reset_index()
                    dfc["Date"] = pd.to_datetime(dfc["Date"])

                    # Candlestick with Bollinger Bands
                    fig3 = go.Figure()
                    fig3.add_trace(go.Candlestick(x=dfc['Date'],
                                    open=dfc['Open'],
                                    high=dfc['High'],
                                    low=dfc['Low'],
                                    close=dfc['Adj Close'], name='Candlestick'))

                    fig3.add_trace(go.Scatter(x=dfc['Date'], y=df["20 Day MA"], mode='lines', name='20 Day MA'))
                    fig3.add_trace(go.Scatter(x=dfc['Date'], y=df["Upper Band"], mode='lines', name='Upper Band'))
                    fig3.add_trace(go.Scatter(x=dfc['Date'], y=df["Lower Band"], mode='lines', name='Lower Band'))

                    fig3.update_layout(title=f"{symbol.upper()} Candlestick Chart with Bollinger Bands", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig3)

                    # Combine RSI and Bollinger Bands
                    fig4 = go.Figure()

                    fig4.add_trace(go.Scatter(x=df.index, y=df["20 Day MA"], mode='lines', name='20 Day MA'))
                    fig4.add_trace(go.Scatter(x=df.index, y=df["Upper Band"], mode='lines', name='Upper Band'))
                    fig4.add_trace(go.Scatter(x=df.index, y=df["Lower Band"], mode='lines', name='Lower Band'))

                    fig4.add_trace(go.Scatter(x=df.index, y=rsi, mode='lines', name='RSI'))

                    fig4.update_layout(title=f"Bollinger Bands & RSI for {symbol.upper()}", xaxis_title="Date", yaxis_title="Price/RSI")
                    st.plotly_chart(fig4)
                
            if pred_option_Technical_Indicators == "Volume Weighted Average Price (VWAP)":
                st.success("This program allows you to view the VWAP over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                
                    # Read data
                    df = yf.download(symbol, start, end)

                    def VWAP(df):
                        return (df["Adj Close"] * df["Volume"]).sum() / df["Volume"].sum()

                    n = 14
                    df["VWAP"] = pd.concat(
                        [
                            (pd.Series(VWAP(df.iloc[i : i + n]), index=[df.index[i + n]]))
                            for i in range(len(df) - n)
                        ]
                    )
                
                    vwap_series = pd.concat([(pd.Series(VWAP(df.iloc[i : i + n]), index=[df.index[i + n]])) for i in range(len(df) - n)])
                    vwap_series = vwap_series.dropna()


                    # Simple Line Chart
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig1.add_trace(go.Scatter(x=vwap_series.index, y=vwap_series, mode='lines', name='VWAP'))
                    fig1.update_layout(title="Volume Weighted Average Price for Stock", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig1)

                    # Candlestick with VWAP
                    df.loc[:, "VolumePositive"] = df["Open"] < df["Adj Close"]
                
                    df = df.dropna()
                    df = df.reset_index()
                    df["Date"] = pd.to_datetime(df["Date"])
                    df["Date"] = df["Date"].apply(mdates.date2num)

                    fig2 = go.Figure()

                    fig2.add_trace(go.Candlestick(x=df['Date'],
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Adj Close'], name='Candlestick'))

                    fig2.add_trace(go.Scatter(x=df['Date'], y=df["VWAP"], mode='lines', name='VWAP'))

                    fig2.update_layout(title=f"Stock {symbol} Closing Price with VWAP", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig2)

            if pred_option_Technical_Indicators == "Weighted Moving Average (WMA)":
                st.success("This program allows you to view the WMA over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                
                    # Read data
                    df = yf.download(symbol, start, end)

                    def WMA(data, n):
                        ws = np.zeros(data.shape[0])
                        t_sum = sum(range(1, n + 1))
                        for i in range(n - 1, data.shape[0]):
                            ws[i] = sum(data[i - n + 1 : i + 1] * np.linspace(1, n, n)) / t_sum
                        return ws

                    df["WMA"] = WMA(df["Adj Close"], 5)

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.add_trace(go.Scatter(x=df.index[4:], y=df["WMA"][4:], mode='lines', name='WMA'))
                    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color='#0079a3', opacity=0.4))

                    fig.update_layout(title=f'Stock {symbol} Closing Price', xaxis_title='Date', yaxis_title='Price')
                    st.plotly_chart(fig)

                    # Candlestick with WMA
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.add_trace(go.Scatter(x=df.index[4:], y=df["WMA"][4:], mode='lines', name='WMA'))

                    fig.update_layout(title=f'Stock {symbol} Candlestick Chart with WMA', xaxis_title='Date', yaxis_title='Price')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Weighted Smoothing Moving Average (WSMA)":
                st.success("This program allows you to view the WMA over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                
                    # Read data
                    df = yf.download(symbol, start, end)
                    
                    def WSMA(df, column="Adj Close", n=14):
                        ema = df[column].ewm(span=n, min_periods=n - 1).mean()
                        K = 1 / n
                        wsma = df[column] * K + ema * (1 - K)
                        return wsma

                    df["WSMA"] = WSMA(df, column="Adj Close", n=14)
                    df = df.dropna()

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["WSMA"], mode='lines', name="WSMA"))
                    fig.update_layout(title="Wilder's Smoothing Moving Average for Stock",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick with WSMA
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.add_trace(go.Scatter(x=df.index, y=df["WSMA"], mode='lines', name="WSMA"))

                    fig.update_layout(title=f"Stock {symbol} Candlestick Chart with WSMA",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)       
            if pred_option_Technical_Indicators == "Z Score Indicator (Z Score)":
                st.success("This program allows you to view the WMA over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                
                    # Read data
                    df = yf.download(symbol, start, end)
                
                    # Read data
                    df = yf.download(symbol, start, end)

                    from scipy.stats import zscore

                    df["z_score"] = zscore(df["Adj Close"])

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    # Z-Score Chart
                    fig.add_trace(go.Scatter(x=df.index, y=df["z_score"], mode='lines', name="Z-Score"))
                    fig.update_layout(title="Z-Score for " + symbol,
                                    xaxis_title="Date",
                                    yaxis_title="Z-Score",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick with Z-Score
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.add_trace(go.Scatter(x=df.index, y=df["z_score"], mode='lines', name="Z-Score"))
                    fig.update_layout(title="Stock " + symbol + " Candlestick Chart with Z-Score",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    
                    st.plotly_chart(fig)
            if pred_option_Technical_Indicators == "Absolute Price Oscillator (APO)":
                st.success("This program allows you to view the WMA over time of a ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    df["HL"] = (df["High"] + df["Low"]) / 2
                    df["HLC"] = (df["High"] + df["Low"] + df["Adj Close"]) / 3
                    df["HLCC"] = (df["High"] + df["Low"] + df["Adj Close"] + df["Adj Close"]) / 4
                    df["OHLC"] = (df["Open"] + df["High"] + df["Low"] + df["Adj Close"]) / 4

                    df["Long_Cycle"] = df["Adj Close"].rolling(20).mean()
                    df["Short_Cycle"] = df["Adj Close"].rolling(5).mean()
                    df["APO"] = df["Long_Cycle"] - df["Short_Cycle"]

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    # Absolute Price Oscillator (APO) Chart
                    fig.add_trace(go.Scatter(x=df.index, y=df["APO"], mode='lines', name="Absolute Price Oscillator", line=dict(color='green')))
                    fig.update_layout(title="Absolute Price Oscillator (APO) for " + symbol,
                                    xaxis_title="Date",
                                    yaxis_title="APO",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick with Absolute Price Oscillator (APO)
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.add_trace(go.Scatter(x=df.index, y=df["APO"], mode='lines', name="Absolute Price Oscillator", line=dict(color='green')))
                    fig.update_layout(title="Stock " + symbol + " Candlestick Chart with APO",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Acceleration Bands":
                st.success("This program allows you to view the Acclerations bands of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)
                

                    n = 7
                    UBB = df["High"] * (1 + 4 * (df["High"] - df["Low"]) / (df["High"] + df["Low"]))
                    df["Upper_Band"] = UBB.rolling(n, center=False).mean()
                    df["Middle_Band"] = df["Adj Close"].rolling(n).mean()
                    LBB = df["Low"] * (1 - 4 * (df["High"] - df["Low"]) / (df["High"] + df["Low"]))
                    df["Lower_Band"] = LBB.rolling(n, center=False).mean()

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Upper_Band"], mode='lines', name='Upper Band'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Middle_Band"], mode='lines', name='Middle Band'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Lower_Band"], mode='lines', name='Lower Band'))
                    fig.update_layout(title="Stock Closing Price of " + str(n) + "-Day Acceleration Bands",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick Chart
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.add_trace(go.Scatter(x=df.index, y=df["Upper_Band"], mode='lines', name='Upper Band'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Middle_Band"], mode='lines', name='Middle Band'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Lower_Band"], mode='lines', name='Lower Band'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price with Acceleration Bands",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    
                    st.plotly_chart(fig)


            if pred_option_Technical_Indicators == "Accumulation Distribution Line":
                st.success("This program allows you to view the ADL of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)
                    
                    df["MF Multiplier"] = (2 * df["Adj Close"] - df["Low"] - df["High"]) / (
                        df["High"] - df["Low"]
                    )
                    df["MF Volume"] = df["MF Multiplier"] * df["Volume"]
                    df["ADL"] = df["MF Volume"].cumsum()
                    df = df.drop(["MF Multiplier", "MF Volume"], axis=1)

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["ADL"], mode='lines', name='Accumulation Distribution Line'))
                    fig.update_layout(yaxis2=dict(title="Accumulation Distribution Line"))

                    fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name="Volume", marker_color='rgba(0, 0, 255, 0.4)'))
                    fig.update_layout(yaxis3=dict(title="Volume"))

                    st.plotly_chart(fig)

                    # Candlestick Chart
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["ADL"], mode='lines', name='Accumulation Distribution Line'))
                    fig.update_layout(yaxis2=dict(title="Accumulation Distribution Line"))

                    fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name="Volume", marker_color='rgba(0, 0, 255, 0.4)'))
                    fig.update_layout(yaxis3=dict(title="Volume"))

                    st.plotly_chart(fig)
                
            if pred_option_Technical_Indicators == "Aroon":
                st.success("This program allows you to view the Aroon of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    df = yf.download(symbol, start, end)

                    n = 25
                    high_max = lambda xs: np.argmax(xs[::-1])
                    low_min = lambda xs: np.argmin(xs[::-1])

                    df["Days since last High"] = (
                        df["High"]
                        .rolling(center=False, min_periods=0, window=n)
                        .apply(func=high_max)
                        .astype(int)
                    )

                    df["Days since last Low"] = (
                        df["Low"]
                        .rolling(center=False, min_periods=0, window=n)
                        .apply(func=low_min)
                        .astype(int)
                    )

                    df["Aroon_Up"] = ((25 - df["Days since last High"]) / 25) * 100
                    df["Aroon_Down"] = ((25 - df["Days since last Low"]) / 25) * 100

                    df = df.drop(["Days since last High", "Days since last Low"], axis=1)

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["Aroon_Up"], mode='lines', name='Aroon UP', line=dict(color='green')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Aroon_Down"], mode='lines', name='Aroon DOWN', line=dict(color='red')))
                    fig.update_layout(yaxis2=dict(title="Aroon"))

                    st.plotly_chart(fig)

                    # Candlestick Chart
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["Aroon_Up"], mode='lines', name='Aroon UP', line=dict(color='green')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Aroon_Down"], mode='lines', name='Aroon DOWN', line=dict(color='red')))
                    fig.update_layout(yaxis2=dict(title="Aroon"))

                    st.plotly_chart(fig)


            if pred_option_Technical_Indicators == "Aroon Oscillator":
                st.success("This program allows you to view the Aroon Oscillator bands of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    n = 25
                    high_max = lambda xs: np.argmax(xs[::-1])
                    low_min = lambda xs: np.argmin(xs[::-1])

                    df["Days since last High"] = (
                        df["High"]
                        .rolling(center=False, min_periods=0, window=n)
                        .apply(func=high_max)
                        .astype(int)
                    )

                    df["Days since last Low"] = (
                        df["Low"]
                        .rolling(center=False, min_periods=0, window=n)
                        .apply(func=low_min)
                        .astype(int)
                    )

                    df["Aroon_Up"] = ((25 - df["Days since last High"]) / 25) * 100
                    df["Aroon_Down"] = ((25 - df["Days since last Low"]) / 25) * 100

                    df["Aroon_Oscillator"] = df["Aroon_Up"] - df["Aroon_Down"]

                    df = df.drop(
                        ["Days since last High", "Days since last Low", "Aroon_Up", "Aroon_Down"], axis=1
                    )

                    # Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["Aroon_Oscillator"], mode='lines', name='Aroon Oscillator', line=dict(color='green')))
                    fig.add_trace(go.Scatter(x=df.index, y=[0]*len(df), mode='lines', name='Zero Line', line=dict(color='red', dash='dash')))
                    st.plotly_chart(fig)

                    # Bar Chart
                    fig = go.Figure()
                    df["Positive"] = df["Aroon_Oscillator"] > 0
                    fig.add_trace(go.Bar(x=df.index, y=df["Aroon_Oscillator"], marker_color=df.Positive.map({True: "green", False: "red"})))
                    fig.add_shape(type="line", x0=df.index[0], y0=0, x1=df.index[-1], y1=0, line=dict(color="red", width=1, dash="dash"))

                    fig.update_layout(title="Aroon Oscillator",
                                    xaxis_title="Date",
                                    yaxis_title="Aroon Oscillator",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    st.plotly_chart(fig)

                    # Candlestick Chart
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["Aroon_Oscillator"], mode='lines', name='Aroon Oscillator', line=dict(color='green')))
                    fig.add_trace(go.Scatter(x=df.index, y=[0]*len(df), mode='lines', name='Zero Line', line=dict(color='red', dash='dash')))
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Average Directional Index (ADX)":
                st.success("This program allows you to view the ADX  of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Simple Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    st.plotly_chart(fig)

                    # ADX calculation
                    adx = ta.ADX(df["High"], df["Low"], df["Adj Close"], timeperiod=14)
                    adx = adx.dropna()

                    # Line Chart with ADX
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=adx.index, y=adx, mode='lines', name='ADX'))
                    fig.add_shape(type="line", x0=adx.index[0], y0=20, x1=adx.index[-1], y1=20, line=dict(color="red", width=1, dash="dash"))
                    fig.add_shape(type="line", x0=adx.index[0], y0=50, x1=adx.index[-1], y1=50, line=dict(color="red", width=1, dash="dash"))
                    st.plotly_chart(fig)

                    # Candlestick Chart with ADX
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.update_layout(title="Stock " + symbol + " Candlestick Chart with ADX",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=adx.index, y=adx, mode='lines', name='ADX'))
                    fig.add_shape(type="line", x0=adx.index[0], y0=20, x1=adx.index[-1], y1=20, line=dict(color="red", width=1, dash="dash"))
                    fig.add_shape(type="line", x0=adx.index[0], y0=50, x1=adx.index[-1], y1=50, line=dict(color="red", width=1, dash="dash"))
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Average True Range (ATR)":
                st.success("This program allows you to view the ATR of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)
        
                    n = 14
                    df["HL"] = df["High"] - df["Low"]
                    df["HC"] = abs(df["High"] - df["Adj Close"].shift())
                    df["LC"] = abs(df["Low"] - df["Adj Close"].shift())
                    df["TR"] = df[["HL", "HC", "LC"]].max(axis=1)
                    df["ATR"] = df["TR"].rolling(n).mean()
                    df = df.drop(["HL", "HC", "LC", "TR"], axis=1)

                    # Simple Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # ATR Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["ATR"], mode='lines', name='ATR'))
                    fig.add_shape(type="line", x0=df.index[0], y0=1, x1=df.index[-1], y1=1, line=dict(color="black", width=1, dash="dash"))
                    fig.update_layout(title="Average True Range (ATR)",
                                    xaxis_title="Date",
                                    yaxis_title="ATR",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    
                    st.plotly_chart(fig)

                    # Candlestick Chart with ATR
                    fig = go.Figure()

                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.update_layout(title="Stock " + symbol + " Candlestick Chart with ATR",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["ATR"], mode='lines', name='ATR'))
                    fig.add_shape(type="line", x0=df.index[0], y0=1, x1=df.index[-1], y1=1, line=dict(color="black", width=1, dash="dash"))
                    
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Balance of Power":
                st.success("This program allows you to view the BoP of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    df["BOP"] = (df["Adj Close"] - df["Open"]) / (df["High"] - df["Low"])

                    # Simple Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.add_trace(go.Scatter(x=df.index, y=[df["Adj Close"].mean()] * len(df), mode='lines', name='Mean', line=dict(color='red')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Low"], mode='lines', name='Low', line=dict(color='blue', dash='dash')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["High"], mode='lines', name='High', line=dict(color='red', dash='dash')))
                    fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name='Volume', marker_color='#0079a3', opacity=0.4))

                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # BOP Bar Chart
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=df.index, y=df["BOP"], name='Balance of Power', marker_color=df["BOP"].apply(lambda x: 'green' if x >= 0 else 'red')))
                    fig.update_layout(title="Balance of Power",
                                    xaxis_title="Date",
                                    yaxis_title="BOP",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick Chart with BOP
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["BOP"], mode='lines', name='Balance of Power', line=dict(color='black')))
                    fig.update_layout(title="Stock " + symbol + " Candlestick Chart with BOP",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Beta Indicator":
                st.success("This program allows you to view the Beta Indicator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    market = "^GSPC"
                    # Read data
                    df = yf.download(symbol, start, end)
                    mk = yf.download(market, start, end)

                    df["Returns"] = df["Adj Close"].pct_change().dropna()
                    mk["Returns"] = mk["Adj Close"].pct_change().dropna()

                    n = 5
                    covar = df["Returns"].rolling(n).cov(mk["Returns"])
                    variance = mk["Returns"].rolling(n).var()
                    df["Beta"] = covar / variance

                    # Stock Closing Price Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.update_layout(title="Stock " + symbol + " Closing Price",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    st.plotly_chart(fig)

                    # Beta Line Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Beta"], mode='lines', name='Beta', line=dict(color='red')))
                    fig.update_layout(title="Beta",
                                    xaxis_title="Date",
                                    yaxis_title="Beta")
                    st.plotly_chart(fig)

                    # Candlestick Chart with Beta
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))
                    fig.update_layout(title="Stock " + symbol + " Candlestick Chart with Beta",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    fig.add_trace(go.Scatter(x=df.index, y=df["Beta"], mode='lines', name='Beta', line=dict(color='red')))
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Bollinger Bands":
                st.success("This program allows you to view the Acclerations bands of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                
                    # Read data
                    df = yf.download(symbol, start, end)
                    df["VolumePositive"] = df["Open"] < df["Adj Close"]

                    n = 20
                    MA = pd.Series(df["Adj Close"].rolling(n).mean())
                    STD = pd.Series(df["Adj Close"].rolling(n).std())
                    bb1 = MA + 2 * STD
                    df["Upper Bollinger Band"] = pd.Series(bb1)
                    bb2 = MA - 2 * STD
                    df["Lower Bollinger Band"] = pd.Series(bb2)

                    # Bollinger Bands Plot
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Upper Bollinger Band"], mode='lines', name='Upper Bollinger Band', line=dict(color='red')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Lower Bollinger Band"], mode='lines', name='Lower Bollinger Band', line=dict(color='blue')))
                    fig.update_layout(title=f"{symbol} Bollinger Bands",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    st.plotly_chart(fig)

                    # Candlestick Chart with Bollinger Bands
                    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick')])
                    fig.add_trace(go.Scatter(x=df.index, y=df["Upper Bollinger Band"], mode='lines', name='Upper Bollinger Band', line=dict(color='red')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Lower Bollinger Band"], mode='lines', name='Lower Bollinger Band', line=dict(color='blue')))
                    fig.update_layout(title="Candlestick Chart with Bollinger Bands",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    st.plotly_chart(fig)

                    # Volume Chart
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name='Volume', marker_color=df.VolumePositive.map({True: "green", False: "red"})))
                    fig.update_layout(title="Volume",
                                    xaxis_title="Date",
                                    yaxis_title="Volume")
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Bollinger Bandwidth":
                st.success("This program allows you to view the Bollinger bandwidth of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    n = 20
                    MA = pd.Series(df["Adj Close"].rolling(n).mean())
                    STD = pd.Series(df["Adj Close"].rolling(n).std())
                    bb1 = MA + 2 * STD
                    df["Upper Bollinger Band"] = pd.Series(bb1)
                    bb2 = MA - 2 * STD
                    df["Lower Bollinger Band"] = pd.Series(bb2)
                    df["SMA"] = df["Adj Close"].rolling(n).mean()

                    df["BBWidth"] = ((df["Upper Bollinger Band"] - df["Lower Bollinger Band"]) / df["SMA"] * 100)

                    # Bollinger Bands Plot
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Upper Bollinger Band"], mode='lines', name='Upper Bollinger Band', line=dict(color='red')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Lower Bollinger Band"], mode='lines', name='Lower Bollinger Band', line=dict(color='blue')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"].rolling(20).mean(), mode='lines', name='Mean Average', line=dict(color='orange', dash='dash')))
                    fig.update_layout(title=f"{symbol} Bollinger Bands",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    st.plotly_chart(fig)

                    # BB Width Plot
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["BBWidth"], mode='lines', name='BB Width', line=dict(color='black')))
                    fig.add_trace(go.Scatter(x=df.index, y=df["BBWidth"].rolling(20).mean(), mode='lines', name='200 Moving Average', line=dict(color='darkblue')))
                    fig.update_layout(title="Bollinger Bands Width",
                                    xaxis_title="Date",
                                    yaxis_title="BB Width")
                    st.plotly_chart(fig)



            if pred_option_Technical_Indicators == "Breadth Indicator":
                st.success("This program allows you to view the Breadth Indicator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
            
                    # Read data
                    df = yf.download(symbol, start, end)

                    #df["Adj Close"][1:]

                    # ## On Balance Volume
                    OBV = ta.OBV(df["Adj Close"], df["Volume"])

                    Advances = q.get("URC/NYSE_ADV", start_date="2017-07-27")["Numbers of Stocks"]
                    Declines = q.get("URC/NYSE_DEC", start_date="2017-07-27")["Numbers of Stocks"]

                    adv_vol = q.get("URC/NYSE_ADV_VOL", start_date="2017-07-27")["Numbers of Stocks"]
                    dec_vol = q.get("URC/NYSE_DEC_VOL", start_date="2017-07-27")["Numbers of Stocks"]

                    data = pd.DataFrame()
                    data["Advances"] = Advances
                    data["Declines"] = Declines
                    data["adv_vol"] = adv_vol
                    data["dec_vol"] = dec_vol

                    data["Net_Advances"] = data["Advances"] - data["Declines"]
                    data["Ratio_Adjusted"] = (
                        data["Net_Advances"] / (data["Advances"] + data["Declines"])
                    ) * 1000
                    data["19_EMA"] = ta.EMA(data["Ratio_Adjusted"], timeperiod=19)
                    data["39_EMA"] = ta.EMA(data["Ratio_Adjusted"], timeperiod=39)
                    data["RANA"] = (
                        (data["Advances"] - data["Declines"]) / (data["Advances"] + data["Declines"]) * 1000
                    )

                    # Finding the TRIN Value
                    data["ad_ratio"] = data["Advances"].divide(data["Declines"])  # AD Ratio
                    data["ad_vol"] = data["adv_vol"].divide(data["dec_vol"])  # AD Volume Ratio
                    data["TRIN"] = data["ad_ratio"].divide(data["adv_vol"])  # TRIN Value

                    # Function to calculate Force Index
                    def ForceIndex(data, n):
                        ForceIndex = pd.Series(df["Adj Close"].diff(n) * df["Volume"], name="ForceIndex")
                        data = data.join(ForceIndex)
                        return data

                    # Calculate Force Index
                    n = 10
                    ForceIndex = ForceIndex(df, n)
                    ForceIndex = ForceIndex["ForceIndex"]

                    # Market Price Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Close Price'))
                    fig.update_layout(title="Market Price Chart",
                                    xaxis_title="Date",
                                    yaxis_title="Close Price")
                    st.plotly_chart(fig)

                    # Force Index
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=ForceIndex, mode='lines', name='Force Index'))
                    fig.update_layout(title="Force Index",
                                    xaxis_title="Date",
                                    yaxis_title="Force Index")
                    st.plotly_chart(fig)


                    # Function to calculate Chaikin Oscillator
                    def Chaikin(data):
                        money_flow_volume = (
                            (2 * data["Adj Close"] - data["High"] - data["Low"])
                            / (data["High"] - data["Low"])
                            * data["Volume"]
                        )
                        ad = money_flow_volume.cumsum()
                        Chaikin = pd.Series(
                            ad.ewm(com=(3 - 1) / 2).mean() - ad.ewm(com=(10 - 1) / 2).mean(), name="Chaikin"
                        )
                        #data["Chaikin"] = data.join(Chaikin)
                        data["Chaikin"] = Chaikin
                        return data


                    # Calculate Chaikin Oscillator
                    Chaikin(df)
                

                    # Chaikin Oscillator Plot
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Chaikin"], mode='lines', name='Chaikin Oscillator'))
                    fig.update_layout(title="Chaikin Oscillator",
                                    xaxis_title="Date",
                                    yaxis_title="Chaikin Oscillator")
                    
                    st.plotly_chart(fig)


                    # Calculate Cumulative Volume Index
                    data["CVI"] = data["Net_Advances"].shift(1) + (data["Advances"] - data["Declines"])

                    # Cumulative Volume Index Plot
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=data.index, y=data["CVI"], mode='lines', name='Cumulative Volume Index'))
                    fig.update_layout(title="Cumulative Volume Index",
                                    xaxis_title="Date",
                                    yaxis_title="CVI")
                    
                    st.plotly_chart(fig)


            if pred_option_Technical_Indicators == "Candle Absolute Returns":
                st.success("This program allows you to view the Candle absolute returns  of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
            
                    # Read data
                    df = yf.download(symbol, start, end)
                    df["Absolute_Return"] = (
                        100 * (df["Adj Close"] - df["Adj Close"].shift(1)) / df["Adj Close"].shift(1)
                    )

                    # Plot the closing price
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode="lines", name="Closing Price"))
                    fig.update_layout(title="Stock " + symbol + " Closing Price", xaxis_title="Date", yaxis_title="Price")
                    st.plotly_chart(fig)

                    # Plot the Absolute Return
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Absolute_Return"], mode="lines", name="Absolute Return", line=dict(color="red")))
                    fig.update_layout(title="Absolute Return", xaxis_title="Date", yaxis_title="Absolute Return")
                    
                    st.plotly_chart(fig)
            if pred_option_Technical_Indicators == "Central Pivot Range (CPR)":
                st.success("This program allows you to view the CPR of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate CPR
                    df["Pivot"] = (df["High"] + df["Low"] + df["Adj Close"]) / 3.0
                    df["BC"] = (df["High"] + df["Low"]) / 2.0
                    df["TC"] = (df["Pivot"] - df["BC"]) + df["Pivot"]

                    # Plot candlestick with CPR
                    candlestick = go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Close'],
                                                name='Candlestick')

                    pivot = go.Scatter(x=df.index, y=df["Pivot"], mode='lines', name='Pivot')
                    bc = go.Scatter(x=df.index, y=df["BC"], mode='lines', name='BC')
                    tc = go.Scatter(x=df.index, y=df["TC"], mode='lines', name='TC')

                    data = [candlestick, pivot, bc, tc]

                    layout = go.Layout(title=f'Stock {symbol} Closing Price with Central Pivot Range (CPR)',
                                    xaxis=dict(title='Date'),
                                    yaxis=dict(title='Price'),
                                    showlegend=True)

                    fig = go.Figure(data=data, layout=layout)
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Chaikin Money Flow":
                st.success("This program allows you to view the Chaikin Money Flow (CMF) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate CMF
                    n = 20
                    df["MF_Multiplier"] = (2 * df["Adj Close"] - df["Low"] - df["High"]) / (df["High"] - df["Low"])
                    df["MF_Volume"] = df["MF_Multiplier"] * df["Volume"]
                    df["CMF"] = df["MF_Volume"].rolling(n).sum() / df["Volume"].rolling(n).sum()
                    df = df.drop(["MF_Multiplier", "MF_Volume"], axis=1)

                    # Plot CMF
                    cmf_chart = go.Scatter(x=df.index, y=df["CMF"], mode='lines', name='Chaikin Money Flow')

                    layout = go.Layout(title=f'Chaikin Money Flow for Stock {symbol}',
                                    xaxis=dict(title='Date'),
                                    yaxis=dict(title='CMF'),
                                    showlegend=True)

                    fig = go.Figure(data=[cmf_chart], layout=layout)
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Chaikin Oscillator":
                st.success("This program allows you to view the Chaikin Oscillator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Chaikin Oscillator
                    df["MF_Multiplier"] = (2 * df["Adj Close"] - df["Low"] - df["High"]) / (df["High"] - df["Low"])
                    df["MF_Volume"] = df["MF_Multiplier"] * df["Volume"]
                    df["ADL"] = df["MF_Volume"].cumsum()
                    df["ADL_3_EMA"] = df["ADL"].ewm(ignore_na=False, span=3, min_periods=2, adjust=True).mean()
                    df["ADL_10_EMA"] = df["ADL"].ewm(ignore_na=False, span=10, min_periods=9, adjust=True).mean()
                    df["Chaikin_Oscillator"] = df["ADL_3_EMA"] - df["ADL_10_EMA"]
                    df = df.drop(["MF_Multiplier", "MF_Volume", "ADL", "ADL_3_EMA", "ADL_10_EMA"], axis=1)

                    # Plot Chaikin Oscillator
                    co_chart = go.Scatter(x=df.index, y=df["Chaikin_Oscillator"], mode='lines', name='Chaikin Oscillator')

                    layout = go.Layout(title=f'Chaikin Oscillator for Stock {symbol}',
                                    xaxis=dict(title='Date'),
                                    yaxis=dict(title='Chaikin Oscillator'),
                                    showlegend=True)

                    fig = go.Figure(data=[co_chart], layout=layout)
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Commodity Channel Index (CCI)":
                st.success("This program allows you to view the Commodity Channel Index (CCI) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate CCI
                    n = 20
                    df["TP"] = (df["High"] + df["Low"] + df["Adj Close"]) / 3
                    df["SMA_TP"] = df["TP"].rolling(n).mean()
                    df["SMA_STD"] = df["TP"].rolling(n).std()
                    df["CCI"] = (df["TP"] - df["SMA_TP"]) / (0.015 * df["SMA_STD"])
                    df = df.drop(["TP", "SMA_TP", "SMA_STD"], axis=1)

                    # Plot CCI
                    cci_chart = go.Scatter(x=df.index, y=df["CCI"], mode='lines', name='Commodity Channel Index (CCI)')

                    layout = go.Layout(title=f'Commodity Channel Index (CCI) for Stock {symbol}',
                                    xaxis=dict(title='Date'),
                                    yaxis=dict(title='CCI'),
                                    showlegend=True)

                    fig = go.Figure(data=[cci_chart], layout=layout)
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Correlation Coefficient":
                st.success("This program allows you to view the Correlation Coefficient between two tickers over time")
                symbol1 = st.text_input("Enter the first ticker")
                symbol2 = st.text_input("Enter the second ticker")
                if symbol1 and symbol2:
                    message = (f"Tickers captured : {symbol1}, {symbol2}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    start = start_date
                    end = end_date

                    # Read data
                    df1 = yf.download(symbol1, start, end)
                    df2 = yf.download(symbol2, start, end)

                    # Calculate correlation coefficient
                    cc = df1["Adj Close"].corr(df2["Adj Close"])

                    # Plot correlation coefficient
                    cc_chart = go.Scatter(x=df1.index, y=cc, mode='lines', name='Correlation Coefficient')

                    layout = go.Layout(title=f'Correlation Coefficient between {symbol1} and {symbol2}',
                                    xaxis=dict(title='Date'),
                                    yaxis=dict(title='Correlation Coefficient'),
                                    showlegend=True)

                    fig = go.Figure(data=[cc_chart], layout=layout)
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Covariance":
                st.success("This program allows you to view the Covariance between two tickers over time")
                symbol1 = st.text_input("Enter the first ticker")
                symbol2 = st.text_input("Enter the second ticker")
                if symbol1 and symbol2:
                    message = (f"Tickers captured : {symbol1}, {symbol2}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    start = start_date
                    end = end_date

                    # Read data
                    df1 = yf.download(symbol1, start, end)
                    df2 = yf.download(symbol2, start, end)

                    # Calculate covariance
                    c = df1["Adj Close"].cov(df2["Adj Close"])

                    # Plot covariance
                    cov_chart = go.Scatter(x=df1.index, y=c, mode='lines', name='Covariance')

                    layout = go.Layout(title=f'Covariance between {symbol1} and {symbol2}',
                                    xaxis=dict(title='Date'),
                                    yaxis=dict(title='Covariance'),
                                    showlegend=True)

                    fig = go.Figure(data=[cov_chart], layout=layout)
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Detrended Price Oscillator (DPO)":
                st.success("This program allows you to view the Detrended Price Oscillator (DPO) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    n = 15
                    df["DPO"] = (df["Adj Close"].shift(int((0.5 * n) + 1)) - df["Adj Close"].rolling(n).mean())

                    # Plot DPO
                    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                                        open=df['Open'],
                                                        high=df['High'],
                                                        low=df['Low'],
                                                        close=df['Adj Close'],
                                                        name='Candlestick'),
                                        go.Scatter(x=df.index,
                                                    y=df['DPO'],
                                                    mode='lines',
                                                    name='DPO')])
                    fig.update_layout(title=f"Detrended Price Oscillator (DPO) for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Donchian Channel":
                st.success("This program allows you to view the Donchian Channel of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df["Upper_Channel_Line"] = pd.Series.rolling(df["High"], window=20).max()
                    df["Lower_Channel_Line"] = pd.Series.rolling(df["Low"], window=20).min()
                    df["Middle_Channel_Line"] = (df["Upper_Channel_Line"] + df["Lower_Channel_Line"]) / 2
                    df = df.dropna()

                    # Plot Donchian Channel
                    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                                        open=df['Open'],
                                                        high=df['High'],
                                                        low=df['Low'],
                                                        close=df['Adj Close'],
                                                        name='Candlestick'),
                                        go.Scatter(x=df.index,
                                                    y=df['Upper_Channel_Line'],
                                                    mode='lines',
                                                    name='Upper Channel Line'),
                                        go.Scatter(x=df.index,
                                                    y=df['Lower_Channel_Line'],
                                                    mode='lines',
                                                    name='Lower Channel Line'),
                                        go.Scatter(x=df.index,
                                                    y=df['Middle_Channel_Line'],
                                                    mode='lines',
                                                    name='Middle Channel Line')])
                    fig.update_layout(title=f"Donchian Channel for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Double Exponential Moving Average (DEMA)":
                st.success("This program allows you to view the Double Exponential Moving Average (DEMA) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df["EMA"] = ta.EMA(df["Adj Close"], timeperiod=5)
                    df["EMA_S"] = ta.EMA(df["EMA"], timeperiod=5)
                    df["DEMA"] = (2 * df["EMA"]) - df["EMA_S"]

                    # Plot DEMA
                    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                                        open=df['Open'],
                                                        high=df['High'],
                                                        low=df['Low'],
                                                        close=df['Adj Close'],
                                                        name='Candlestick'),
                                        go.Scatter(x=df.index,
                                                    y=df['DEMA'],
                                                    mode='lines',
                                                    name='DEMA')])
                    fig.update_layout(title=f"Double Exponential Moving Average (DEMA) for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Dynamic Momentum Index":
                st.success("This program allows you to view the Dynamic Momentum Index (DMI) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df["sd"] = df["Adj Close"].rolling(5).std()
                    df["asd"] = df["sd"].rolling(10).mean()
                    df["DMI"] = 14 / (df["sd"] / df["asd"])
                    df = df.drop(["sd", "asd"], axis=1)

                    # Plot DMI
                    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                                        open=df['Open'],
                                                        high=df['High'],
                                                        low=df['Low'],
                                                        close=df['Adj Close'],
                                                        name='Candlestick'),
                                        go.Scatter(x=df.index,
                                                    y=df['DMI'],
                                                    mode='lines',
                                                    name='Dynamic Momentum Index')])
                    fig.update_layout(title=f"Dynamic Momentum Index (DMI) for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Ease of Movement":
                st.success("This program allows you to view the Ease of Movement (EVM) indicator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)
                    # Create a function for Ease of Movement
                    def EVM(data, ndays):
                        dm = ((data["High"] + data["Low"]) / 2) - (
                            (data["High"].shift(1) + data["Low"].shift(1)) / 2
                        )
                        br = (data["Volume"] / 100000000) / ((data["High"] - data["Low"]))
                        EVM = dm / br
                        EVM_MA = pd.Series(EVM.rolling(ndays).mean(), name="EVM")
                        data = data.join(EVM_MA)
                        return data

                    # Compute the 14-day Ease of Movement for stock
                    n = 14
                    Stock_EVM = EVM(df, n)
                    EVM = Stock_EVM["EVM"]

                    # Compute EVM
                    df = EVM(df, 14)

                    # Plot EVM
                    fig = go.Figure(data=[
                        go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Adj Close'],
                                    name='Candlestick'),
                        go.Scatter(x=df.index,
                                y=df['EVM'],
                                mode='lines',
                                name='Ease of Movement')
                    ])
                    fig.update_layout(title=f"Ease of Movement (EVM) for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Force Index":
                st.success("This program allows you to view the Force Index of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    n = 13
                    df["FI_1"] = (df["Adj Close"] - df["Adj Close"].shift()) * df["Volume"]
                    df["FI_13"] = df["FI_1"].ewm(ignore_na=False, span=n, min_periods=n, adjust=True).mean()

                    # Plot Force Index
                    fig = go.Figure(data=[
                        go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Adj Close'],
                                    name='Candlestick'),
                        go.Scatter(x=df.index,
                                y=df['FI_13'],
                                mode='lines',
                                name='Force Index')
                    ])
                    fig.update_layout(title=f"Force Index for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Geometric Return Indicator":
                st.success("This program allows you to view the Geometric Return Indicator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Compute Geometric Return Indicator
                    n = 10
                    df["Geometric_Return"] = pd.Series(df["Adj Close"]).rolling(n).apply(gmean)

                    # Plot Geometric Return Indicator with Candlestick graph
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Geometric_Return'], mode='lines', name='Geometric Return Indicator'))
                    fig.update_layout(title=f"Geometric Return Indicator for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Golden/Death Cross":
                st.success("This program allows you to view the Golden/Death Cross of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Compute Golden/Death Cross
                    df["MA_50"] = df["Adj Close"].rolling(center=False, window=50).mean()
                    df["MA_200"] = df["Adj Close"].rolling(center=False, window=200).mean()
                    df["diff"] = df["MA_50"] - df["MA_200"]

                    # Plot Golden/Death Cross with Candlestick graph
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['MA_50'], mode='lines', name='MA_50'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['MA_200'], mode='lines', name='MA_200'))
                    fig.update_layout(title=f"Golden/Death Cross for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "High Minus Low":
                st.success("This program allows you to view the High Minus Low of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Compute High Minus Low
                    df["H-L"] = df["High"] - df["Low"]

                    # Plot High Minus Low with Candlestick graph
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['H-L'], mode='lines', name='High Minus Low'))
                    fig.update_layout(title=f"High Minus Low for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Hull Moving Average":
                st.success("This program allows you to view the Hull Moving Average (HMA) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Compute Hull Moving Average
                    period = 20
                    df['WMA'] = df['Adj Close'].rolling(window=period).mean()
                    half_period = int(period / 2)
                    sqrt_period = int(np.sqrt(period))
                    df['Weighted_MA'] = df['Adj Close'].rolling(window=half_period).mean() * 2 - df['Adj Close'].rolling(window=period).mean()
                    df['HMA'] = df['Weighted_MA'].rolling(window=sqrt_period).mean()

                    # Plot Hull Moving Average with Candlestick graph
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['HMA'], mode='lines', name='Hull Moving Average'))
                    fig.update_layout(title=f"Hull Moving Average (HMA) for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Keltner Channels":
                st.success("This program allows you to visualize Keltner Channels for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Keltner Channels
                    n = 20
                    df["EMA"] = ta.EMA(df["Adj Close"], timeperiod=n)
                    df["ATR"] = ta.ATR(df["High"], df["Low"], df["Adj Close"], timeperiod=10)
                    df["Upper Line"] = df["EMA"] + 2 * df["ATR"]
                    df["Lower Line"] = df["EMA"] - 2 * df["ATR"]

                    # Plot Keltner Channels
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['EMA'], mode='lines', name='EMA'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Upper Line'], mode='lines', name='Upper Line'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Lower Line'], mode='lines', name='Lower Line'))
                    fig.update_layout(title=f"Keltner Channels for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Linear Regression":
                st.success("This program allows you to visualize Linear Regression for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Linear Regression
                    avg = df["Adj Close"].mean()
                    df["Linear_Regression"] = avg - (df["Adj Close"].mean() - df["Adj Close"]) / 20

                    # Plot Linear Regression
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Linear_Regression'], mode='lines', name='Linear Regression'))
                    fig.update_layout(title=f"Linear Regression for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Linear Regression Slope":
                st.success("This program allows you to visualize Linear Regression Slope for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Linear Regression Slope
                    avg1 = df["Adj Close"].mean()
                    avg2 = df["Adj Close"].mean()
                    df["AVGS1_S1"] = avg1 - df["Adj Close"]
                    df["AVGS2_S2"] = avg2 - df["Adj Close"]
                    df["Average_SQ"] = df["AVGS1_S1"] ** 2
                    df["AVG_AVG"] = df["AVGS1_S1"] * df["AVGS2_S2"]
                    sum_sq = df["Average_SQ"].sum()
                    sum_avg = df["AVG_AVG"].sum()
                    slope = sum_avg / sum_sq
                    intercept = avg2 - (slope * avg1)
                    df["Linear_Regression"] = intercept + slope * (df["Adj Close"])
                    df = df.drop(["AVGS1_S1", "AVGS2_S2", "Average_SQ", "AVG_AVG"], axis=1)

                    # Plot Linear Regression Slope
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Linear_Regression'], mode='lines', name='Linear Regression Slope'))
                    fig.update_layout(title=f"Linear Regression Slope for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Linear Weighted Moving Average (LWMA)":
                st.success("This program allows you to visualize Linearly Weighted Moving Average (LWMA) for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Linear Weighted Moving Average (LWMA)
                    def linear_weight_moving_average(close, n):
                        lwma = [np.nan] * n
                        for i in range(n, len(close)):
                            lwma.append(
                                (close[i - n : i] * (np.arange(n) + 1)).sum() / (np.arange(n) + 1).sum()
                            )
                        return lwma

                    period = 14
                    df["LWMA"] = linear_weight_moving_average(df["Adj Close"], period)

                    # Plot Linear Weighted Moving Average (LWMA)
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['LWMA'], mode='lines', name='LWMA'))
                    fig.update_layout(title=f"Linear Weighted Moving Average (LWMA) for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "McClellan Oscillator":
                st.success("This program allows you to visualize McClellan Oscillator for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate McClellan Oscillator
                    ema_19 = ta.EMA(df["Advancing Issues"] - df["Declining Issues"], timeperiod=19)
                    ema_39 = ta.EMA(df["Advancing Issues"] - df["Declining Issues"], timeperiod=39)
                    mcclellan_oscillator = ema_19 - ema_39

                    # Plot McClellan Oscillator
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=mcclellan_oscillator, mode='lines', name='McClellan Oscillator'))
                    fig.update_layout(title=f"McClellan Oscillator for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Value',
                                    template='plotly_dark')
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Momentum":
                st.success("This program allows you to visualize Momentum for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Momentum
                    period = 14
                    df['Momentum'] = df['Adj Close'].diff(period)

                    # Plot Momentum
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['Open'],
                                                high=df['High'],
                                                low=df['Low'],
                                                close=df['Adj Close'],
                                                name='Candlestick'))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Momentum'], mode='lines', name='Momentum'))
                    fig.update_layout(title=f"Momentum for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    template='plotly_dark')
                    st.plotly_chart(fig)        

            if pred_option_Technical_Indicators == "Moving Average Envelopes":
                st.success("This program allows you to visualize Moving Average Envelopes for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df["20SMA"] = ta.SMA(df["Adj Close"], timeperiod=20)
                    df["Upper_Envelope"] = df["20SMA"] + (df["20SMA"] * 0.025)
                    df["Lower_Envelope"] = df["20SMA"] - (df["20SMA"] * 0.025)

                    # Plot Line Chart with Moving Average Envelopes
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Upper_Envelope"], mode='lines', name='Upper Envelope', line=dict(color='blue')))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Lower_Envelope"], mode='lines', name='Lower Envelope', line=dict(color='red')))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"].rolling(20).mean(), mode='lines', name='Moving Average', line=dict(color='orange', dash='dash')))
                    fig_line.update_layout(title=f"Stock of Moving Average Envelopes for {symbol}",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig_line)

                    # Candlestick with Moving Average Envelopes
                    fig_candlestick = go.Figure(data=[go.Candlestick(x=df.index,
                                                                    open=df['Open'],
                                                                    high=df['High'],
                                                                    low=df['Low'],
                                                                    close=df['Adj Close'],
                                                                    name='Candlestick')])
                    fig_candlestick.add_trace(go.Scatter(x=df.index, y=df["Upper_Envelope"], mode='lines', name='Upper Envelope', line=dict(color='blue')))
                    fig_candlestick.add_trace(go.Scatter(x=df.index, y=df["Lower_Envelope"], mode='lines', name='Lower Envelope', line=dict(color='red')))
                    fig_candlestick.add_trace(go.Scatter(x=df.index, y=df["Adj Close"].rolling(20).mean(), mode='lines', name='Moving Average', line=dict(color='orange', dash='dash')))
                    fig_candlestick.update_layout(title=f"Stock {symbol} Candlestick with Moving Average Envelopes",
                                                xaxis_title='Date',
                                                yaxis_title='Price')
            
                    st.plotly_chart(fig_candlestick)

            if pred_option_Technical_Indicators == "Moving Average High/Low":
                st.success("This program allows you to visualize Moving Average High/Low for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    n = 14  # number of periods
                    df["MA_High"] = df["High"].rolling(n).mean()
                    df["MA_Low"] = df["Low"].rolling(n).mean()

                    # Plot Line Chart with Moving Average High/Low
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA_High"], mode='lines', name='Moving Average of High'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA_Low"], mode='lines', name='Moving Average of Low'))
                    fig_line.update_layout(title=f"Stock {symbol} Moving Average High/Low",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig_line)

            if pred_option_Technical_Indicators == "Moving Average Ribbon":
                st.success("This program allows you to visualize Moving Average Ribbon for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df["MA10"] = df["Adj Close"].rolling(10).mean()
                    df["MA20"] = df["Adj Close"].rolling(20).mean()
                    df["MA30"] = df["Adj Close"].rolling(30).mean()
                    df["MA40"] = df["Adj Close"].rolling(40).mean()
                    df["MA50"] = df["Adj Close"].rolling(50).mean()
                    df["MA60"] = df["Adj Close"].rolling(60).mean()

                    # Plot Line Chart with Moving Average Ribbon
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA10"], mode='lines', name='MA10'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA20"], mode='lines', name='MA20'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA30"], mode='lines', name='MA30'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA40"], mode='lines', name='MA40'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA50"], mode='lines', name='MA50'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["MA60"], mode='lines', name='MA60'))
                    fig_line.update_layout(title=f"Stock {symbol} Moving Average Ribbon",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig_line)

            if pred_option_Technical_Indicators == "Moving Average Envelopes (MMA)":
                st.success("This program allows you to visualize Moving Average Envelopes (MMA) for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df["20SMA"] = ta.SMA(df["Adj Close"], timeperiod=20)
                    df["Upper_Envelope"] = df["20SMA"] + (df["20SMA"] * 0.025)
                    df["Lower_Envelope"] = df["20SMA"] - (df["20SMA"] * 0.025)

                    # Plot Line Chart with Moving Average Envelopes (MMA)
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Upper_Envelope"], mode='lines', name='Upper Envelope', line=dict(color='blue')))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Lower_Envelope"], mode='lines', name='Lower Envelope', line=dict(color='red')))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"].rolling(20).mean(), mode='lines', name='Moving Average', line=dict(color='orange', dash='dash')))
                    fig_line.update_layout(title=f"Stock {symbol} Moving Average Envelopes (MMA)",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig_line)

            if pred_option_Technical_Indicators == "Moving Linear Regression":
                st.success("This program allows you to visualize Moving Linear Regression for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df['Slope'] = ta.LINEARREG_SLOPE(df['Adj Close'], timeperiod=14)

                    # Plot Line Chart with Moving Linear Regression
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Slope"], mode='lines', name='Slope', line=dict(color='red')))
                    fig_line.update_layout(title=f"Stock {symbol} Moving Linear Regression",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig_line)

            if pred_option_Technical_Indicators == "New Highs/New Lows":
                st.success("This program allows you to visualize New Highs/New Lows for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    df = yf.download(symbol, start, end)

                    df['52wHigh'] = df['Adj Close'].rolling(window=252).max()
                    df['52wLow'] = df['Adj Close'].rolling(window=252).min()

                    # Plot Line Chart with New Highs/New Lows
                    fig_line = go.Figure()
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Adj Close'))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["52wHigh"], mode='lines', name='52 Weeks High', line=dict(color='green')))
                    fig_line.add_trace(go.Scatter(x=df.index, y=df["52wLow"], mode='lines', name='52 Weeks Low', line=dict(color='red')))
                    fig_line.update_layout(title=f"Stock {symbol} New Highs/New Lows",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig_line)

            if pred_option_Technical_Indicators == "Pivot Point":
                st.success("This program allows you to visualize Pivot Points for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate Pivot Points
                    PP = (dataset["High"] + dataset["Low"] + dataset["Close"]) / 3
                    R1 = 2 * PP - dataset["Low"]
                    S1 = 2 * PP - dataset["High"]
                    R2 = PP + dataset["High"] - dataset["Low"]
                    S2 = PP - dataset["High"] + dataset["Low"]
                    R3 = dataset["High"] + 2 * (PP - dataset["Low"])
                    S3 = dataset["Low"] - 2 * (dataset["High"] - PP)

                    # Plot Pivot Points
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=PP, mode='lines', name='Pivot Point'),
                                        go.Scatter(x=dataset.index, y=R1, mode='lines', name='R1'),
                                        go.Scatter(x=dataset.index, y=S1, mode='lines', name='S1'),
                                        go.Scatter(x=dataset.index, y=R2, mode='lines', name='R2'),
                                        go.Scatter(x=dataset.index, y=S2, mode='lines', name='S2'),
                                        go.Scatter(x=dataset.index, y=R3, mode='lines', name='R3'),
                                        go.Scatter(x=dataset.index, y=S3, mode='lines', name='S3')])
                    fig.update_layout(title=f"{symbol} Pivot Points",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig)
        
            if pred_option_Technical_Indicators == "Price Channels":
                st.success("This program allows you to visualize Price Channels for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate Price Channels
                    rolling_high = dataset['High'].rolling(window=20).max()
                    rolling_low = dataset['Low'].rolling(window=20).min()
                    midline = (rolling_high + rolling_low) / 2

                    # Plot Price Channels
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=rolling_high, mode='lines', name='Upper Channel'),
                                        go.Scatter(x=dataset.index, y=rolling_low, mode='lines', name='Lower Channel'),
                                        go.Scatter(x=dataset.index, y=midline, mode='lines', name='Midline')])
                    fig.update_layout(title=f"{symbol} Price Channels",
                                    xaxis_title='Date',
                                    yaxis_title='Price')
                    
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Price Relative":
                st.success("This program allows you to visualize Price Relative for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                benchmark_ticker = st.text_input("Enter the benchmark ticker")
                if ticker and benchmark_ticker:
                    message = (f"Ticker captured : {ticker}, Benchmark Ticker : {benchmark_ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    benchmark = benchmark_ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)
                    benchmark_data = yf.download(benchmark, start, end)

                    # Calculate Price Relative
                    price_relative = dataset['Adj Close'] / benchmark_data['Adj Close']

                    # Plot Price Relative
                    fig = go.Figure(data=[go.Scatter(x=price_relative.index, y=price_relative, mode='lines', name='Price Relative')])
                    fig.update_layout(title=f"{symbol} Price Relative to {benchmark}",
                                    xaxis_title='Date',
                                    yaxis_title='Price Relative')
                    
                    st.plotly_chart(fig)


            if pred_option_Technical_Indicators == "Realized Volatility":
                st.success("This program allows you to visualize Realized Volatility for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate Realized Volatility
                    returns = dataset["Adj Close"].pct_change().dropna()
                    realized_volatility = returns.std() * np.sqrt(252)  # Annualized volatility assuming 252 trading days

                    # Plot Realized Volatility
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=returns.index, y=returns, mode='lines', name='Daily Returns'))
                    fig.add_trace(go.Scatter(x=returns.index, y=np.ones(len(returns)) * realized_volatility, mode='lines', name='Realized Volatility', line=dict(color='red', dash='dash')))
                    fig.update_layout(title=f"{symbol} Daily Returns and Realized Volatility",
                                    xaxis_title="Date",
                                    yaxis_title="Returns / Realized Volatility")
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Relative Volatility Index":
                st.success("This program allows you to visualize Relative Volatility Index for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate Relative Volatility Index (RVI)
                    n = 14  # Number of period
                    change = dataset["Adj Close"].diff(1)
                    gain = change.mask(change < 0, 0)
                    loss = abs(change.mask(change > 0, 0))
                    avg_gain = gain.rolling(n).std()
                    avg_loss = loss.rolling(n).std()
                    RS = avg_gain / avg_loss
                    RVI = 100 - (100 / (1 + RS))

                    # Plot RVI
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=RVI.index, y=RVI, mode='lines', name='Relative Volatility Index', line=dict(color='blue')))
                    fig.add_shape(type="line", x0=RVI.index[0], y0=60, x1=RVI.index[-1], y1=60, line=dict(color="red", width=1, dash="dash"), name="Overbought")
                    fig.add_shape(type="line", x0=RVI.index[0], y0=40, x1=RVI.index[-1], y1=40, line=dict(color="green", width=1, dash="dash"), name="Oversold")
                    fig.update_layout(title=f"{symbol} Relative Volatility Index",
                                    xaxis_title="Date",
                                    yaxis_title="RVI")
                    st.plotly_chart(fig)


            if pred_option_Technical_Indicators == "Smoothed Moving Average":
                st.success("This program allows you to visualize Smoothed Moving Average for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    n = 7
                    dataset["SMMA"] = dataset["Adj Close"].ewm(alpha=1 / float(n)).mean()

                    # Plot Smoothed Moving Average
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=dataset["SMMA"], mode='lines', name='Smoothed Moving Average', line=dict(color='red'))])
                    fig.update_layout(title=f"{symbol} Smoothed Moving Average",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Speed Resistance Lines":
                st.success("This program allows you to visualize Speed Resistance Lines for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    dataset["Middle_Line"] = dataset["Low"] + (dataset["High"] - dataset["Low"]) * 0.667
                    dataset["Lower_Line"] = dataset["Low"] + (dataset["High"] - dataset["Low"]) * 0.333

                    # Plot Speed Resistance Lines
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=dataset["Middle_Line"], mode='lines', name='Middle Line', line=dict(color='red')),
                                        go.Scatter(x=dataset.index, y=dataset["Lower_Line"], mode='lines', name='Lower Line', line=dict(color='green'))])
                    fig.update_layout(title=f"{symbol} Speed Resistance Lines",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Standard Deviation Volatility":
                st.success("This program allows you to visualize Standard Deviation Volatility for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    dataset["STD"] = dataset["Adj Close"].rolling(10).std()

                    # Plot Standard Deviation Volatility
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=dataset["STD"], mode='lines', name='Standard Deviation Volatility', line=dict(color='red'))])
                    fig.update_layout(title=f"{symbol} Standard Deviation Volatility",
                                    xaxis_title="Date",
                                    yaxis_title="Price")
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Stochastic RSI":
                st.success("This program allows you to visualize Stochastic RSI for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate RSI
                    n = 14
                    change = dataset["Adj Close"].diff(1)
                    gain = change.mask(change < 0, 0)
                    loss = abs(change.mask(change > 0, 0))
                    avg_gain = gain.rolling(n).mean()
                    avg_loss = loss.rolling(n).mean()
                    RS = avg_gain / avg_loss
                    RSI = 100 - (100 / (1 + RS))

                    # Calculate Stochastic RSI
                    LL_RSI = RSI.rolling(14).min()
                    HH_RSI = RSI.rolling(14).max()
                    dataset["Stoch_RSI"] = (RSI - LL_RSI) / (HH_RSI - LL_RSI)

                    # Plot Stochastic RSI
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=dataset["Stoch_RSI"], mode='lines', name='Stochastic RSI', line=dict(color='red'))])
                    fig.update_layout(title=f"{symbol} Stochastic RSI",
                                    xaxis_title="Date",
                                    yaxis_title="Stochastic RSI")
                    st.plotly_chart(fig)
            if pred_option_Technical_Indicators == "Stochastic Fast":
                st.success("This program allows you to visualize Stochastic Fast for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate Stochastic Fast
                    low_min = dataset['Low'].rolling(window=14).min()
                    high_max = dataset['High'].rolling(window=14).max()
                    dataset['%K'] = 100 * (dataset['Close'] - low_min) / (high_max - low_min)
                    dataset['%D'] = dataset['%K'].rolling(window=3).mean()

                    # Plot Stochastic Fast
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=dataset["%K"], mode='lines', name='Stochastic Fast %K', line=dict(color='red')),
                                        go.Scatter(x=dataset.index, y=dataset["%D"], mode='lines', name='Stochastic Fast %D', line=dict(color='blue'))])
                    fig.update_layout(title=f"{symbol} Stochastic Fast",
                                    xaxis_title="Date",
                                    yaxis_title="Stochastic Fast")
                    st.plotly_chart(fig)
            if pred_option_Technical_Indicators == "Stochastic Full":
                st.success("This program allows you to visualize Stochastic Full for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate Stochastic Full
                    low_min = dataset['Low'].rolling(window=14).min()
                    high_max = dataset['High'].rolling(window=14).max()
                    dataset['%K'] = 100 * (dataset['Close'] - low_min) / (high_max - low_min)
                    dataset['%D'] = dataset['%K'].rolling(window=3).mean()
                    dataset['%D_full'] = dataset['%D'].rolling(window=3).mean()

                    # Plot Stochastic Full
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=dataset["%K"], mode='lines', name='Stochastic Full %K', line=dict(color='red')),
                                        go.Scatter(x=dataset.index, y=dataset["%D_full"], mode='lines', name='Stochastic Full %D', line=dict(color='blue'))])
                    fig.update_layout(title=f"{symbol} Stochastic Full",
                                    xaxis_title="Date",
                                    yaxis_title="Stochastic Full")
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "Stochastic Slow":
                st.success("This program allows you to visualize Stochastic Slow for a selected ticker")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = f"Ticker captured: {ticker}"
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date

                    # Read data
                    dataset = yf.download(symbol, start, end)

                    # Calculate Stochastic Slow
                    low_min = dataset['Low'].rolling(window=14).min()
                    high_max = dataset['High'].rolling(window=14).max()
                    dataset['%K'] = 100 * (dataset['Close'] - low_min) / (high_max - low_min)
                    dataset['%D'] = dataset['%K'].rolling(window=3).mean()

                    # Plot Stochastic Slow
                    fig = go.Figure(data=[go.Candlestick(x=dataset.index,
                                                        open=dataset['Open'],
                                                        high=dataset['High'],
                                                        low=dataset['Low'],
                                                        close=dataset['Close'],
                                                        name='Candlesticks'),
                                        go.Scatter(x=dataset.index, y=dataset["%K"], mode='lines', name='Stochastic Slow %K', line=dict(color='red')),
                                        go.Scatter(x=dataset.index, y=dataset["%D"], mode='lines', name='Stochastic Slow %D', line=dict(color='blue'))])
                    fig.update_layout(title=f"{symbol} Stochastic Slow",
                                    xaxis_title="Date",
                                    yaxis_title="Stochastic Slow")
                    st.plotly_chart(fig)

            
            
            if pred_option_Technical_Indicators == "Super Trend":
                st.success("This program allows you to view the Super Trend of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    n = 7  # Number of periods
                    df["H-L"] = abs(df["High"] - df["Low"])
                    df["H-PC"] = abs(df["High"] - df["Adj Close"].shift(1))
                    df["L-PC"] = abs(df["Low"] - df["Adj Close"].shift(1))
                    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1)
                    df["ATR"] = df["TR"].rolling(n).mean()

                    df["Upper Basic"] = (df["High"] + df["Low"]) / 2 + (2 * df["ATR"])
                    df["Lower Basic"] = (df["High"] + df["Low"]) / 2 - (2 * df["ATR"])

                    df["Upper Band"] = df["Upper Basic"]
                    df["Lower Band"] = df["Lower Basic"]

                    for i in range(n, len(df)):
                        if df["Close"][i - 1] <= df["Upper Band"][i - 1]:
                            df["Upper Band"][i] = min(df["Upper Basic"][i], df["Upper Band"][i - 1])
                        else:
                            df["Upper Band"][i] = df["Upper Basic"][i]

                    for i in range(n, len(df)):
                        if df["Close"][i - 1] >= df["Lower Band"][i - 1]:
                            df["Lower Band"][i] = max(df["Lower Basic"][i], df["Lower Band"][i - 1])
                        else:
                            df["Lower Band"][i] = df["Lower Basic"][i]

                    df["SuperTrend"] = 0.00
                    for i in range(n, len(df)):
                        if df["Close"][i] <= df["Upper Band"][i]:
                            df["SuperTrend"][i] = df["Upper Band"][i]
                        elif df["Close"][i] > df["Upper Band"][i]:
                            df["SuperTrend"][i] = df["Lower Band"][i]

                    # Candlestick Chart with Super Trend
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'], name='Candlestick'))

                    fig.update_layout(title="Stock " + symbol + " Candlestick Chart with Super Trend",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))

                    fig.add_trace(go.Scatter(x=df.index, y=df["SuperTrend"], mode='lines', name='SuperTrend'))
                    st.plotly_chart(fig)

            if pred_option_Technical_Indicators == "True Strength Index":
                st.success("This program allows you to view the True Strength Index (TSI) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate True Strength Index (TSI)
                    df["PC"] = df["Adj Close"] - df["Adj Close"].shift()
                    df["EMA_FS"] = df["PC"].ewm(span=25, min_periods=25, adjust=True).mean()
                    df["EMA_SS"] = df["EMA_FS"].ewm(span=13, min_periods=13, adjust=True).mean()
                    df["Absolute_PC"] = abs(df["Adj Close"] - df["Adj Close"].shift())
                    df["Absolute_FS"] = df["Absolute_PC"].ewm(span=25, min_periods=25).mean()
                    df["Absolute_SS"] = df["Absolute_FS"].ewm(span=13, min_periods=13).mean()
                    df["TSI"] = 100 * df["EMA_SS"] / df["Absolute_SS"]
                    df = df.drop(["PC", "EMA_FS", "EMA_SS", "Absolute_PC", "Absolute_FS", "Absolute_SS"], axis=1)

                    # Plotting
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Closing Price'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["TSI"], mode='lines', name='True Strength Index'))
                    fig.update_layout(title="Stock " + symbol + " True Strength Index",
                                    xaxis_title="Date",
                                    yaxis_title="Value",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick Chart with True Strength Index
                    fig_candle = go.Figure(data=[go.Candlestick(x=df.index,
                                            open=df['Open'],
                                            high=df['High'],
                                            low=df['Low'],
                                            close=df['Close'], name='Candlestick')])
                    fig_candle.add_trace(go.Scatter(x=df.index, y=df["TSI"], mode='lines', name='True Strength Index'))
                    fig_candle.update_layout(title="Stock " + symbol + " Candlestick Chart with True Strength Index",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig_candle)
        
            if pred_option_Technical_Indicators == "Ultimate Oscillator":
                st.success("This program allows you to view the Ultimate Oscillator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Ultimate Oscillator
                    df["Prior Close"] = df["Adj Close"].shift()
                    df["BP"] = df["Adj Close"] - df[["Low", "Prior Close"]].min(axis=1)
                    df["TR"] = df[["High", "Prior Close"]].max(axis=1) - df[["Low", "Prior Close"]].min(axis=1)
                    df["Average7"] = df["BP"].rolling(7).sum() / df["TR"].rolling(7).sum()
                    df["Average14"] = df["BP"].rolling(14).sum() / df["TR"].rolling(14).sum()
                    df["Average28"] = df["BP"].rolling(28).sum() / df["TR"].rolling(28).sum()
                    df["UO"] = 100 * (4 * df["Average7"] + 2 * df["Average14"] + df["Average28"]) / (4 + 2 + 1)
                    df = df.drop(["Prior Close", "BP", "TR", "Average7", "Average14", "Average28"], axis=1)

                    # Plotting
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Closing Price'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["UO"], mode='lines', name='Ultimate Oscillator'))
                    fig.update_layout(title="Stock " + symbol + " Ultimate Oscillator",
                                    xaxis_title="Date",
                                    yaxis_title="Value",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick Chart with Ultimate Oscillator
                    fig_candle = go.Figure(data=[go.Candlestick(x=df.index,
                                            open=df['Open'],
                                            high=df['High'],
                                            low=df['Low'],
                                            close=df['Close'], name='Candlestick')])
                    fig_candle.add_trace(go.Scatter(x=df.index, y=df["UO"], mode='lines', name='Ultimate Oscillator'))
                    fig_candle.update_layout(title="Stock " + symbol + " Candlestick Chart with Ultimate Oscillator",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig_candle)

            if pred_option_Technical_Indicators == "Variance Indicator":
                st.success("This program allows you to view the Variance Indicator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Variance Indicator
                    n = 14
                    df["Variance"] = df["Adj Close"].rolling(n).var()

                    # Plotting
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Closing Price'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Variance"], mode='lines', name='Variance Indicator'))
                    fig.update_layout(title="Stock " + symbol + " Variance Indicator",
                                    xaxis_title="Date",
                                    yaxis_title="Value",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick Chart with Variance Indicator
                    fig_candle = go.Figure(data=[go.Candlestick(x=df.index,
                                            open=df['Open'],
                                            high=df['High'],
                                            low=df['Low'],
                                            close=df['Close'], name='Candlestick')])
                    fig_candle.add_trace(go.Scatter(x=df.index, y=df["Variance"], mode='lines', name='Variance Indicator'))
                    fig_candle.update_layout(title="Stock " + symbol + " Candlestick Chart with Variance Indicator",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig_candle)

            if pred_option_Technical_Indicators == "Volume Price Confirmation Indicator":
                st.success("This program allows you to view the Volume Price Confirmation Indicator of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Volume Price Confirmation Indicator
                    short_term = 5
                    long_term = 20
                    vwma_lt = ((df["Adj Close"] * df["Volume"]) + (df["Adj Close"].shift(1) * df["Volume"].shift(1)) + (df["Adj Close"].shift(2) * df["Volume"].shift(2))) / (df["Volume"].rolling(long_term).sum())
                    vwma_st = ((df["Adj Close"] * df["Volume"]) + (df["Adj Close"].shift(1) * df["Volume"].shift(1)) + (df["Adj Close"].shift(2) * df["Volume"].shift(2))) / (df["Volume"].rolling(short_term).sum())
                    vpc = vwma_lt - df["Adj Close"].rolling(long_term).mean()
                    vpr = vwma_st / df["Adj Close"].rolling(short_term).mean()
                    vm = df["Adj Close"].rolling(short_term).mean() / df["Adj Close"].rolling(long_term).mean()
                    vpci = vpc * vpr * vm

                    # Plotting
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name='Closing Price'))
                    fig.add_trace(go.Scatter(x=df.index, y=vpci, mode='lines', name='Volume Price Confirmation Indicator'))
                    fig.update_layout(title="Stock " + symbol + " Volume Price Confirmation Indicator",
                                    xaxis_title="Date",
                                    yaxis_title="Value",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick Chart with Volume Price Confirmation Indicator
                    fig_candle = go.Figure(data=[go.Candlestick(x=df.index,
                                            open=df['Open'],
                                            high=df['High'],
                                            low=df['Low'],
                                            close=df['Close'], name='Candlestick')])
                    fig_candle.add_trace(go.Scatter(x=df.index, y=vpci, mode='lines', name='Volume Price Confirmation Indicator'))
                    fig_candle.update_layout(title="Stock " + symbol + " Candlestick Chart with Volume Price Confirmation Indicator",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig_candle)

            if pred_option_Technical_Indicators == "Volume Weighted Moving Average (VWMA)":
                st.success("This program allows you to view the Volume Weighted Moving Average (VWMA) of a ticker over time")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:")
                with col2:
                    end_date = st.date_input("End Date:")
                if st.button("Check"):    
                    symbol = ticker
                    start = start_date
                    end = end_date
                    # Read data
                    df = yf.download(symbol, start, end)

                    # Calculate Volume Weighted Moving Average (VWMA)
                    df["Volume_x_Close"] = df["Volume"] * df["Close"]
                    df["VWMA"] = df["Volume_x_Close"].rolling(window=14).sum() / df["Volume"].rolling(window=14).sum()

                    # Plotting
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode='lines', name='Closing Price'))
                    fig.add_trace(go.Scatter(x=df.index, y=df["VWMA"], mode='lines', name='Volume Weighted Moving Average (VWMA)'))
                    fig.update_layout(title="Stock " + symbol + " Volume Weighted Moving Average (VWMA)",
                                    xaxis_title="Date",
                                    yaxis_title="Value",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig)

                    # Candlestick Chart with Volume Weighted Moving Average (VWMA)
                    fig_candle = go.Figure(data=[go.Candlestick(x=df.index,
                                            open=df['Open'],
                                            high=df['High'],
                                            low=df['Low'],
                                            close=df['Close'], name='Candlestick')])
                    fig_candle.add_trace(go.Scatter(x=df.index, y=df["VWMA"], mode='lines', name='Volume Weighted Moving Average (VWMA)'))
                    fig_candle.update_layout(title="Stock " + symbol + " Candlestick Chart with Volume Weighted Moving Average (VWMA)",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    legend=dict(x=0, y=1, traceorder="normal"))
                    st.plotly_chart(fig_candle)
        elif option =='Portfolio Strategies':
            pred_option_portfolio_strategies = st.selectbox('Make a choice', [
                                                                    'Astral Timing signals',
                                                                    'Lumibot Backtesting strategy',
                                                                    'Backtest Strategies',
                                                                    'Backtrader Backtest',
                                                                    'Best Moving Averages Analysis',
                                                                    'EMA Crossover Strategy',
                                                                    'Factor Analysis',
                                                                    'Financial Signal Analysis',
                                                                    'Geometric Brownian Motion',
                                                                    'Long Hold Stats Analysis',
                                                                    'LS DCA Analysis',
                                                                    'Monte Carlo',
                                                                    'Moving Average Crossover Signals',
                                                                    'Moving Average Strategy',
                                                                    'Optimal Portfolio',
                                                                    'Optimized Bollinger Bands',
                                                                    'Pairs Trading',
                                                                    'Portfolio Analysis',
                                                                    'Portfolio Optimization',
                                                                    'Portfolio VAR Simulation',
                                                                    'Risk Management'
                                                                    'RSI Trendline Strategy',
                                                                    'RWB Strategy',
                                                                    'SMA Trading Strategy',
                                                                    'Stock Spread Plotter',
                                                                    'Support Resistance Finder'])

            if pred_option_portfolio_strategies == "Astral Timing signals":
                st.success("This program allows you to start backtesting using Astral Timing signals")
                ticker = st.text_input("Enter the ticker you want to monitor")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")

                if st.button("Check"):
                    # Apply Astral Timing signals to stock data.
                    def astral(data, completion, step, step_two, what, high, low, where_long, where_short):
                        data['long_signal'] = 0
                        data['short_signal'] = 0

                        # Iterate through the DataFrame
                        for i in range(len(data)):
                            # Long signal logic
                            if data.iloc[i][what] < data.iloc[i - step][what] and data.iloc[i][low] < data.iloc[i - step_two][low]:
                                data.at[data.index[i], 'long_signal'] = -1
                            elif data.iloc[i][what] >= data.iloc[i - step][what]:
                                data.at[data.index[i], 'long_signal'] = 0

                            # Short signal logic
                            if data.iloc[i][what] > data.iloc[i - step][what] and data.iloc[i][high] > data.iloc[i - step_two][high]:
                                data.at[data.index[i], 'short_signal'] = 1
                            elif data.iloc[i][what] <= data.iloc[i - step][what]:
                                data.at[data.index[i], 'short_signal'] = 0

                        return data

                    # Define stock ticker and date range
                
                    start = start_date
                    end = end_date

                    # Fetch stock data
                    data = yf.download(ticker, start, end)

                    # Apply Astral Timing signals
                    astral_data = astral(data, 8, 1, 5, 'Close', 'High', 'Low', 'long_signal', 'short_signal')

                    # Display the results
                    # Create candlestick chart with signals
                    fig = go.Figure(data=[go.Candlestick(x=astral_data.index,
                                                        open=astral_data['Open'],
                                                        high=astral_data['High'],
                                                        low=astral_data['Low'],
                                                        close=astral_data['Close'])])

                    # Add long and short signals to the plot
                    fig.add_trace(go.Scatter(x=astral_data.index, y=astral_data['long_signal'],
                                            mode='markers', marker=dict(color='blue'), name='Long Signal'))
                    fig.add_trace(go.Scatter(x=astral_data.index, y=astral_data['short_signal'],
                                            mode='markers', marker=dict(color='red'), name='Short Signal'))

                    # Customize layout
                    fig.update_layout(title=f"{ticker} Candlestick Chart with Signals",
                                    xaxis_title="Date",
                                    yaxis_title="Price",
                                    xaxis_rangeslider_visible=False)

                    # Display the interactive plot
                    st.plotly_chart(fig)
                    st.write(astral_data[['long_signal', 'short_signal']])

            if pred_option_portfolio_strategies == "Backtest Strategies":
                st.success("This portion allows you backtest a ticker for a period using SMA Logic ")
                ticker = st.text_input("Enter the ticker for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):

                    # Function to fetch stock data
                    def get_stock_data(stock, start, end):
                        """
                        Fetches stock data from Yahoo Finance.
                        """
                        return yf.download(stock, start, end)

                    # Trading statistics calculation
                    def calculate_trading_statistics(df, buy_sell_logic, additional_logic=None):
                            """
                            Calculates trading statistics based on buy/sell logic.
                            """
                            position = 0
                            percentChange = []
                            buyP = sellP = 0  # Initialize buyP and sellP
                            for i in df.index:
                                close = df.loc[i, "Adj Close"]
                                if buy_sell_logic(df, i, position):
                                    position = 0 if position == 1 else 1
                                    buyP = close if position == 1 else buyP
                                    sellP = close if position == 0 else sellP
                                    if position == 0:
                                        perc = (sellP / buyP - 1) * 100
                                        percentChange.append(perc)
                                if additional_logic: additional_logic(df, i)
                            return calculate_statistics_from_percent_change(percentChange)

                    # Compute statistics from percent change
                    def calculate_statistics_from_percent_change(percentChange):
                        """
                        Computes statistics from percentage change in stock prices.
                        """
                        gains = sum(p for p in percentChange if p > 0)
                        losses = sum(p for p in percentChange if p < 0)
                        numGains = sum(1 for p in percentChange if p > 0)
                        numLosses = sum(1 for p in percentChange if p < 0)
                        totReturn = round(np.prod([((p / 100) + 1) for p in percentChange]) * 100 - 100, 2)
                        avgGain = gains / numGains if numGains > 0 else 0
                        avgLoss = losses / numLosses if numLosses > 0 else 0
                        maxReturn = max(percentChange) if numGains > 0 else 0
                        maxLoss = min(percentChange) if numLosses > 0 else 0
                        ratioRR = -avgGain / avgLoss if numLosses > 0 else "inf"
                        batting_avg = numGains / (numGains + numLosses) if numGains + numLosses > 0 else 0
                        return {
                            "total_return": totReturn,
                            "avg_gain": avgGain,
                            "avg_loss": avgLoss,
                            "max_return": maxReturn,
                            "max_loss": maxLoss,
                            "gain_loss_ratio": ratioRR,
                            "num_trades": numGains + numLosses,
                            "batting_avg": batting_avg
                        }

                    # SMA strategy logic
                    def sma_strategy_logic(df, i, position):
                        """
                        Logic for Simple Moving Average (SMA) trading strategy.
                        """
                        SMA_short, SMA_long = df["SMA_20"], df["SMA_50"]
                        return (SMA_short[i] > SMA_long[i] and position == 0) or (SMA_short[i] < SMA_long[i] and position == 1)

                
                    stock = ticker
                    num_of_years = years
                    start = start_date
                    end = end_date
                    df = get_stock_data(stock, start, end)

                    # Implementing SMA strategy
                    df["SMA_20"] = df["Adj Close"].rolling(window=20).mean()
                    df["SMA_50"] = df["Adj Close"].rolling(window=50).mean()
                    sma_stats = calculate_trading_statistics(df, sma_strategy_logic)
                    st.write("Simple Moving Average Strategy Stats:", sma_stats)

            if pred_option_portfolio_strategies == "Lumibot Backtesting strategy":
                st.success("This portion allows you backtest a ticker for a period using Lumibot YahooBacktesting strategy ")
                ticker = st.text_input("Enter the ticker for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                quantities = st.number_input("Enter the quantities of the ticker to buy")
                if quantities:
                    st.write(f"The noted quantities are : {quantities}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    start = start_date
                    end = end_date
                    class MyStrategy(Strategy):
                        def on_trading_iteration(self):
                            if self.first_iteration:
                                order = self.create_order(ticker, quantity=quantities, side="buy")
                                self.submit_order(order)

                    # Create a backtest
                    backtesting_start = start
                    backtesting_end = end

                    # The benchmark asset to use for the backtest to compare to
                    benchmark_asset = Asset(symbol="QQQ", asset_type="stock")

                    backtest = MyStrategy.backtest(
                        datasource_class=YahooDataBacktesting,
                        backtesting_start=backtesting_start,
                        backtesting_end=backtesting_end,
                        benchmark_asset=benchmark_asset,
                    )


                
            if pred_option_portfolio_strategies == "Backtrader Backtest":
                ticker = st.text_input("Enter the ticker for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):

                    # Setting chart resolution
                    plt.rcParams['figure.dpi'] = 140

                    # API credentials
                    API_KEY = API_KEY_ALPACA
                    SECRET_KEY = SECRET_KEY_ALPACA

                    # Initialize REST API
                    rest_api = REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets/v2')

                    def run_backtest(strategy, symbol, start, end, timeframe=TimeFrame.Day, cash=10000):
                        cerebro = bt.Cerebro(stdstats=True)
                        cerebro.broker.setcash(cash)
                        cerebro.addstrategy(strategy)

                        # Adding analyzers
                        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trade_analyzer')
                        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe_ratio')

                        # Loading data
                        data = rest_api.get_bars(symbol, timeframe, start, end, adjustment='all').df
                        bt_data = bt.feeds.PandasData(dataname=data, name=symbol)
                        cerebro.adddata(bt_data)

                        # Running the backtest
                        initial_value = cerebro.broker.getvalue()
                        st.write(f'Starting Portfolio Value: {initial_value}')
                        results = cerebro.run()
                        final_value = cerebro.broker.getvalue()
                        st.write(f'Final Portfolio Value: {round(final_value, 2)}')

                        strategy_return = 100 * (final_value - initial_value)/initial_value
                        st.write(f'Strategy Return: {round(strategy_return, 2)}%')

                        # Display results
                        strategy_statistics(results, initial_value, data)

                        # Plotting the results
                        cerebro.plot(iplot=False)
                    
                    def strategy_statistics(results, initial_value, data):
                        # Analyzing the results
                        strat = results[0]
                        trade_analysis = strat.analyzers.trade_analyzer.get_analysis()

                        # Sharpe Ratio
                        sharpe_ratio = round(strat.analyzers.sharpe_ratio.get_analysis()['sharperatio'], 2)

                        # Total number of trades
                        total_trades = trade_analysis.total.closed

                        # Win Rate
                        win_rate = round((trade_analysis.won.total / total_trades) * 100, 2) if total_trades > 0 else 0

                        # Average Percent Gain and Loss
                        avg_percent_gain = round(trade_analysis.won.pnl.average / initial_value * 100, 2) if trade_analysis.won.total > 0 else 0
                        avg_percent_loss = round(trade_analysis.lost.pnl.average / initial_value * 100, 2) if trade_analysis.lost.total > 0 else 0

                        # Profit Factor
                        profit_factor = round((avg_percent_gain * win_rate) / (avg_percent_loss * (1 - win_rate)), 2) if avg_percent_loss != 0 else float('inf')

                        # Gain/Loss Ratio
                        gain_loss_ratio = round(avg_percent_gain / -avg_percent_loss, 2) if avg_percent_loss != 0 else float('inf')

                        # Max Return and Max Loss as Percentages
                        max_return = round(trade_analysis.won.pnl.max / initial_value * 100, 2) if trade_analysis.won.total > 0 else 0
                        max_loss = round(trade_analysis.lost.pnl.max / initial_value * 100, 2) if trade_analysis.lost.total > 0 else 0

                        # Buy and Hold Return
                        buy_and_hold_return = round((data['close'].iloc[-1] / data['close'].iloc[0] - 1) * 100, 2)

                        # Displaying results
                        st.write(f'Buy and Hold Return: {buy_and_hold_return}%')
                        st.write('Sharpe Ratio:', sharpe_ratio)
                        st.write('Total Trades:', total_trades)
                        st.write('Win Rate (%):', win_rate)
                        st.write('Average % Gain per Trade:', avg_percent_gain)
                        st.write('Average % Loss per Trade:', avg_percent_loss)
                        st.write('Profit Factor:', profit_factor)
                        st.write('Gain/Loss Ratio:', gain_loss_ratio)
                        st.write('Max % Return on a Trade:', max_return)
                        st.write('Max % Loss on a Trade:', max_loss)

                    # Class for SMA Crossover strategy
                    class SmaCross(bt.Strategy):
                        params = dict(pfast=13, pslow=25)

                        # Define trading strategy
                        def __init__(self):
                            sma1 = bt.ind.SMA(period=self.p.pfast)
                            sma2 = bt.ind.SMA(period=self.p.pslow)
                            self.crossover = bt.ind.CrossOver(sma1, sma2)

                            # Custom trade tracking
                            self.trade_data = []

                        # Execute trades
                        def next(self):
                            # Trading the entire portfolio
                            size = int(self.broker.get_cash() / self.data.close[0])

                            if not self.position:
                                if self.crossover > 0:
                                    self.buy(size=size)
                                    self.entry_bar = len(self)  # Record entry bar index
                            elif self.crossover < 0:
                                self.close()

                        # Record trade details
                        def notify_trade(self, trade):
                            if trade.isclosed:
                                exit_bar = len(self)
                                holding_period = exit_bar - self.entry_bar
                                trade_record = {
                                    'entry': self.entry_bar,
                                    'exit': exit_bar,
                                    'duration': holding_period,
                                    'profit': trade.pnl
                                }
                                self.trade_data.append(trade_record)

                        # Caclulating holding periods
                        def stop(self):
                            # Calculate and st.write average holding periods
                            total_holding = sum([trade['duration'] for trade in self.trade_data])
                            total_trades = len(self.trade_data)
                            avg_holding_period = round(total_holding / total_trades) if total_trades > 0 else 0

                            # Calculating for winners and losers separately
                            winners = [trade for trade in self.trade_data if trade['profit'] > 0]
                            losers = [trade for trade in self.trade_data if trade['profit'] < 0]
                            avg_winner_holding = round(sum(trade['duration'] for trade in winners) / len(winners))if winners else 0
                            avg_loser_holding = round(sum(trade['duration'] for trade in losers) / len(losers)) if losers else 0

                            # Display average holding period statistics
                            st.write('Average Holding Period:', avg_holding_period)
                            st.write('Average Winner Holding Period:', avg_winner_holding)
                            st.write('Average Loser Holding Period:', avg_loser_holding)

                        # Run backtest
                    run_backtest(SmaCross, ticker, start_date, end_date, TimeFrame.Day, portfolio)
            
            if pred_option_portfolio_strategies == "Best Moving Averages Analysis":
                st.success("This portion allows you backtest a ticker for a period using the best moving averages Logic ")
                ticker = st.text_input("Enter the ticker for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Define stock symbol and historical data range
                    symbol = ticker
                    num_of_years = years
                    start_date = start_date
                    end_date = end_date

                    # Fetch stock data using yfinance
                    data = yf.download(symbol, start=start_date, end=end_date)

                    # Calculate Simple Moving Averages (SMAs) for different periods
                    data['SMA_20'] = data['Close'].rolling(window=20).mean()
                    data['SMA_50'] = data['Close'].rolling(window=50).mean()
                    data['SMA_200'] = data['Close'].rolling(window=200).mean()

                    # Create interactive plot for stock price and its SMAs
                    fig_stock = go.Figure()
                    fig_stock.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
                    fig_stock.add_trace(go.Scatter(x=data.index, y=data['SMA_20'], mode='lines', name='20-period SMA'))
                    fig_stock.add_trace(go.Scatter(x=data.index, y=data['SMA_50'], mode='lines', name='50-period SMA'))
                    fig_stock.add_trace(go.Scatter(x=data.index, y=data['SMA_200'], mode='lines', name='200-period SMA'))

                    fig_stock.update_layout(title=f'{symbol} Stock Price and SMAs',
                                            xaxis_title='Date',
                                            yaxis_title='Price')

                    # Display the interactive plot
                    st.plotly_chart(fig_stock)

                    # Analysis to find the best SMA for predicting future returns
                    days_forward = 10
                    results = []

                    # Testing different SMA lengths
                    for sma_length in range(20, 500):
                        data['SMA'] = data['Close'].rolling(sma_length).mean()
                        data['Position'] = data['Close'] > data['SMA']
                        data['Forward Close'] = data['Close'].shift(-days_forward)
                        data['Forward Return'] = (data['Forward Close'] - data['Close']) / data['Close']
                        
                        # Splitting into training and test datasets
                        train_data = data[:int(0.6 * len(data))]
                        test_data = data[int(0.6 * len(data)):]
                        
                        # Calculating average forward returns
                        train_return = train_data[train_data['Position']]['Forward Return'].mean()
                        test_return = test_data[test_data['Position']]['Forward Return'].mean()
                        
                        # Statistical test
                        p_value = ttest_ind(train_data[train_data['Position']]['Forward Return'],
                                            test_data[test_data['Position']]['Forward Return'],
                                            equal_var=False)[1]
                        
                        results.append({'SMA Length': sma_length, 
                                        'Train Return': train_return, 
                                        'Test Return': test_return, 
                                        'p-value': p_value})

                    # Sorting results and printing the best SMA
                    best_result = sorted(results, key=lambda x: x['Train Return'], reverse=True)[0]
                    st.write(f"Best SMA Length: {best_result['SMA Length']}")
                    st.write(f"Train Return: {best_result['Train Return']:.4f}")
                    st.write(f"Test Return: {best_result['Test Return']:.4f}")
                    st.write(f"p-value: {best_result['p-value']:.4f}")

                    # Create interactive plot for the best SMA
                    data['Best SMA'] = data['Close'].rolling(best_result['SMA Length']).mean()
                    fig_best_sma = go.Figure()
                    fig_best_sma.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
                    fig_best_sma.add_trace(go.Scatter(x=data.index, y=data['Best SMA'], mode='lines', name=f"{best_result['SMA Length']} periods SMA"))

                    fig_best_sma.update_layout(title=f'{symbol} Stock Price and Best SMA',
                                                xaxis_title='Date',
                                                yaxis_title='Price')

                    # Display the interactive plot for the best SMA
                    st.plotly_chart(fig_best_sma)

            if pred_option_portfolio_strategies == "EMA Crossover Strategy":
                tickers = []
                ticker = st.text_input("Enter the ticker for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                    tickers.append(ticker)
                more_input = st.selectbox("Please Add one/more ticker(s) for comparison", ("","Yes", "No"))
                if more_input == "Yes":
                    ticker_2 =  st.text_input("Enter another ticker to continue the investigation")
                    tickers.append(ticker_2)
                    portfolio = st.number_input("Enter the portfolio size in USD")
                    if portfolio:
                        st.write(f"The portfolio size in USD Captured is : {portfolio}")
                    min_date = datetime(1980, 1, 1)
                    # Date input widget with custom minimum date
                    col1, col2 = st.columns([2, 2])
                    with col1:
                        start_date = st.date_input("Start date:", min_value=min_date)
                    with col2:
                        end_date = st.date_input("End Date:")
                    years = end_date.year - start_date.year
                    st.success(f"years captured : {years}")
                    if st.button("Check"):
                        # Define the analysis period
                        num_of_years = years
                        start =  start_date
                        end = end_date

                        # Define tickers for analysis

                        # Fetch stock data using Yahoo Finance
                        df = yf.download(tickers, start, end)['Close']

                        # Calculate moving averages
                        short_rolling = df.rolling(window=20).mean()
                        long_rolling = df.rolling(window=100).mean()
                        ema_short = df.ewm(span=20, adjust=False).mean()

                        # Determine trading position based on EMA
                        trade_positions_raw = df - ema_short
                        trade_positions = trade_positions_raw.apply(np.sign) / 3  # Equal weighting
                        trade_positions_final = trade_positions.shift(1)  # Shift to simulate next-day trading

                        # Calculate asset and portfolio returns
                        asset_log_returns = np.log(df).diff()
                        portfolio_log_returns = trade_positions_final * asset_log_returns
                        cumulative_portfolio_log_returns = portfolio_log_returns.cumsum()
                        cumulative_portfolio_relative_returns = np.exp(cumulative_portfolio_log_returns) - 1

                        # Plot cumulative returns
                        cumulative_fig = go.Figure()
                        for ticker in asset_log_returns:
                            cumulative_fig.add_trace(go.Scatter(x=cumulative_portfolio_relative_returns.index,
                                                                y=100 * cumulative_portfolio_relative_returns[ticker],
                                                                mode='lines',
                                                                name=ticker))

                        cumulative_fig.update_layout(title='Cumulative Log Returns (%)',
                                                    xaxis_title='Date',
                                                    yaxis_title='Cumulative Log Returns (%)',
                                                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
                        st.plotly_chart(cumulative_fig)

                        # Comparing exact and approximate cumulative returns
                        cumulative_return_exact = cumulative_portfolio_relative_returns.sum(axis=1)
                        cumulative_log_return = cumulative_portfolio_log_returns.sum(axis=1)
                        cumulative_return_approx = np.exp(cumulative_log_return) - 1

                        # Plot exact vs approximate returns
                        approx_fig = go.Figure()
                        approx_fig.add_trace(go.Scatter(x=cumulative_return_exact.index,
                                                        y=100 * cumulative_return_exact,
                                                        mode='lines',
                                                        name='Exact'))
                        approx_fig.add_trace(go.Scatter(x=cumulative_return_approx.index,
                                                        y=100 * cumulative_return_approx,
                                                        mode='lines',
                                                        name='Approx'))

                        approx_fig.update_layout(title='Total Cumulative Relative Returns (%)',
                                                xaxis_title='Date',
                                                yaxis_title='Total Cumulative Relative Returns (%)',
                                                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
                        st.plotly_chart(approx_fig)

                        # Function to print portfolio statistics
                        def print_portfolio_statistics(portfolio_returns, num_of_years):
                            total_return = portfolio_returns[-1]
                            avg_yearly_return = (1 + total_return) ** (1 / num_of_years) - 1
                            st.write(f'Total Portfolio Return: {total_return * 100:.2f}%')
                            st.write(f'Average Yearly Return: {avg_yearly_return * 100:.2f}%')

                        # Printing statistics for EMA crossover strategy
                        print_portfolio_statistics(cumulative_return_exact, num_of_years)
                if more_input == "No":
                    st.error("The EMA crossover cannot proceed without a comparison")

            if pred_option_portfolio_strategies == "Factor Analysis":
                tickers = []
                ticker = st.text_input("Enter the ticker for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                    tickers.append(ticker)
                more_input = st.selectbox("Please Add one/more ticker(s) for comparison", ("","Yes", "No"))
                if more_input == "Yes":
                    ticker_2 =  st.text_input("Enter another ticker to continue the investigation")
                    tickers.append(ticker_2)
                    portfolio = st.number_input("Enter the portfolio size in USD")
                    if portfolio:
                        st.write(f"The portfolio size in USD Captured is : {portfolio}")
                    min_date = datetime(1980, 1, 1)
                    # Date input widget with custom minimum date
                    col1, col2 = st.columns([2, 2])
                    with col1:
                        start_date = st.date_input("Start date:", min_value=min_date)
                    with col2:
                        end_date = st.date_input("End Date:")
                    years = end_date.year - start_date.year
                    st.success(f"years captured : {years}")
                    if st.button("Check"):

                        # Setting plot aesthetics
                        sns.set(style='darkgrid', context='talk', palette='Dark2')

                        # Defining the time frame for data collection
                        end_date = dt.datetime.now()
                        start_date = end_date - dt.timedelta(days=365 * 7)

                        # List of stock symbols for factor analysis
                        symbols = tickers

                        # Fetching adjusted close prices for the specified symbols
                        df = pd.DataFrame({symbol: yf.download(symbol, start_date, end_date)['Adj Close']
                                        for symbol in symbols})

                        # Initializing FactorAnalyzer and fitting it to our data
                        fa = FactorAnalyzer(rotation=None, n_factors=df.shape[1])
                        fa.fit(df.dropna())

                        # Extracting communalities, eigenvalues, and factor loadings
                        communalities = fa.get_communalities()
                        eigenvalues, _ = fa.get_eigenvalues()
                        loadings = fa.loadings_

                        # Plotting the Scree plot to assess the number of factors
                        # Plotting the Scree plot to assess the number of factors
                        scree_fig = go.Figure()
                        scree_fig.add_trace(go.Scatter(x=list(range(1, df.shape[1] + 1)),
                                                    y=eigenvalues,
                                                    mode='markers+lines',
                                                    name='Eigenvalues',
                                                    marker=dict(color='blue')))
                        scree_fig.update_layout(title='Scree Plot',
                                                xaxis_title='Number of Factors',
                                                yaxis_title='Eigenvalue',
                                                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
                        st.plotly_chart(scree_fig)

                        # Bartlett's test of sphericity
                        chi_square_value, p_value = calculate_bartlett_sphericity(df.dropna())
                        st.write('Bartlett sphericity test:\nChi-square value:', chi_square_value, '\nP-value:', p_value)

                        # Kaiser-Meyer-Olkin (KMO) test
                        kmo_all, kmo_model = calculate_kmo(df.dropna())
                        st.write('Kaiser-Meyer-Olkin (KMO) Test:\nOverall KMO:', kmo_all, '\nKMO per variable:', kmo_model)

                        # Printing results
                        st.write("\nFactor Analysis Results:")
                        st.write("\nCommunalities:\n", communalities)
                        st.write("\nFactor Loadings:\n", loadings)
                if more_input == "No":
                    st.error("The EMA crossover cannot proceed without a comparison")


            if pred_option_portfolio_strategies == "Financial Signal Analysis":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Constants for analysis
                    index = 'SPY'  # S&P500 as the index for comparison
                    num_of_years = years  # Number of years for historical data
                    start = start_date

                    # Download historical stock prices
                    stock_data = yf.download(ticker, start=start)['Adj Close']
                    # Plotting stock prices and their distribution
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=stock_data.index, y=stock_data.values, mode='lines', name=f'{ticker.upper()} Price'))
                    fig1.update_layout(title=f'{ticker.upper()} Price', xaxis_title='Date', yaxis_title='Price')
                    st.plotly_chart(fig1)

                    fig2 = go.Figure()
                    fig2.add_trace(go.Histogram(x=stock_data, name=f'{ticker.upper()} Price Distribution'))
                    fig2.update_layout(title=f'{ticker.upper()} Price Distribution', xaxis_title='Price', yaxis_title='Frequency')
                    st.plotly_chart(fig2)

                    # Calculating and plotting stock returns
                    stock_returns = stock_data.apply(np.log).diff(1)
                    fig3 = go.Figure()
                    fig3.add_trace(go.Scatter(x=stock_returns.index, y=stock_returns.values, mode='lines', name=f'{ticker.upper()} Returns'))
                    fig3.update_layout(title=f'{ticker.upper()} Returns', xaxis_title='Date', yaxis_title='Returns')
                    st.plotly_chart(fig3)

                    fig4 = go.Figure()
                    fig4.add_trace(go.Histogram(x=stock_returns, name=f'{ticker.upper()} Returns Distribution'))
                    fig4.update_layout(title=f'{ticker.upper()} Returns Distribution', xaxis_title='Returns', yaxis_title='Frequency')
                    st.plotly_chart(fig4)

                    # Rolling statistics for stock returns
                    rolling_window = 22
                    rolling_mean = stock_returns.rolling(rolling_window).mean()
                    rolling_std = stock_returns.rolling(rolling_window).std()
                    rolling_skew = stock_returns.rolling(rolling_window).skew()
                    rolling_kurtosis = stock_returns.rolling(rolling_window).kurt()

                    # Combining rolling statistics into a DataFrame
                    signals = pd.concat([rolling_mean, rolling_std, rolling_skew, rolling_kurtosis], axis=1)
                    signals.columns = ['Mean', 'Std Dev', 'Skewness', 'Kurtosis']

                    fig5 = go.Figure()
                    for col in signals.columns:
                        fig5.add_trace(go.Scatter(x=signals.index, y=signals[col], mode='lines', name=col))
                    fig5.update_layout(title='Rolling Statistics for Stock Returns', xaxis_title='Date', yaxis_title='Value')
                    st.plotly_chart(fig5)

                    # Volatility analysis for S&P500
                    index_data = yf.download(index, start=start)['Adj Close']
                    index_returns = index_data.apply(np.log).diff(1)
                    index_volatility = index_returns.rolling(rolling_window).std()

                    # Drop NaN values from index_volatility
                    index_volatility.dropna(inplace=True)

                    # Gaussian Mixture Model on S&P500 volatility
                    gmm_labels = GaussianMixture(2).fit_predict(index_volatility.values.reshape(-1, 1))
                    index_data = index_data.reindex(index_volatility.index)

                    # Plotting volatility regimes
                    fig6 = go.Figure()
                    fig6.add_trace(go.Scatter(x=index_data[gmm_labels == 0].index,
                                            y=index_data[gmm_labels == 0].values,
                                            mode='markers',
                                            marker=dict(color='blue'),
                                            name='Regime 1'))
                    fig6.add_trace(go.Scatter(x=index_data[gmm_labels == 1].index,
                                            y=index_data[gmm_labels == 1].values,
                                            mode='markers',
                                            marker=dict(color='red'),
                                            name='Regime 2'))
                    fig6.update_layout(title=f'{index} Volatility Regimes (Gaussian Mixture)',
                                    xaxis_title='Date',
                                    yaxis_title='Price',
                                    showlegend=True)
                    st.plotly_chart(fig6)
            if pred_option_portfolio_strategies == "Geometric Brownian Motion":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Constants for analysis
                    num_of_years = years  # Number of years for historical data
                    start = start_date
                    stock = ticker
                    index = '^GSPC'

                    # Fetching historical data from Yahoo Finance
                    stock_data = yf.download(stock, start_date, end_date)
                    index_data = yf.download(index, start_date, end_date)

                    # Resampling data to monthly frequency and calculating returns
                    stock_monthly = stock_data.resample('M').last()
                    index_monthly = index_data.resample('M').last()
                    combined_data = pd.DataFrame({'Stock': stock_monthly['Adj Close'], 
                                                'Index': index_monthly['Adj Close']})
                    combined_returns = combined_data.pct_change().dropna()

                    # Calculating covariance matrix for the returns
                    cov_matrix = np.cov(combined_returns['Stock'], combined_returns['Index'])

                    # Class for Geometric Brownian Motion simulation
                    class GBM:
                        def __init__(self, initial_price, drift, volatility, time_period, total_time):
                            self.initial_price = initial_price
                            self.drift = drift
                            self.volatility = volatility
                            self.time_period = time_period
                            self.total_time = total_time
                            self.simulate()

                        def simulate(self):
                            self.prices = [self.initial_price]
                            while self.total_time > 0:
                                dS = self.prices[-1] * (self.drift * self.time_period + 
                                                        self.volatility * np.random.normal(0, math.sqrt(self.time_period)))
                                self.prices.append(self.prices[-1] + dS)
                                self.total_time -= self.time_period

                    # Parameters for GBM simulation
                    num_simulations = 20
                    initial_price = stock_data['Adj Close'][-1]
                    drift = 0.24
                    volatility = math.sqrt(cov_matrix[0, 0])
                    time_period = 1 / 365
                    total_time = 1

                    # Running multiple GBM simulations
                    simulations = [GBM(initial_price, drift, volatility, time_period, total_time) for _ in range(num_simulations)]

                    # Plotting the simulations
                    fig = go.Figure()
                    for i, sim in enumerate(simulations):
                        fig.add_trace(go.Scatter(x=np.arange(len(sim.prices)), y=sim.prices, mode='lines', name=f'Simulation {i+1}'))

                    fig.add_trace(go.Scatter(x=np.arange(len(sim.prices)), y=[initial_price] * len(sim.prices),
                                            mode='lines', name='Initial Price', line=dict(color='red', dash='dash')))
                    fig.update_layout(title=f'Geometric Brownian Motion for {stock.upper()}',
                                    xaxis_title='Time Steps',
                                    yaxis_title='Price')
                    st.plotly_chart(fig)

            
            if pred_option_portfolio_strategies == "Long Hold Stats Analysis":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Constants for analysis         
                    # Function to download stock data
                    def download_stock_data(symbol, start, end):
                        return yf.download(symbol, start, end)['Adj Close']

                    # Function to calculate investment statistics
                    def calculate_investment_stats(df, investment_amount, symbol):
                        # Calculate number of shares bought and investment values
                        shares = int(investment_amount / df.iloc[0])
                        begin_value = round(shares * df.iloc[0], 2)
                        current_value = round(shares * df.iloc[-1], 2)

                        # Calculate daily returns and various statistics
                        returns = df.pct_change().dropna()
                        stats = {
                            'mean': round(returns.mean() * 100, 2),
                            'std_dev': round(returns.std() * 100, 2),
                            'skew': round(returns.skew(), 2),
                            'kurt': round(returns.kurtosis(), 2),
                            'total_return': round((1 + returns).cumprod().iloc[-1], 4) * 100
                        }
                        return shares, begin_value, current_value, stats

                    # User inputs
                    symbol = ticker
                    num_of_years = years
                    investment_amount = portfolio

                    # Calculate date range
                    start = dt.datetime.now() - dt.timedelta(days=int(365.25 * num_of_years))
                    end = dt.datetime.now()

                    # Download and process stock data
                    df = download_stock_data(ticker, start_date, end_date)
                    shares, begin_value, current_value, stats = calculate_investment_stats(df, investment_amount, symbol)

                    # Print statistics
                    st.write(f'\nNumber of Shares for {symbol}: {shares}')
                    st.write(f'Beginning Value: ${begin_value}')
                    st.write(f'Current Value: ${current_value}')
                    st.write(f"\nStatistics:\nMean: {stats['mean']}%\nStd. Dev: {stats['std_dev']}%\nSkew: {stats['skew']}\nKurt: {stats['kurt']}\nTotal Return: {stats['total_return']}%")

                    # Plotting returns and other statistics
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df.pct_change(), mode='lines', name='Daily Returns'))
                    fig.update_layout(title=f'{symbol} Daily Returns', xaxis_title='Date', yaxis_title='Returns')
                    st.plotly_chart(fig)

            if pred_option_portfolio_strategies == "LS DCA Analysis":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    def fetch_stock_data(symbol, start, end):
                        return yf.download(symbol, start, end)

                    # Lump Sum Investment Function
                    def lump_sum_investment(df, invest_date, principal):
                        invest_price = df.loc[invest_date]['Adj Close']
                        current_price = df['Adj Close'][-1]
                        return principal * ((current_price / invest_price) - 1)

                    # Dollar-Cost Averaging Function
                    def dca_investment(df, invest_date, periods, freq, principal):
                        dca_dates = pd.date_range(invest_date, periods=periods, freq=freq)
                        dca_dates = dca_dates[dca_dates < df.index[-1]]
                        cut_off_count = 12 - len(dca_dates)
                        cut_off_value = cut_off_count * (principal / periods)
                        dca_value = cut_off_value
                        for date in dca_dates:
                            trading_date = df.index[df.index.searchsorted(date)]
                            dca_value += lump_sum_investment(df, trading_date, principal / periods)
                        return dca_value

                    # User Input
                    symbol = ticker
                    years = years
                    principal = portfolio

                    # Set dates for data retrieval
                    start_date = start_date
                    end_date = end_date

                    # Fetch Data
                    stock_data = fetch_stock_data(symbol, start_date, end_date)

                    # Analysis for Lump Sum and DCA
                    lump_sum_values = [lump_sum_investment(stock_data, date, principal) for date in stock_data.index]
                    dca_values = [dca_investment(stock_data, date, 12, '30D', principal) for date in stock_data.index]
                
                    fig1 = go.Figure()
                    fig1.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Adj Close'], mode='lines', name=f'{symbol} Price'))
                    fig1.update_layout(title=f'{symbol} Stock Price', yaxis_title='Price', yaxis_tickprefix='$', yaxis_tickformat=',.0f')

                    fig2 = go.Figure()
                    fig2.add_trace(go.Scatter(x=stock_data.index, y=lump_sum_values, mode='lines', name='Lump Sum Investment'))
                    fig2.add_trace(go.Scatter(x=stock_data.index, y=dca_values, mode='lines', name='DCA Investment'))
                    fig2.update_layout(title='Lump Sum vs. DCA Investment Value', yaxis_title='Investment Value', yaxis_tickprefix='$', yaxis_tickformat=',.0f')

                    fig3 = go.Figure()
                    fig3.add_trace(go.Scatter(x=stock_data.index, y=np.array(lump_sum_values) - np.array(dca_values), mode='lines', name='Difference in Investment Values'))
                    fig3.update_layout(title='Difference Between Lump Sum and DCA', yaxis_title='Difference', yaxis_tickprefix='$', yaxis_tickformat=',.0f')

                    # Display plots in Streamlit
                    st.plotly_chart(fig1)
                    st.plotly_chart(fig2)
                    st.plotly_chart(fig3)


            if pred_option_portfolio_strategies == "Monte Carlo":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Function to download stock data
                    symbol = ticker
                    df = yf.download(symbol, start_date, end_date)

                    # Function to calculate annual volatility
                    def annual_volatility(df):
                        quote = df['Close']
                        returns = quote.pct_change()
                        return returns.std() * np.sqrt(252)

                    # Function to calculate CAGR
                    def cagr(df):
                        quote = df['Close']
                        days = (quote.index[-1] - quote.index[0]).days
                        return ((((quote[-1]) / quote[1])) ** (365.0/days)) - 1

                    # Monte Carlo Simulation Function
                    def monte_carlo_simulation(simulations, days_predicted):
                        mu = cagr(df)
                        vol = annual_volatility(df)
                        start_price = df['Close'][-1]

                        results = []
                        
                        # Run simulations
                        for _ in range(simulations):
                            prices = [start_price]
                            for _ in range(days_predicted):
                                shock = np.random.normal(mu / days_predicted, vol / math.sqrt(days_predicted))
                                prices.append(prices[-1] * (1 + shock))
                            results.append(prices[-1])

                        return pd.DataFrame({
                            "Results": results,
                            "Percentile 5%": np.percentile(results, 5),
                            "Percentile 95%": np.percentile(results, 95)
                        })

                
                    
                    symbol = ticker
                    start_date = start_date
                    end_date = end_date
                    simulations = 1000
                    days_predicted = 252

                    # Perform Monte Carlo Simulation
                    simulation_results = monte_carlo_simulation(simulations, days_predicted)

                    # Plotting
                    fig = go.Figure()
                    fig.add_trace(go.Histogram(x=simulation_results['Results'], histnorm='probability'))
                    fig.update_layout(title=f"{symbol} Monte Carlo Simulation Histogram", xaxis_title="Price", yaxis_title="Probability Density")
                    st.plotly_chart(fig)

            if pred_option_portfolio_strategies == "Moving Average Crossover Signals":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Function to retrieve stock data
                    def get_stock_data(ticker, start_date, end_date):
                        return yf.download(ticker, start_date, end_date)

                    # Function to calculate Simple Moving Averages (SMA)
                    def calculate_sma(data, window):
                        return data['Close'].rolling(window=window).mean()

                    # Function to generate buy and sell signals
                    def generate_signals(data):
                        signal_buy = []
                        signal_sell = []
                        flag = -1

                        for i in range(len(data)):
                            if data['SMA 50'][i] > data['SMA 200'][i] and flag != 1:
                                signal_buy.append(data['Close'][i])
                                signal_sell.append(np.nan)
                                flag = 1
                            elif data['SMA 50'][i] < data['SMA 200'][i] and flag != 0:
                                signal_buy.append(np.nan)
                                signal_sell.append(data['Close'][i])
                                flag = 0
                            else:
                                signal_buy.append(np.nan)
                                signal_sell.append(np.nan)

                        return signal_buy, signal_sell

                    # Main function to run the analysis
                    def main():
                        st.title("Stock Data Analysis with Moving Averages and Signals")

                        ticker = st.text_input("Enter a ticker:")
                        if not ticker:
                            st.warning("Please enter a valid ticker.")
                            return

                        num_of_years = 6
                        start_date = dt.datetime.now() - dt.timedelta(int(365.25 * num_of_years))
                        end_date = dt.datetime.now()

                        # Retrieve and process stock data
                        stock_data = get_stock_data(ticker, start_date, end_date)
                        stock_data['SMA 50'] = calculate_sma(stock_data, 50)
                        stock_data['SMA 200'] = calculate_sma(stock_data, 200)

                        # Generate buy and sell signals
                        buy_signals, sell_signals = generate_signals(stock_data)

                        # Plotting
                        fig = go.Figure()

                        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close Price'))
                        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA 50'], mode='lines', name='SMA 50'))
                        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA 200'], mode='lines', name='SMA 200'))
                        fig.add_trace(go.Scatter(x=stock_data.index, y=buy_signals, mode='markers', name='Buy Signal', marker=dict(symbol='triangle-up', color='green')))
                        fig.add_trace(go.Scatter(x=stock_data.index, y=sell_signals, mode='markers', name='Sell Signal', marker=dict(symbol='triangle-down', color='red')))

                        fig.update_layout(title=f'{ticker.upper()} Close Price History with Buy & Sell Signals',
                                        xaxis_title='Date',
                                        yaxis_title='Close Price')

                        st.plotly_chart(fig)
            
            if pred_option_portfolio_strategies == "Moving Average Strategy":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                
                    # Function to download stock data
                    def download_stock_data(ticker, start_date, end_date):
                        return yf.download(ticker, start_date, end_date)

                    # Function to calculate moving averages
                    def calculate_moving_averages(data, windows):
                        for window in windows:
                            data[f'SMA_{window}'] = data['Adj Close'].rolling(window).mean()
                        return data

                    # Main function
                    def main():
                        st.title("Stock Data Analysis with Moving Averages")

                        ticker = st.text_input("Enter a ticker:")
                        if not ticker:
                            st.warning("Please enter a valid ticker.")
                            return

                        num_of_years = 6
                        start_date = dt.datetime.now() - dt.timedelta(int(365.25 * num_of_years))
                        end_date = dt.datetime.now()

                        # Download and process stock data
                        stock_data = download_stock_data(ticker, start_date, end_date)
                        stock_data = calculate_moving_averages(stock_data, [20, 40, 80])

                        # Plotting
                        fig = go.Figure()
                        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Adj Close'], mode='lines', name='Close Price'))
                        for window in [20, 40, 80]:
                            fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data[f'SMA_{window}'], mode='lines', name=f'{window}-days SMA'))
                        
                        fig.update_layout(title=f'{ticker.upper()} Close Price with Moving Averages',
                                        xaxis_title='Date',
                                        yaxis_title='Close Price')

                        st.plotly_chart(fig)

            if pred_option_portfolio_strategies == "Optimal Portfolio":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Function to download stock data and calculate annual returns
                    def annual_returns(symbols, start_date, end_date):
                        df = yf.download(symbols, start_date, end_date)['Adj Close']
                        log_rets = np.log(df / df.shift(1))
                        return np.exp(log_rets.groupby(log_rets.index.year).sum()) - 1

                    # Function to calculate portfolio variance
                    def portfolio_var(returns, weights):
                        cov_matrix = np.cov(returns.T)
                        return np.dot(weights.T, np.dot(cov_matrix, weights))

                    # Function to calculate Sharpe ratio
                    def sharpe_ratio(returns, weights, rf_rate):
                        portfolio_return = np.dot(returns.mean(), weights)
                        portfolio_volatility = np.sqrt(portfolio_var(returns, weights))
                        return (portfolio_return - rf_rate) / portfolio_volatility

                    # Function to optimize portfolio for maximum Sharpe ratio
                    def optimize_portfolio(returns, initial_weights, rf_rate):
                        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
                        bounds = tuple((0, 1) for _ in range(len(initial_weights)))
                        optimized = fmin(lambda x: -sharpe_ratio(returns, x, rf_rate), initial_weights, disp=False)
                        return optimized

                    # Main function to execute the script
                    def main():
                        st.title("Optimal Portfolio Optimization")

                        symbols = st.text_input("Enter stock symbols (comma-separated):")
                        start_date = st.date_input("Enter start date:")
                        end_date = st.date_input("Enter end date:")
                        rf_rate = st.number_input("Enter risk-free rate (in decimal):", min_value=0.0, value=0.003)

                        if not symbols or not start_date or not end_date:
                            st.warning("Please provide all required inputs.")
                            return

                        symbols = symbols.split(',')

                        # Calculate annual returns
                        returns = annual_returns(symbols, start_date, end_date)

                        # Initialize equal weights
                        initial_weights = np.ones(len(symbols)) / len(symbols)

                        # Calculate equal weighted portfolio Sharpe ratio
                        equal_weighted_sharpe = sharpe_ratio(returns, initial_weights, rf_rate)
                        
                        # Optimize portfolio
                        optimal_weights = optimize_portfolio(returns, initial_weights, rf_rate)
                        optimal_sharpe = sharpe_ratio(returns, optimal_weights, rf_rate)

                        # Display results
                        st.write(f"Equal Weighted Portfolio Sharpe Ratio: {equal_weighted_sharpe}")
                        st.write(f"Optimal Portfolio Weights: {optimal_weights}")
                        st.write(f"Optimal Portfolio Sharpe Ratio: {optimal_sharpe}")

        
            if pred_option_portfolio_strategies == "Optimized Bollinger Bands":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                # Function to download stock data from Yahoo Finance
                    def get_stock_data(ticker):
                        df = yf.download(ticker)
                        df = df[['Adj Close']]
                        return df

                    # Function to add Bollinger Bands to DataFrame
                    def add_bollinger_bands(df, window_size=20, num_std_dev=2):
                        df['SMA'] = df['Adj Close'].rolling(window=window_size).mean()
                        df['Upper Band'] = df['SMA'] + (df['Adj Close'].rolling(window=window_size).std() * num_std_dev)
                        df['Lower Band'] = df['SMA'] - (df['Adj Close'].rolling(window=window_size).std() * num_std_dev)
                        return df

                    # Function to plot stock prices with Bollinger Bands
                    def plot_with_bollinger_bands(df, ticker):
                        fig = go.Figure()
                        fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'], mode='lines', name=f'{ticker} Adjusted Close'))
                        fig.add_trace(go.Scatter(x=df.index, y=df['SMA'], mode='lines', name='20 Day SMA'))
                        fig.add_trace(go.Scatter(x=df.index, y=df['Upper Band'], mode='lines', name='Upper Bollinger Band'))
                        fig.add_trace(go.Scatter(x=df.index, y=df['Lower Band'], mode='lines', name='Lower Bollinger Band'))
                        fig.update_layout(title=f'{ticker} Stock Price with Bollinger Bands',
                                        xaxis_title='Date',
                                        yaxis_title='Price')
                        st.plotly_chart(fig)

                    # Main function to execute the script
                    st.title("Stock Price with Bollinger Bands")

                    ticker = st.text_input("Enter stock ticker:")
                    if not ticker:
                        st.warning("Please enter a valid ticker.")
                        return

                    df = get_stock_data(ticker)
                    df = add_bollinger_bands(df)

                    plot_with_bollinger_bands(df, ticker)

            if pred_option_portfolio_strategies == "Pairs Trading":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
        
                    # Function to download stock data from Yahoo Finance
                    def download_stock_data(symbols, start_date, end_date):
                        """Download historical stock data for given symbols from Yahoo Finance."""
                        stock_data = yf.download(symbols, start=start_date, end=end_date)['Adj Close']
                        return stock_data.dropna()

                    # Function to identify cointegrated pairs of stocks
                    def find_cointegrated_pairs(data):
                        """Identify cointegrated pairs of stocks."""
                        n = data.shape[1]
                        score_matrix, pvalue_matrix = np.zeros((n, n)), np.ones((n, n))
                        pairs = []
                        for i in range(n):
                            for j in range(i+1, n):
                                S1, S2 = data[data.columns[i]], data[data.columns[j]]
                                _, pvalue, _ = coint(S1, S2)
                                score_matrix[i, j], pvalue_matrix[i, j] = _, pvalue
                                if pvalue < 0.05:  # Using a p-value threshold of 0.05
                                    pairs.append((data.columns[i], data.columns[j]))
                        return score_matrix, pvalue_matrix, pairs

                    # Function to plot heatmap of p-values for cointegration test using Plotly
                    def plot_cointegration_heatmap(pvalues, tickers):
                        """Plot heatmap of p-values for cointegration test."""
                        fig = go.Figure(data=go.Heatmap(
                            z=pvalues,
                            x=tickers,
                            y=tickers,
                            colorscale='Viridis',
                            zmin=0,
                            zmax=0.05
                        ))
                        fig.update_layout(title="P-Values for Pairs Cointegration Test")
                        return fig

                    # Pairs Trading Section
                    def pairs_trading():
                        st.title("Pairs Trading")

                        # Inputs
                        ticker = st.text_input("Please enter the ticker needed for investigation")
                        portfolio = st.number_input("Enter the portfolio size in USD")
                        min_date = datetime.datetime(1980, 1, 1)
                        start_date = st.date_input("Start date:", min_value=min_date)
                        end_date = st.date_input("End Date:")
                        years = end_date.year - start_date.year

                        if st.button("Check"):
                            # Download and process data
                            data = download_stock_data([ticker], start_date, end_date)

                            # Find cointegrated pairs
                            _, pvalues, pairs = find_cointegrated_pairs(data)

                            # Plot heatmap of p-values
                            fig = plot_cointegration_heatmap(pvalues, [ticker])
                            st.plotly_chart(fig)

                            # Display the found pairs
                            st.write("Cointegrated Pairs:", pairs)
                    
            if pred_option_portfolio_strategies == "Portfolio Analysis":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"): 
                    # Override yfinance with Pandas Datareader's Yahoo Finance API
                    def get_historical_prices(symbols, start_date, end_date):
                        """Retrieve historical stock prices for specified symbols."""
                        return yf.download(symbols, start=start_date, end=end_date)['Adj Close']

                    def calculate_daily_returns(prices):
                        """Calculate daily returns from stock prices."""
                        return np.log(prices / prices.shift(1))

                    def calculate_monthly_returns(daily_returns):
                        """Calculate monthly returns from daily returns."""
                        return np.exp(daily_returns.groupby(lambda date: date.month).sum()) - 1

                    def calculate_annual_returns(daily_returns):
                        """Calculate annual returns from daily returns."""
                        return np.exp(daily_returns.groupby(lambda date: date.year).sum()) - 1

                    def portfolio_variance(returns, weights=None):
                        """Calculate the variance of a portfolio."""
                        if weights is None:
                            weights = np.ones(len(returns.columns)) / len(returns.columns)
                        covariance_matrix = np.cov(returns.T)
                        return np.dot(weights, np.dot(covariance_matrix, weights))

                    def sharpe_ratio(returns, weights=None, risk_free_rate=0.001):
                        """Calculate the Sharpe ratio of a portfolio."""
                        if weights is None:
                            weights = np.ones(len(returns.columns)) / len(returns.columns)
                        port_var = portfolio_variance(returns, weights)
                        port_return = np.dot(returns.mean(), weights)
                        return (port_return - risk_free_rate) / np.sqrt(port_var)

                    # Example usage
                    symbols = ['AAPL', 'MSFT', 'GOOGL']
                    start_date = dt.datetime.now() - dt.timedelta(days=365*5)
                    end_date = dt.datetime.now()

                    # Fetch historical data
                    historical_prices = get_historical_prices(symbols, start_date, end_date)

                    # Calculate returns
                    daily_returns = calculate_daily_returns(historical_prices)
                    monthly_returns = calculate_monthly_returns(daily_returns)
                    annual_returns = calculate_annual_returns(daily_returns)

                    # Calculate portfolio metrics
                    portfolio_variance = portfolio_variance(annual_returns)
                    portfolio_sharpe_ratio = sharpe_ratio(daily_returns)

                    # Display results
                    st.write(f"Portfolio Variance: {portfolio_variance}")
                    st.write(f"Portfolio Sharpe Ratio: {portfolio_sharpe_ratio}")

                    # Plot historical prices using Plotly
                    fig = go.Figure()
                    for symbol in symbols:
                        fig.add_trace(go.Scatter(x=historical_prices.index, y=historical_prices[symbol], mode='lines', name=symbol))

                    fig.update_layout(title="Historical Prices",
                                    xaxis_title="Date",
                                    yaxis_title="Adjusted Closing Price",
                                    legend_title="Symbols")
                    st.plotly_chart(fig)


            if pred_option_portfolio_strategies == "Portfolio Optimization":
                tickers = []
                ticker = st.text_input("Enter the ticker for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                    tickers.append(ticker)
                more_input = st.selectbox("Please Add one/more ticker(s) for comparison", ("","Yes", "No"))
                if more_input == "Yes":
                    ticker_2 =  st.text_input("Enter another ticker to continue the investigation")
                    tickers.append(ticker_2)
                    portfolio = st.number_input("Enter the portfolio size in USD")
                    if portfolio:
                        st.write(f"The portfolio size in USD Captured is : {portfolio}")
                    min_date = datetime(1980, 1, 1)
                    # Date input widget with custom minimum date
                    col1, col2 = st.columns([2, 2])
                    with col1:
                        start_date = st.date_input("Start date:", min_value=min_date)
                    with col2:
                        end_date = st.date_input("End Date:")
                    years = end_date.year - start_date.year
                    st.success(f"years captured : {years}")
                    if st.button("Check"):


                        # Registering converters for using matplotlib's plot_date() function.
                        register_matplotlib_converters()

                        # Setting display options for pandas
                        pd.set_option("display.max_columns", None)
                        pd.set_option("display.max_rows", None)

                        # Defining stocks to include in the portfolio
                        stocks = tickers

                        # Getting historical data from Yahoo Finance
                        start = start_date
                        end = end_date
                        df = yf.download(stocks, start=start, end=end)["Close"]

                        # Calculating daily returns of each stock
                        returns = df.pct_change()

                        # Define a function to generate random portfolios
                        def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
                            results = np.zeros((3, num_portfolios))
                            weights_record = []
                            for i in range(num_portfolios):
                                weights = np.random.random(n)
                                weights /= np.sum(weights)
                                weights_record.append(weights)
                                portfolio_std_dev, portfolio_return = portfolio_performance(
                                    weights, mean_returns, cov_matrix
                                )
                                results[0, i] = portfolio_std_dev
                                results[1, i] = portfolio_return
                                results[2, i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
                            return results, weights_record

                        # Calculating mean returns and covariance matrix of returns
                        mean_returns = returns.mean()
                        cov_matrix = returns.cov()

                        # Setting the number of random portfolios to generate and the risk-free rate
                        num_portfolios = 50000
                        risk_free_rate = 0.021

                        # Define a function to calculate the negative Sharpe ratio
                        def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
                            p_var, p_ret = portfolio_performance(weights, mean_returns, cov_matrix)
                            return -(p_ret - risk_free_rate) / p_var

                        # Define a function to find the portfolio with maximum Sharpe ratio
                        def max_sharpe_ratio(mean_returns, cov_matrix, risk_free_rate):
                            num_assets = len(mean_returns)
                            args = (mean_returns, cov_matrix, risk_free_rate)
                            constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
                            bound = (0.0, 1.0)
                            bounds = tuple(bound for asset in range(num_assets))
                            result = sco.minimize(
                                neg_sharpe_ratio,
                                num_assets
                                * [
                                    1.0 / num_assets,
                                ],
                                args=args,
                                method="SLSQP",
                                bounds=bounds,
                                constraints=constraints,
                            )
                            return result

                        # Helper function to calculate portfolio performance
                        def portfolio_performance(weights, mean_returns, cov_matrix):
                            returns = np.sum(mean_returns * weights) * 252
                            std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
                            return std_dev, returns

                        # Calculate portfolio volatility
                        def portfolio_volatility(weights, mean_returns, cov_matrix):
                            return portfolio_performance(weights, mean_returns, cov_matrix)[0]

                        # Function to find portfolio with minimum variance
                        def min_variance(mean_returns, cov_matrix):
                            num_assets = len(mean_returns)
                            args = (mean_returns, cov_matrix)
                            bounds = tuple((0.0, 1.0) for asset in range(num_assets))
                            constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

                            result = sco.minimize(portfolio_volatility, [1./num_assets]*num_assets,
                                                args=args, method='SLSQP', bounds=bounds, constraints=constraints)
                            return result

                        # Function to calculate efficient return
                        def efficient_return(mean_returns, cov_matrix, target_return):
                            num_assets = len(mean_returns)
                            args = (mean_returns, cov_matrix)
                            bounds = tuple((0.0, 1.0) for asset in range(num_assets))
                            constraints = [{'type': 'eq', 'fun': lambda x: portfolio_performance(x, mean_returns, cov_matrix)[1] - target_return},
                                        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]

                            result = sco.minimize(portfolio_volatility, [1./num_assets]*num_assets,
                                                args=args, method='SLSQP', bounds=bounds, constraints=constraints)
                            return result

                        # Function to construct efficient frontier
                        def efficient_frontier(mean_returns, cov_matrix, returns_range):
                            efficient_portfolios = []
                            for ret in returns_range:
                                efficient_portfolios.append(efficient_return(mean_returns, cov_matrix, ret))
                            return efficient_portfolios

                        # Calculating efficient frontier
                        target_returns = np.linspace(0.0, 0.5, 100)
                        efficient_portfolios = efficient_frontier(mean_returns, cov_matrix, target_returns)

                        # Extracting volatility and return for each portfolio
                        volatility = [p['fun'] for p in efficient_portfolios]
                        returns = [portfolio_performance(p['x'], mean_returns, cov_matrix)[1] for p in efficient_portfolios]

                        # Plotting the efficient frontier
                        fig_efficient_frontier = go.Figure()
                        fig_efficient_frontier.add_trace(go.Scatter(x=volatility, y=returns, mode='lines', name='Efficient Frontier'))
                        fig_efficient_frontier.add_trace(go.Scatter(x=[p['fun'] for p in min_variance(mean_returns, cov_matrix)], y=[p['x'].mean() for p in min_variance(mean_returns, cov_matrix)], mode='markers', marker=dict(size=10, color='red'), name='Minimum Variance Portfolio'))
                        fig_efficient_frontier.update_layout(title='Efficient Frontier', xaxis_title='Volatility', yaxis_title='Return')
                        st.plotly_chart(fig_efficient_frontier)

                if pred_option_portfolio_strategies == "Portfolio VAR Simulation":
                    ticker = st.text_input("Please enter the ticker needed for investigation")
                    if ticker:
                        message = (f"Ticker captured : {ticker}")
                        st.success(message)
                    portfolio = st.number_input("Enter the portfolio size in USD")
                    if portfolio:
                        st.write(f"The portfolio size in USD Captured is : {portfolio}")
                    min_date = datetime(1980, 1, 1)
                    # Date input widget with custom minimum date
                    col1, col2 = st.columns([2, 2])
                    with col1:
                        start_date = st.date_input("Start date:", min_value=min_date)
                    with col2:
                        end_date = st.date_input("End Date:")
                    years = end_date.year - start_date.year
                    st.success(f"years captured : {years}")
                    if st.button("Check"):

                        # Define the tickers and time parameters
                        tickers = ['GOOGL', 'FB', 'AAPL', 'NFLX', 'AMZN']
                        Time = 1440  # Number of trading days in minutes
                        pvalue = 1000  # Portfolio value in dollars
                        num_of_years = 3
                        start_date = dt.datetime.now() - dt.timedelta(days=365.25 * num_of_years)
                        end_date = dt.datetime.now()

                        # Fetching and preparing stock data
                        price_data = [web.DataReader(ticker, start=start_date, end=end_date, data_source='yahoo')['Adj Close'] for ticker in tickers]
                        df_stocks = pd.concat(price_data, axis=1)
                        df_stocks.columns = tickers

                        # Calculating expected returns and covariance matrix
                        mu = expected_returns.mean_historical_return(df_stocks)
                        Sigma = risk_models.sample_cov(df_stocks)

                        # Portfolio Optimization using Efficient Frontier
                        ef = EfficientFrontier(mu, Sigma, weight_bounds=(0,1))
                        sharpe_pwt = ef.max_sharpe()
                        cleaned_weights = ef.clean_weights()

                        # Plotting Cumulative Returns of All Stocks
                        cum_returns = ((df_stocks.pct_change() + 1).cumprod() - 1)
                        fig_cum_returns = go.Figure()
                        for column in cum_returns.columns:
                            fig_cum_returns.add_trace(go.Scatter(x=cum_returns.index, y=cum_returns[column], mode='lines', name=column))
                        fig_cum_returns.update_layout(title='Cumulative Returns', xaxis_title='Date', yaxis_title='Cumulative Returns')
                        st.plotly_chart(fig_cum_returns)

                        # Portfolio VaR Simulation
                        ticker_returns = cum_returns.pct_change().dropna()
                        weighted_returns = ticker_returns.dot(np.array(list(cleaned_weights.values())))
                        portfolio_return = weighted_returns.mean()
                        portfolio_vol = weighted_returns.std()

                        # Simulating daily returns for VAR calculation
                        simulated_daily_returns = [np.random.normal(portfolio_return / Time, portfolio_vol / np.sqrt(Time), Time) for _ in range(10000)]

                        # Plotting Range of Returns in a Day
                        fig_returns_range = go.Figure()
                        for i in range(10000):
                            fig_returns_range.add_trace(go.Scatter(y=simulated_daily_returns[i], mode='lines', name=f'Simulation {i+1}'))
                        fig_returns_range.add_trace(go.Scatter(y=np.percentile(simulated_daily_returns, 5), mode='lines', name='5th Percentile', line=dict(color='red', dash='dash')))
                        fig_returns_range.add_trace(go.Scatter(y=np.percentile(simulated_daily_returns, 95), mode='lines', name='95th Percentile', line=dict(color='green', dash='dash')))
                        fig_returns_range.add_trace(go.Scatter(y=np.mean(simulated_daily_returns), mode='lines', name='Mean', line=dict(color='blue')))
                        fig_returns_range.update_layout(title=f'Range of Returns in a Day of {Time} Minutes', xaxis_title='Minute', yaxis_title='Returns')
                        st.plotly_chart(fig_returns_range)

                        # Histogram of Daily Returns
                        fig_hist_returns = go.Figure()
                        fig_hist_returns.add_trace(go.Histogram(x=simulated_daily_returns.flatten(), nbinsx=15))
                        fig_hist_returns.add_trace(go.Scatter(x=[np.percentile(simulated_daily_returns, 5), np.percentile(simulated_daily_returns, 5)], y=[0, 1500], mode='lines', name='5th Percentile', line=dict(color='red', dash='dash')))
                        fig_hist_returns.add_trace(go.Scatter(x=[np.percentile(simulated_daily_returns, 95), np.percentile(simulated_daily_returns, 95)], y=[0, 1500], mode='lines', name='95th Percentile', line=dict(color='green', dash='dash')))
                        fig_hist_returns.update_layout(title='Histogram of Daily Returns', xaxis_title='Returns', yaxis_title='Frequency')
                        st.plotly_chart(fig_hist_returns)

                        # Printing VaR results
                        st.write(f"5th Percentile: {np.percentile(simulated_daily_returns, 5)}")
                        st.write(f"95th Percentile: {np.percentile(simulated_daily_returns, 95)}")
                        st.write(f"Amount required to cover minimum losses for one day: ${pvalue * -np.percentile(simulated_daily_returns, 5)}")


            if pred_option_portfolio_strategies == "Risk Management":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                                
                    # Define the start and end dates for data retrieval
                    start = dt.datetime(2019, 1, 1)
                    now = dt.datetime.now()

                    # Define the moving averages and exponential moving averages to be used
                    smaUsed = [50, 200]
                    emaUsed = [21]

                    # User inputs for stock ticker and position
                    stock = st.text_input("Enter a ticker: ")
                    position = st.selectbox("Buy or Short?", ["Buy", "Short"]).lower()
                    AvgGain = st.number_input("Enter Your Average Gain (%)", value=0.0, step=0.1)
                    AvgLoss = st.number_input("Enter Your Average Loss (%)", value=0.0, step=0.1)

                    # Fetch historical data from Yahoo Finance
                    df = yf.download(stock, start=start, end=now)

                    # Calculate the maximum stop value and target returns based on user's position
                    if position == "buy":
                        close = df["Adj Close"][-1]
                        maxStop = close * (1 - AvgLoss / 100)
                        targets = [round(close * (1 + (i * AvgGain / 100)), 2) for i in range(1, 4)]
                    elif position == "short":
                        close = df["Adj Close"][-1]
                        maxStop = close * (1 + AvgLoss / 100)
                        targets = [round(close * (1 - (i * AvgGain / 100)), 2) for i in range(1, 4)]

                    # Calculate SMA and EMA for the stock
                    for x in smaUsed:
                        df[f"SMA_{x}"] = df["Adj Close"].rolling(window=x).mean()
                    for x in emaUsed:
                        df[f"EMA_{x}"] = df["Adj Close"].ewm(span=x, adjust=False).mean()

                    # Fetching the latest values of SMA, EMA, and 5 day low
                    sma_values = {f"SMA_{x}": round(df[f"SMA_{x}"][-1], 2) for x in smaUsed}
                    ema_values = {f"EMA_{x}": round(df[f"EMA_{x}"][-1], 2) for x in emaUsed}
                    low5 = round(min(df["Low"].tail(5)), 2)

                    # Calculate the performance metrics and checks
                    performance_checks = {}
                    for key, value in {**sma_values, **ema_values, "Low_5": low5}.items():
                        pf = round(((close / value) - 1) * 100, 2)
                        check = value > maxStop if position == "buy" else value < maxStop
                        performance_checks[key] = {"Performance": pf, "Check": check}

                    # Displaying the results
                    st.write(f"Current Stock: {stock} | Price: {round(close, 2)}")
                    st.write(" | ".join([f"{key}: {value}" for key, value in {**sma_values, **ema_values, 'Low_5': low5}.items()]))
                    st.write("-------------------------------------------------")
                    st.write(f"Max Stop: {round(maxStop, 2)}")
                    st.write(f"Price Targets: 1R: {targets[0]} | 2R: {targets[1]} | 3R: {targets[2]}")
                    for key, value in performance_checks.items():
                        st.write(f"From {key} {value['Performance']}% - {'Within' if value['Check'] else 'Outside'} Max Stop")


            if pred_option_portfolio_strategies == "RSI Trendline Strategy":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Define the date range for data retrieval
                    num_of_years = 10
                    start = datetime.datetime.now() - datetime.timedelta(days=365.25 * num_of_years)
                    end = datetime.datetime.now()

                    # Load stock symbols
                    @st.cache
                    def load_tickers():
                        stocklist = ti.tickers_sp500()
                        return [stock.replace(".", "-") for stock in stocklist]  # Adjusting ticker format for Yahoo Finance

                    stocklist = load_tickers()

                    # Initialize the DataFrame for exporting results
                    exportList = pd.DataFrame(columns=['Stock', "RSI", "200 Day MA"])

                    # Process a limited number of stocks for demonstration
                    for stock in stocklist[:5]:
                        time.sleep(1.5)  # To avoid hitting API rate limits
                        st.write(f"\npulling {stock}")

                        # Fetch stock data
                        df = yf.download(stock, start=start, end=end)

                        try:
                            # Calculate indicators: 200-day MA, RSI
                            df["SMA_200"] = df.iloc[:, 4].rolling(window=200).mean()
                            df["rsi"] = ta.RSI(df["Close"])
                            currentClose, moving_average_200, RSI = df["Adj Close"][-1], df["SMA_200"][-1], df["rsi"].tail(14).mean()
                            two_day_rsi_avg = (df.rsi[-1] + df.rsi[-2]) / 2

                            # Define entry criteria
                            if currentClose > moving_average_200 and two_day_rsi_avg < 33:
                                exportList = exportList.append({'Stock': stock, "RSI": RSI, "200 Day MA": moving_average_200}, ignore_index=True)
                                st.write(f"{stock} made the requirements")

                        except Exception as e:
                            st.write(e)  # Handling exceptions

                    # Displaying the exported list
                    st.write(exportList)


            if pred_option_portfolio_strategies == "RWB Strategy":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    emas_used = [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60]

                    def get_stock_data(ticker, num_of_years):
                        start_date = dt.date.today() - dt.timedelta(days=365.25 * num_of_years)
                        end_date = dt.datetime.now()
                        df = yf.download(ticker, start_date, end_date).dropna()
                        for ema in emas_used:
                            df[f"Ema_{ema}"] = df.iloc[:, 4].ewm(span=ema, adjust=False).mean()
                        return df.iloc[60:]

                    def rwb_strategy(df):
                        pos, num, percent_change = 0, 0, []
                        for i in df.index:
                            cmin = min(df[f"Ema_{ema}"][i] for ema in emas_used[:6])
                            cmax = max(df[f"Ema_{ema}"][i] for ema in emas_used[6:])
                            close = df["Adj Close"][i]
                            if cmin > cmax and pos == 0:
                                bp, pos = close, 1
                                st.write(f"Buying now at {bp}")
                            elif cmin < cmax and pos == 1:
                                pos, sp = 0, close
                                st.write(f"Selling now at {sp}")
                                percent_change.append((sp / bp - 1) * 100)
                            if num == df["Adj Close"].count() - 1 and pos == 1:
                                pos, sp = 0, close
                                st.write(f"Selling now at {sp}")
                                percent_change.append((sp / bp - 1) * 100)
                            num += 1
                        return percent_change

                    st.title("RWB Strategy Visualization")

                    stock = st.text_input("Enter a ticker:", "AAPL")
                    num_of_years = st.number_input("Enter number of years:", min_value=1, max_value=10, step=1, value=5)

                    df = get_stock_data(stock, num_of_years)
                    percent_change = rwb_strategy(df)

                    gains = sum(i for i in percent_change if i > 0)
                    losses = sum(i for i in percent_change if i < 0)
                    total_trades = len(percent_change)
                    total_return = round((np.prod([1 + i/100 for i in percent_change]) - 1) * 100, 2)

                    st.write(f"Results for {stock.upper()} going back to {num_of_years} years:")
                    st.write(f"Number of Trades: {total_trades}")
                    st.write(f"Total return: {total_return}%")

                    fig = go.Figure()
                    for ema in emas_used:
                        fig.add_trace(go.Scatter(x=df.index, y=df[f"Ema_{ema}"], mode='lines', name=f"Ema_{ema}"))
                    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], mode='lines', name="Adj Close", line=dict(color='green')))
                    fig.update_layout(title=f"RWB Strategy for {stock.upper()}", xaxis_title="Date", yaxis_title="Price", template='plotly_dark')
                    st.plotly_chart(fig)


            
            if pred_option_portfolio_strategies == "SMA Trading Strategy":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):
                    # Define the function to get historical data
                    def get_stock_data(stock, num_of_years):
                        start = dt.date.today() - dt.timedelta(days=365 * num_of_years)
                        end = dt.datetime.now()
                        return yf.download(stock, start, end, interval='1d')

                    # Define the function for SMA Trading Strategy
                    def sma_trading_strategy(df, short_sma, long_sma):
                        df[f"SMA_{short_sma}"] = df['Adj Close'].rolling(window=short_sma).mean()
                        df[f"SMA_{long_sma}"] = df['Adj Close'].rolling(window=long_sma).mean()

                        position = 0
                        percent_change = []
                        for i in df.index:
                            close = df['Adj Close'][i]
                            SMA_short = df[f"SMA_{short_sma}"][i]
                            SMA_long = df[f"SMA_{long_sma}"][i]

                            if SMA_short > SMA_long and position == 0:
                                buyP, position = close, 1
                                st.write("Buy at the price:", buyP)
                            elif SMA_short < SMA_long and position == 1:
                                sellP, position = close, 0
                                st.write("Sell at the price:", sellP)
                                percent_change.append((sellP / buyP - 1) * 100)

                        if position == 1:
                            position = 0
                            sellP = df['Adj Close'][-1]
                            st.write("Sell at the price:", sellP)
                            percent_change.append((sellP / buyP - 1) * 100)

                        return percent_change

                    # Main script
                    st.title("SMA Trading Strategy Visualization")

                    stock = st.text_input("Enter a ticker:", "NFLX")
                    num_of_years = st.number_input("Enter number of years:", min_value=1, max_value=10, step=1, value=5)
                    short_sma = st.number_input("Enter short SMA:", min_value=1, value=20)
                    long_sma = st.number_input("Enter long SMA:", min_value=1, value=50)

                    df = get_stock_data(stock, num_of_years)
                    percent_change = sma_trading_strategy(df, short_sma, long_sma)
                    current_price = round(df['Adj Close'][-1], 2)

                    # Calculate strategy statistics
                    gains = 0
                    numGains = 0
                    losses = 0
                    numLosses = 0
                    totReturn = 1
                    for i in percent_change:
                        if i > 0:
                            gains += i
                            numGains += 1
                        else:
                            losses += i
                            numLosses += 1
                        totReturn = totReturn * ((i / 100) + 1)
                    totReturn = round((totReturn - 1) * 100, 2)
                    # Plot SMA and Adj Close
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df.index, y=df[f"SMA_{short_sma}"], mode='lines', name=f"SMA_{short_sma}"))
                    fig.add_trace(go.Scatter(x=df.index, y=df[f"SMA_{long_sma}"], mode='lines', name=f"SMA_{long_sma}"))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'], mode='lines', name="Adj Close", line=dict(color='green')))
                    fig.update_layout(title=f"SMA Trading Strategy for {stock.upper()}", xaxis_title="Date", yaxis_title="Price", template='plotly_dark')
                    st.plotly_chart(fig)

                    # Display strategy statistics
                    st.write(f"Results for {stock.upper()} going back to {num_of_years} years:")
                    st.write(f"Number of Trades: {numGains + numLosses}")
                    st.write(f"Total return: {totReturn}%")


            
        
            if pred_option_portfolio_strategies == "Stock Spread Plotter":
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")

                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"Years captured: {years}")
                # Initialize the stocks list in session state if it doesn't exist
                if 'stocks' not in st.session_state:
                    st.session_state.stocks = []

                # Function to add stock
                def addStock():
                    tsk = st.text_input('Enter your tickers', key='ticker_input', placeholder='Enter a ticker')
                    if tsk:
                        st.session_state.stocks.append(tsk)
                        st.success(f"Ticker {tsk} added.")
                        st.experimental_rerun()  # Refresh the app to show the updated list

                # Display the add stock button and call the function if clicked
                if st.button('Add Ticker'):
                    addStock()

                # Display the list of stocks
                st.write("Current list of tickers:")
                st.write(st.session_state.stocks)
                threshold = st.slider("Threshold", min_value=0.1, max_value=5.0, value=0.5)
                stop_loss = st.slider("Stop Loss", min_value=0.1, max_value=5.0, value=1.0)
                if st.button("Check"):
                    # Function to fetch stock data
                    def fetch_stock_data(tickers, start_date, end_date):
                        data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
                        data.index = pd.to_datetime(data.index)
                        return data

                    def plot_stock_spread(df, ticker1, ticker2, threshold=0.5, stop_loss=1):
                        spread = df[ticker1] - df[ticker2]
                        mean_spread = spread.mean()
                        sell_threshold = mean_spread + threshold
                        buy_threshold = mean_spread - threshold
                        sell_stop = mean_spread + stop_loss
                        buy_stop = mean_spread - stop_loss

                        fig = go.Figure()

                        # Add the individual stock prices
                        fig.add_trace(go.Scatter(x=df.index, y=df[ticker1], mode='lines', name=ticker1))
                        fig.add_trace(go.Scatter(x=df.index, y=df[ticker2], mode='lines', name=ticker2))

                        # Add the spread
                        fig.add_trace(go.Scatter(x=df.index, y=spread, mode='lines', name='Spread', line=dict(color='#85929E')))

                        # Add threshold and stop lines
                        fig.add_hline(y=sell_threshold, line=dict(color='blue', dash='dash'), name='Sell Threshold')
                        fig.add_hline(y=buy_threshold, line=dict(color='red', dash='dash'), name='Buy Threshold')
                        fig.add_hline(y=sell_stop, line=dict(color='green', dash='dash'), name='Sell Stop')
                        fig.add_hline(y=buy_stop, line=dict(color='yellow', dash='dash'), name='Buy Stop')

                        # Update layout for better presentation
                        fig.update_layout(
                            title=f'Stock Spread between {ticker1} and {ticker2}',
                            xaxis_title='Date',
                            yaxis_title='Price',
                            legend_title='Legend',
                            template='plotly_white'
                        )

                        st.plotly_chart(fig)
                    # Main
                    if len(st.session_state.stocks) >= 2:
                        df = fetch_stock_data(st.session_state.stocks, start_date, end_date)
                        for i in range(len(st.session_state.stocks) - 1):
                            plot_stock_spread(df, st.session_state.stocks[i], st.session_state.stocks[i + 1], threshold, stop_loss)
                    else:
                        st.error("Please enter at least two tickers for the analysis.")

            if pred_option_portfolio_strategies == "Support Resistance Finder":
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Check"):

                    # Function to retrieve stock data
                    def fetch_stock_data(ticker, start_date, end_date):
                        df = yf.download(ticker, start=start_date, end=end_date)
                        df["Date"] = df.index
                        return df.reset_index(drop=True)

                    # Function to identify support and resistance levels
                    def identify_levels(df):
                        levels = []
                        for i in range(2, df.shape[0] - 2):
                            if is_support(df, i):
                                levels.append((i, df["Low"][i], "Support"))
                            elif is_resistance(df, i):
                                levels.append((i, df["High"][i], "Resistance"))
                        return levels

                    # Define support and resistance checks
                    def is_support(df, i):
                        return df["Low"][i] < min(df["Low"][i - 1], df["Low"][i + 1])

                    def is_resistance(df, i):
                        return df["High"][i] > max(df["High"][i - 1], df["High"][i + 1])

                    # Function to plot support and resistance levels
                    def plot_support_resistance(df, levels):
                        fig, ax = plt.subplots()
                        candlestick_ohlc(ax, zip(mpl_dates.date2num(df['Date']), df['Open'], df['High'], df['Low'], df['Close']), width=0.6, colorup='green', colordown='red', alpha=0.8)
                        ax.xaxis.set_major_formatter(mpl_dates.DateFormatter('%d-%m-%Y'))

                        for level in levels:
                            plt.hlines(level[1], xmin=df["Date"][level[0]], xmax=max(df["Date"]), colors="blue")
                        plt.title(f"Support and Resistance for {ticker.upper()}")
                        plt.xlabel("Date")
                        plt.ylabel("Price")
                        st.pyplot(fig)

                    # Main
                    st.title("Support and Resistance Levels Visualization")

                    ticker = st.text_input("Enter a ticker:")
                    num_of_years = st.slider("Number of years:", min_value=0.1, max_value=10.0, value=0.2, step=0.1)

                    start_date = pd.Timestamp.now() - pd.Timedelta(days=int(365.25 * num_of_years))
                    end_date = pd.Timestamp.now()

                    df = fetch_stock_data(ticker, start_date, end_date)
                    levels = identify_levels(df)
                    plot_support_resistance(df, levels)

        elif option == "Algorithmic Trading":
            AI_option_trading = st.selectbox('Make a choice', ["Lumibots : Diversified Leverage", "Lumibots : Stock Bracket Strategy","Lumibots : Hold to Expiry","Lumibots : Important functions (Crypto)", "Lumibots : Stock Limit & Trailing Stops","Lumibots : Momentum Strategy","Lumibots : Stock OCO Strategy","Lumibots : CCXT Backtesting Strategy","Lumibots : Buy & Hold Strategy", "Lumibots : GLD signal", "Lumibots : Trend Strategy", "Lumibots : Swing High Strategy"])
            if AI_option_trading == 'Lumibots : Buy & Hold Strategy':
                st.write("Lumibots buy hold strategy for Long term investors")
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                        
                    def initialize(self):
                        self.sleeptime = "1D"

                    def on_trading_iteration(self):
                        if self.first_iteration:
                            stocks_and_quantities = [
                                {"symbol": ticker_input, "quantity": quantities_input},
                            ]
                            for stock_info in stocks_and_quantities:
                                symbol = stock_info["symbol"]
                                quantity = stock_info["quantity"]
                                price = self.get_last_price(symbol)
                                cost = price * quantity
                                self.cash = portfolio_size
                                if self.cash >= cost:
                                    order = self.create_order(symbol, quantity, "buy")
                                    self.submit_order(order)
                
                    broker = Alpaca(ALPACA_CONFIG)
                    strategy = BuyHold(broker=broker)
                    trader = Trader()
                    trader.add_strategy(strategy)
                    trader.run_all()

            if AI_option_trading == 'Lumibots : GLD Signal Strategy':
                st.write("Lumibots buy hold strategy for Long term investors")
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    gld = pd.DataFrame(yf.download(ticker_input, start_date)['Close'])
                    gld['9-day'] = gld['Close'].rolling(9).mean()
                    gld['21-day'] = gld['Close'].rolling(21).mean()
                    gld['Signal'] = np.where(np.logical_and(gld['9-day'] > gld['21-day'],
                                            gld['9-day'].shift(1) < gld['21-day'].shift(1)),
                                            "BUY", None)
                    gld['Signal'] = np.where(np.logical_and(gld['9-day'] < gld['21-day'],
                                            gld['9-day'].shift(1) > gld['21-day'].shift(1)),
                                            "SELL", gld['Signal'])

                    def signal(df, start=start_date, end=end_date):
                        df = pd.DataFrame(yf.download(ticker_input, start, end)['Close'])
                        df['9-day'] = df['Close'].rolling(9).mean()
                        df['21-day'] = df['Close'].rolling(21).mean()
                        df['Signal'] = np.where(np.logical_and(df['9-day'] > df['21-day'],
                                                df['9-day'].shift(1) < df['21-day'].shift(1)),
                                                "BUY", None)
                        df['Signal'] = np.where(np.logical_and(df['9-day'] < df['21-day'],
                                                df['9-day'].shift(1) > df['21-day'].shift(1)),
                                                "SELL", df['Signal'])
                        return df, df.iloc[-1].Signal

                
            if AI_option_trading == 'Lumibots : Swing High Strategy':
                st.write("Lumibots buy hold strategy for Long term investors")
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    class SwingHigh(Strategy):
                        data = {}  # Dictionary to store last price data for each symbol
                        order_numbers = {}  # Dictionary to store order numbers for each symbol
                        shares_per_ticker = {}  # Dictionary to specify the number of shares per ticker

                        def initialize(self, ticker_input, quantities_input):
                            self.symbols = ticker_input# Add other symbols as needed
                            self.shares_per_ticker = {ticker_input: quantities_input}   # Specify the number of shares for each symbol
                            self.sleeptime = "10S"
                        
                        def on_trading_iteration(self):
                            for symbol in self.symbols:
                                if symbol not in self.data:
                                    self.data[symbol] = []

                                entry_price = self.get_last_price(symbol)
                                self.log_message(f"Position for {symbol}: {self.get_position(symbol)}")
                                self.data[symbol].append(entry_price)

                                if len(self.data[symbol]) > 3:
                                    temp = self.data[symbol][-3:]
                                    if temp[-1] > temp[1] > temp[0]:
                                        self.log_message(f"Last 3 prints for {symbol}: {temp}")
                                        order = self.create_order(symbol, quantity=self.shares_per_ticker[symbol], side="buy")
                                        self.submit_order(order)
                                        if symbol not in self.order_numbers:
                                            self.order_numbers[symbol] = 0
                                        self.order_numbers[symbol] += 1
                                        if self.order_numbers[symbol] == 1:
                                            self.log_message(f"Entry price for {symbol}: {temp[-1]}")
                                            entry_price = temp[-1]  # filled price
                                    if self.get_position(symbol) and self.data[symbol][-1] < entry_price * 0.995:
                                        self.sell_all(symbol)
                                        self.order_numbers[symbol] = 0
                                    elif self.get_position(symbol) and self.data[symbol][-1] >= entry_price * 1.015:
                                        self.sell_all(symbol)
                                        self.order_numbers[symbol] = 0

                        def before_market_closes(self):
                            for symbol in self.symbols:
                                self.sell_all(symbol)

            if AI_option_trading == 'Lumibots : Trend Strategy':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    class Trend(Strategy):

                        def initialize(self):
                            signal = None
                            start = start_date

                            self.signal = signal
                            self.start = start
                            self.sleeptime = "1D"
                        # minute bars, make functions    

                        def on_trading_iteration(self):
                            bars = self.get_historical_prices("GLD", 22, "day")
                            gld = bars.df
                            #gld = pd.DataFrame(yf.download("GLD", self.start)['Close'])
                            gld['9-day'] = gld['close'].rolling(9).mean()
                            gld['21-day'] = gld['close'].rolling(21).mean()
                            gld['Signal'] = np.where(np.logical_and(gld['9-day'] > gld['21-day'],
                                                                    gld['9-day'].shift(1) < gld['21-day'].shift(1)),
                                                    "BUY", None)
                            gld['Signal'] = np.where(np.logical_and(gld['9-day'] < gld['21-day'],
                                                                    gld['9-day'].shift(1) > gld['21-day'].shift(1)),
                                                    "SELL", gld['Signal'])
                            self.signal = gld.iloc[-1].Signal
                            
                            symbol = "GLD"
                            quantity = 200
                            if self.signal == 'BUY':
                                pos = self.get_position(symbol)
                                if pos is not None:
                                    self.sell_all()
                                    
                                order = self.create_order(symbol, quantity, "buy")
                                self.submit_order(order)

                            elif self.signal == 'SELL':
                                pos = self.get_position(symbol)
                                if pos is not None:
                                    self.sell_all()
                                    
                                order = self.create_order(symbol, quantity, "sell")
                                self.submit_order(order)

                        
                    if __name__ == "__main__":
                        trade = False
                        #Reactivate after code rebase
                        if trade:
                            broker = Alpaca(ALPACA_CONFIG)
                            strategy = Trend(broker=broker)
                            bot = Trader()
                            bot.add_strategy(strategy)
                            bot.run_all()
                        else:
                            start = start_date
                            end = end_date
                            Trend.backtest(
                                YahooDataBacktesting,
                                start,
                                end
                            )
            if AI_option_trading == 'Lumibots : CCXT Backtesting Strategy':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    class CcxtBacktestingExampleStrategy(Strategy):
                        def initialize(self, asset:tuple[Asset,Asset] = None,
                                    cash_at_risk:float=.25,window:int=21):
                            if asset is None:
                                raise ValueError("You must provide a valid asset pair")
                            # for crypto, market is 24/7
                            self.set_market("24/7")
                            self.sleeptime = "1D"
                            self.asset = asset
                            self.base, self.quote = asset
                            self.window = window
                            self.symbol = f"{self.base.symbol}/{self.quote.symbol}"
                            self.last_trade = None
                            self.order_quantity = 0.0
                            self.cash_at_risk = cash_at_risk

                        def _position_sizing(self):
                            cash = self.get_cash()
                            last_price = self.get_last_price(asset=self.asset,quote=self.quote)
                            quantity = round(cash * self.cash_at_risk / last_price,0)
                            return cash, last_price, quantity

                        def _get_historical_prices(self):
                            return self.get_historical_prices(asset=self.asset,length=None,
                                                        timestep="day",quote=self.quote).df

                        def _get_bbands(self,history_df:DataFrame):
                            # BBL (Lower Bollinger Band): Can act as a support level based on price volatility, and can indicate an 'oversold' condition if the price falls below this line.
                            # BBM (Breaking Bollinger Bands): This is essentially a moving average over a selected period of time, used as a reference point for price trends.
                            # BBU (Upper Bollinger Band): Can act as a resistance level based on price volatility, and can indicate an 'overbought' condition if the price moves above this line.
                            # BBB (Bollinger Band Width): Indicates the distance between the upper and lower bands, with a higher value indicating a more volatile market.
                            # BBP (Bollinger Band Percentage): This shows where the current price is located within the Bollinger Bands as a percentage, where a value close to 0 means that the price is close to the lower band, and a value close to 1 means that the price is close to the upper band.
                            # return bbands
                            num_std_dev = 2.0
                            close = 'close'

                            df = DataFrame(index=history_df.index)
                            df[close] = history_df[close]
                            df['bbm'] = df[close].rolling(window=self.window).mean()
                            df['bbu'] = df['bbm'] + df[close].rolling(window=self.window).std() * num_std_dev
                            df['bbl'] = df['bbm'] - df[close].rolling(window=self.window).std() * num_std_dev
                            df['bbb'] = (df['bbu'] - df['bbl']) / df['bbm']
                            df['bbp'] = (df[close] - df['bbl']) / (df['bbu'] - df['bbl'])
                            return df

                        def on_trading_iteration(self):
                            # During the backtest, we get the current time with self.get_datetime().
                            # The time interval is self.sleeptime.
                            current_dt = self.get_datetime()
                            cash, last_price, quantity = self._position_sizing()
                            history_df = self._get_historical_prices()
                            bbands = self._get_bbands(history_df)
                            prev_bbp = bbands[bbands.index < current_dt].tail(1).bbp.values[0]

                            if prev_bbp < -0.13 and cash > 0 and self.last_trade != Order.OrderSide.BUY and quantity > 0.0:
                                order = self.create_order(self.base,
                                                        quantity,
                                                        side = Order.OrderSide.BUY,
                                                        type = Order.OrderType.MARKET,
                                                        quote=self.quote)
                                self.submit_order(order)
                                self.last_trade = Order.OrderSide.BUY
                                self.order_quantity = quantity
                                self.log_message(f"Last buy trade was at {current_dt}")
                            elif prev_bbp > 1.2 and self.last_trade != Order.OrderSide.SELL and self.order_quantity > 0.0:
                                order = self.create_order(self.base,
                                                        self.order_quantity,
                                                        side = Order.OrderSide.SELL,
                                                        type = Order.OrderType.MARKET,
                                                        quote=self.quote)
                                self.submit_order(order)
                                self.last_trade = Order.OrderSide.SELL
                                self.order_quantity = 0.0
                                self.log_message(f"Last sell trade was at {current_dt}")

                        base_symbol = "ETH" # TODO-Adjust for either SPY/ETH for crypto
                        quote_symbol = ticker
                        start_date = datetime(2023,2,11)
                        end_date = datetime(2024,2,12)
                        asset = (Asset(symbol=base_symbol, asset_type="crypto"),
                                Asset(symbol=quote_symbol, asset_type="crypto"))

                        exchange_id = "kraken"  #"kucoin" #"bybit" #"okx" #"bitmex" # "binance"


                        # CcxtBacktesting default data download limit is 50,000
                        # If you want to change the maximum data download limit, you can do so by using 'max_data_download_limit'.
                        kwargs = {
                            # "max_data_download_limit":10000, # optional
                            "exchange_id":exchange_id,
                        }
                        CcxtBacktesting.MIN_TIMESTEP = "day"
                        results, strat_obj = CcxtBacktestingExampleStrategy.run_backtest(
                            CcxtBacktesting,
                            start_date,
                            end_date,
                            benchmark_asset=f"{base_symbol}/{quote_symbol}",
                            quote_asset=Asset(symbol=quote_symbol, asset_type="crypto"),
                            parameters={
                                    "asset":asset,
                                    "cash_at_risk":.25,
                                    "window":21,},
                            **kwargs,
                        )
            if AI_option_trading == 'Lumibots : Important functions (Crypto)':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    class ImportantFunctions(Strategy):
                        def initialize(self):
                            # Set the time between trading iterations
                            self.sleeptime = "30S"

                            # Set the market to 24/7 since those are the hours for the crypto market
                            self.set_market("24/7")

                        def on_trading_iteration(self):
                            ###########################
                            # Placing an Order
                            ###########################

                            # Define the base and quote assets for our transactions
                            base = Asset(symbol="BTC", asset_type="crypto")
                            quote = self.quote_asset

                            # Market Order for 0.1 BTC
                            mkt_order = self.create_order(base, 0.1, "buy", quote=quote)
                            self.submit_order(mkt_order)

                            # Limit Order for 0.1 BTC at a limit price of $10,000
                            lmt_order = self.create_order(base, 0.1, "buy", quote=quote, limit_price=10000)
                            self.submit_order(lmt_order)

                            ###########################
                            # Getting Historical Data
                            ###########################

                            # Get the historical prices for our base/quote pair for the last 100 minutes
                            bars = self.get_historical_prices(base, 100, "minute", quote=quote)
                            if bars is not None:
                                df = bars.df
                                max_price = df["close"].max()
                                self.log_message(f"Max price for {base} was {max_price}")

                                ############################
                                # TECHNICAL ANALYSIS
                                ############################

                                # Use pandas_ta to calculate the 20 period RSI
                                rsi = df.ta.rsi(length=20)
                                current_rsi = rsi.iloc[-1]
                                self.log_message(f"RSI for {base} was {current_rsi}")

                                # Use pandas_ta to calculate the MACD
                                macd = df.ta.macd()
                                current_macd = macd.iloc[-1]
                                self.log_message(f"MACD for {base} was {current_macd}")

                                # Use pandas_ta to calculate the 55 EMA
                                ema = df.ta.ema(length=55)
                                current_ema = ema.iloc[-1]
                                self.log_message(f"EMA for {base} was {current_ema}")

                            ###########################
                            # Positions and Orders
                            ###########################

                            # Get all the positions that we own, including cash
                            positions = self.get_positions()
                            for position in positions:
                                self.log_message(f"Position: {position}")

                                # Get the asset of the position
                                asset = position.asset

                                # Get the quantity of the position
                                quantity = position.quantity

                                # Get the symbol from the asset
                                symbol = asset.symbol

                                self.log_message(f"we own {quantity} shares of {symbol}")

                            # Get one specific position
                            asset_to_get = Asset(symbol="BTC", asset_type="crypto")
                            position = self.get_position(asset_to_get)

                            # Get all of the outstanding orders
                            orders = self.get_orders()
                            for order in orders:
                                self.log_message(f"Order: {order}")
                                # Do whatever you need to do with the order

                            # Get one specific order
                            order = self.get_order(mkt_order.identifier)

                            ###########################
                            # Other Useful Functions
                            ###########################

                            # Get the current (last) price for the base/quote pair
                            last_price = self.get_last_price(base, quote=quote)
                            self.log_message(
                                f"Last price for {base}/{quote} was {last_price}", color="green"
                            )

                            dt = self.get_datetime()
                            self.log_message(f"The current datetime is {dt}")
                            self.log_message(f"The current time is {dt.time()}")

                            # If you want to check if it's after a certain time, you can do this (eg. trading only after 9:30am)
                            if dt.time() > datetime.time(hour=9, minute=30):
                                self.log_message("It's after 9:30am")

                            # Get the value of the entire portfolio, including positions and cash
                            portfolio_value = self.portfolio_value
                            # Get the amount of cash in the account (the amount in the quote_asset)
                            cash = self.cash

                            self.log_message(f"The current value of your account is {portfolio_value}")
                            # Note: Cash is based on the quote asset
                            self.log_message(f"The current amount of cash in your account is {cash}")


                    if __name__ == "__main__":
                        trader = Trader()

                    
                        broker = Ccxt(KRAKEN_CONFIG)

                        strategy = ImportantFunctions(
                            broker=broker,
                        )

                        trader.add_strategy(strategy)
                        strategy_executors = trader.run_all()

            if AI_option_trading == 'Lumibots : Hold to Expiry':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    """
                    Strategy Description
                    An example strategy for buying an option and holding it to expiry.
                    """


                    class OptionsHoldToExpiry(Strategy):
                        parameters = {
                            "buy_symbol": "SPY",
                            "expiry": datetime(2023, 10, 20),
                        }

                        # =====Overloading lifecycle methods=============

                        def initialize(self):
                            # Set the initial variables or constants

                            # Built in Variables
                            self.sleeptime = "1D"

                        def on_trading_iteration(self):
                            """Buys the self.buy_symbol once, then never again"""

                            buy_symbol = self.parameters["buy_symbol"]
                            expiry = self.parameters["expiry"]

                            # What to do each iteration
                            underlying_price = self.get_last_price(buy_symbol)
                            self.log_message(f"The value of {buy_symbol} is {underlying_price}")

                            if self.first_iteration:
                                # Calculate the strike price (round to nearest 1)
                                strike = round(underlying_price)

                                # Create options asset
                                asset = Asset(
                                    symbol=buy_symbol,
                                    asset_type="option",
                                    expiration=expiry,
                                    strike=strike,
                                    right="call",
                                )

                                # Create order
                                order = self.create_order(
                                    asset,
                                    10,
                                    "buy_to_open",
                                )
                                
                                # Submit order
                                self.submit_order(order)

                                # Log a message
                                self.log_message(f"Bought {order.quantity} of {asset}")


                    if __name__ == "__main__":
                        is_live = False

                        if is_live:

                            from lumibot.brokers import InteractiveBrokers
                            from lumibot.traders import Trader

                            trader = Trader()

                            broker = InteractiveBrokers(INTERACTIVE_BROKERS_CONFIG)
                            strategy = OptionsHoldToExpiry(broker=broker)

                            trader.add_strategy(strategy)
                            strategy_executors = trader.run_all()

                        else:
                            from lumibot.backtesting import PolygonDataBacktesting

                            # Backtest this strategy
                            backtesting_start = datetime(2023, 10, 19)
                            backtesting_end = datetime(2023, 10, 24)

                            results = OptionsHoldToExpiry.backtest(
                                PolygonDataBacktesting,
                                backtesting_start,
                                backtesting_end,
                                benchmark_asset="SPY",
                                polygon_api_key="YOUR_POLYGON_API_KEY_HERE",  # Add your polygon API key here
                                polygon_has_paid_subscription=False,
                            )




            if AI_option_trading == 'Lumibots : Stock Bracket Strategy':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    """
                    Strategy Description

                    An example strategy for how to use bracket orders.
                    """
                    class StockBracket(Strategy):
                        parameters = {
                            "buy_symbol": "SPY",
                            "take_profit_price": 405,
                            "stop_loss_price": 395,
                            "quantity": 10,
                        }

                        # =====Overloading lifecycle methods=============

                        def initialize(self):
                            # Set the initial variables or constants

                            # Built in Variables
                            self.sleeptime = "1D"

                            # Our Own Variables
                            self.counter = 0

                        def on_trading_iteration(self):
                            """Buys the self.buy_symbol once, then never again"""

                            buy_symbol = self.parameters["buy_symbol"]
                            take_profit_price = self.parameters["take_profit_price"]
                            stop_loss_price = self.parameters["stop_loss_price"]
                            quantity = self.parameters["quantity"]

                            # What to do each iteration
                            current_value = self.get_last_price(buy_symbol)
                            self.log_message(f"The value of {buy_symbol} is {current_value}")

                            if self.first_iteration:
                                # Bracket order
                                order = self.create_order(
                                    buy_symbol,
                                    quantity,
                                    "buy",
                                    take_profit_price=take_profit_price,
                                    stop_loss_price=stop_loss_price,
                                    type="bracket",
                                )
                                self.submit_order(order)


                    if __name__ == "__main__":
                        is_live = False

                        if is_live:

                            from lumibot.brokers import Alpaca
                            from lumibot.traders import Trader

                            trader = Trader()

                            broker = Alpaca(ALPACA_CONFIG)

                            strategy = StockBracket(broker=broker)

                            trader.add_strategy(strategy)
                            strategy_executors = trader.run_all()

                        else:
                            from lumibot.backtesting import YahooDataBacktesting

                            # Backtest this strategy
                            backtesting_start = datetime(2023, 3, 3)
                            backtesting_end = datetime(2023, 3, 10)

                            results = StockBracket.backtest(
                                YahooDataBacktesting,
                                backtesting_start,
                                backtesting_end,
                                benchmark_asset="SPY",
                            )




            if AI_option_trading == 'Lumibots : Diversified Leverage':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):
                    """
                    Strategy Description

                    This strategy will buy a few symbols that have 2x or 3x returns (have leverage), but will 
                    also diversify and rebalance the portfolio often.
                    """


                    class DiversifiedLeverage(Strategy):
                        # =====Overloading lifecycle methods=============

                        parameters = {
                            "portfolio": [
                                {
                                    "symbol": "TQQQ",  # 3x Leveraged Nasdaq
                                    "weight": 0.20,
                                },
                                {
                                    "symbol": "UPRO",  # 3x Leveraged S&P 500
                                    "weight": 0.20,
                                },
                                {
                                    "symbol": "UDOW",  # 3x Leveraged Dow Jones
                                    "weight": 0.10,
                                },
                                {
                                    "symbol": "TMF",  # 3x Leveraged Treasury Bonds
                                    "weight": 0.25,
                                },
                                {
                                    "symbol": "UGL",  # 3x Leveraged Gold
                                    "weight": 0.10,
                                },
                                {
                                    "symbol": "DIG",  # 2x Leveraged Oil and Gas Companies (Commodities)
                                    "weight": 0.15,
                                },
                            ],
                            "rebalance_period": 4,
                        }

                        def initialize(self):
                            # Setting the waiting period (in days) and the counter
                            self.counter = None

                            # There is only one trading operation per day
                            # no need to sleep between iterations
                            self.sleeptime = "1D"

                            # Initializing the portfolio variable with the assets and proportions we want to own
                            self.initialized = False

                            self.minutes_before_closing = 1

                        def on_trading_iteration(self):
                            rebalance_period = self.parameters["rebalance_period"]
                            # If the target number of days (period) has passed, rebalance the portfolio
                            if self.counter == rebalance_period or self.counter == None:
                                self.counter = 0
                                self.rebalance_portfolio()
                                self.log_message(
                                    f"Next portfolio rebalancing will be in {rebalance_period} day(s)"
                                )

                            self.log_message("Sleeping until next trading day")
                            self.counter += 1

                        # =============Helper methods====================

                        def rebalance_portfolio(self):
                            """Rebalance the portfolio and create orders"""

                            orders = []
                            for asset in self.parameters["portfolio"]:
                                # Get all of our variables from portfolio
                                symbol = asset.get("symbol")
                                weight = asset.get("weight")
                                last_price = self.get_last_price(symbol)

                                # Get how many shares we already own
                                # (including orders that haven't been executed yet)
                                position = self.get_position(symbol)
                                quantity = 0
                                if position is not None:
                                    quantity = float(position.quantity)

                                # Calculate how many shares we need to buy or sell
                                shares_value = self.portfolio_value * weight
                                self.log_message(
                                    f"The current portfolio value is {self.portfolio_value} and the weight needed is {weight}, so we should buy {shares_value}"
                                )
                                new_quantity = shares_value // last_price
                                quantity_difference = new_quantity - quantity
                                self.log_message(
                                    f"Currently own {quantity} shares of {symbol} but need {new_quantity}, so the difference is {quantity_difference}"
                                )

                                # If quantity is positive then buy, if it's negative then sell
                                side = ""
                                if quantity_difference > 0:
                                    side = "buy"
                                elif quantity_difference < 0:
                                    side = "sell"

                                # Execute the order if necessary
                                if side:
                                    order = self.create_order(symbol, abs(quantity_difference), side)
                                    orders.append(order)

                            self.submit_orders(orders)


                        if __name__ == "__main__":
                            is_live = False

                            if is_live:
                                ####
                                # Run the strategy live
                                ####

                                trader = Trader()
                                broker = Alpaca(ALPACA_CONFIG)
                                strategy = DiversifiedLeverage(broker=broker)
                                trader.add_strategy(strategy)
                                trader.run_all()

                            else:
                                ####
                                # Backtest the strategy
                                ####

                                # Choose the time from and to which you want to backtest
                                backtesting_start = datetime(2010, 6, 1)
                                backtesting_end = datetime(2023, 7, 31)

                                # 0.01% trading/slippage fee
                                trading_fee = TradingFee(percent_fee=0.005)

                                # Initialize the backtesting object
                                print("Starting Backtest...")
                                result = DiversifiedLeverage.backtest(
                                    YahooDataBacktesting,
                                    backtesting_start,
                                    backtesting_end,
                                    benchmark_asset="SPY",
                                    parameters={},
                                    buy_trading_fees=[trading_fee],
                                    sell_trading_fees=[trading_fee],
                                )

                                print("Backtest result: ", result)



            if AI_option_trading == 'Lumibots : Stock Limit & Trailing Stops':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):

                    """
                    Strategy Description

                    An example of how to use limit orders and trailing stops to buy a stock and then sell it when it drops by a certain
                    percentage. This is a very simple strategy that is meant to demonstrate how to use limit orders and trailing stops.
                    """


                    class LimitAndTrailingStop(Strategy):
                        parameters = {
                            "buy_symbol": "SPY",
                            "limit_buy_price": 403,
                            "limit_sell_price": 407,
                            "trail_percent": 0.02,
                            "trail_price": 7,
                        }

                        # =====Overloading lifecycle methods=============

                        def initialize(self):
                            # Set the initial variables or constants

                            # Built in Variables
                            self.sleeptime = "1D"

                            # Our Own Variables
                            self.counter = 0

                        def on_trading_iteration(self):
                            """Buys the self.buy_symbol once, then never again"""

                            buy_symbol = self.parameters["buy_symbol"]
                            limit_buy_price = self.parameters["limit_buy_price"]
                            limit_sell_price = self.parameters["limit_sell_price"]
                            trail_percent = self.parameters["trail_percent"]
                            trail_price = self.parameters["trail_price"]

                            # What to do each iteration
                            current_value = self.get_last_price(buy_symbol)
                            self.log_message(f"The value of {buy_symbol} is {current_value}")

                            if self.first_iteration:
                                # Create the limit buy order
                                purchase_order = self.create_order(buy_symbol, 100, "buy", limit_price=limit_buy_price)
                                self.submit_order(purchase_order)

                                # Create the limit sell order
                                sell_order = self.create_order(buy_symbol, 100, "sell", limit_price=limit_sell_price)
                                self.submit_order(sell_order)

                                # Place the trailing percent stop
                                trailing_pct_stop_order = self.create_order(buy_symbol, 100, "sell", trail_percent=trail_percent)
                                self.submit_order(trailing_pct_stop_order)

                                # Place the trailing price stop
                                trailing_price_stop_order = self.create_order(buy_symbol, 50, "sell", trail_price=trail_price)
                                self.submit_order(trailing_price_stop_order)


                    if __name__ == "__main__":
                        is_live = False

                        if is_live:

                            from lumibot.brokers import Alpaca
                            from lumibot.traders import Trader

                            trader = Trader()

                            broker = Alpaca(ALPACA_CONFIG)

                            strategy = LimitAndTrailingStop(broker=broker)

                            trader.add_strategy(strategy)
                            strategy_executors = trader.run_all()

                        else:
                            from lumibot.backtesting import YahooDataBacktesting

                            # Backtest this strategy
                            backtesting_start = datetime(2023, 3, 3)
                            backtesting_end = datetime(2023, 3, 10)

                            results = LimitAndTrailingStop.backtest(
                                YahooDataBacktesting,
                                backtesting_start,
                                backtesting_end,
                                benchmark_asset="SPY",
                            )
                    

            if AI_option_trading == 'Lumibots : Momentum Strategy':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):

                    """
                    Strategy Description

                    Buys the best performing asset from self.symbols over self.period number of days.
                    For example, if SPY increased 2% yesterday, but VEU and AGG only increased 1% yesterday,
                    then we will buy SPY.
                    """


                    class Momentum(Strategy):
                        # =====Overloading lifecycle methods=============

                        def initialize(self, symbols=None):
                            # Setting the waiting period (in days)
                            self.period = 2

                            # The counter for the number of days we have been holding the current asset
                            self.counter = 0

                            # There is only one trading operation per day
                            # No need to sleep between iterations
                            self.sleeptime = 0

                            # Set the symbols that we will be monitoring for momentum
                            if symbols:
                                self.symbols = symbols
                            else:
                                self.symbols = ["SPY", "VEU", "AGG"]

                            # The asset that we want to buy/currently own, and the quantity
                            self.asset = ""
                            self.quantity = 0

                        def on_trading_iteration(self):
                            # When the counter reaches the desired holding period,
                            # re-evaluate which asset we should be holding
                            momentums = []
                            if self.counter == self.period or self.counter == 0:
                                self.counter = 0
                                momentums = self.get_assets_momentums()

                                # Get the asset with the highest return in our period
                                # (aka the highest momentum)
                                momentums.sort(key=lambda x: x.get("return"))
                                best_asset_data = momentums[-1]
                                best_asset = best_asset_data["symbol"]
                                best_asset_return = best_asset_data["return"]

                                # Get the data for the currently held asset
                                if self.asset:
                                    current_asset_data = [
                                        m for m in momentums if m["symbol"] == self.asset
                                    ][0]
                                    current_asset_return = current_asset_data["return"]

                                    # If the returns are equals, keep the current asset
                                    if current_asset_return >= best_asset_return:
                                        best_asset = self.asset
                                        best_asset_data = current_asset_data

                                self.log_message("%s best symbol." % best_asset)

                                # If the asset with the highest momentum has changed, buy the new asset
                                if best_asset != self.asset:
                                    # Sell the current asset that we own
                                    if self.asset:
                                        self.log_message("Swapping %s for %s." % (self.asset, best_asset))
                                        order = self.create_order(self.asset, self.quantity, "sell")
                                        self.submit_order(order)

                                    # Calculate the quantity and send the buy order for the new asset
                                    self.asset = best_asset
                                    best_asset_price = best_asset_data["price"]
                                    self.quantity = int(self.portfolio_value // best_asset_price)
                                    order = self.create_order(self.asset, self.quantity, "buy")
                                    self.submit_order(order)
                                else:
                                    self.log_message("Keeping %d shares of %s" % (self.quantity, self.asset))

                            self.counter += 1

                            # Stop for the day, since we are looking at daily momentums
                            self.await_market_to_close()

                        def on_abrupt_closing(self):
                            # Sell all positions
                            self.sell_all()

                        def trace_stats(self, context, snapshot_before):
                            """
                            Add additional stats to the CSV logfile
                            """
                            # Get the values of all our variables from the last iteration
                            row = {
                                "old_best_asset": snapshot_before.get("asset"),
                                "old_asset_quantity": snapshot_before.get("quantity"),
                                "old_cash": snapshot_before.get("cash"),
                                "new_best_asset": self.asset,
                                "new_asset_quantity": self.quantity,
                            }

                            # Get the momentums of all the assets from the context of on_trading_iteration
                            # (notice that on_trading_iteration has a variable called momentums, this is what
                            # we are reading here)
                            momentums = context.get("momentums")
                            if len(momentums) != 0:
                                for item in momentums:
                                    symbol = item.get("symbol")
                                    for key in item:
                                        if key != "symbol":
                                            row[f"{symbol}_{key}"] = item[key]

                            # Add all of our values to the row in the CSV file. These automatically get
                            # added to portfolio_value, cash and return
                            return row

                        # =============Helper methods====================

                        def get_assets_momentums(self):
                            """
                            Gets the momentums (the percentage return) for all the assets we are tracking,
                            over the time period set in self.period
                            """

                            momentums = []
                            start_date = self.get_round_day(timeshift=self.period + 1)
                            end_date = self.get_round_day(timeshift=1)
                            data = self.get_bars(self.symbols, self.period + 2, timestep="day")
                            for asset, bars_set in data.items():
                                # Get the return for symbol over self.period days
                                # (from start_date to end_date)
                                symbol = asset.symbol
                                symbol_momentum = bars_set.get_momentum(start=start_date, end=end_date)
                                self.log_message(
                                    "%s has a return value of %.2f%% over the last %d day(s)."
                                    % (symbol, 100 * symbol_momentum, self.period)
                                )

                                momentums.append(
                                    {
                                        "symbol": symbol,
                                        "price": bars_set.get_last_price(),
                                        "return": symbol_momentum,
                                    }
                                )

                            return momentums


                    if __name__ == "__main__":
                        is_live = False

                        if is_live:

                            from lumibot.brokers import Alpaca
                            from lumibot.traders import Trader

                            trader = Trader()

                            broker = Alpaca(ALPACA_CONFIG)

                            strategy = Momentum(broker=broker)

                            trader.add_strategy(strategy)
                            strategy_executors = trader.run_all()

                        else:
                            from lumibot.backtesting import YahooDataBacktesting

                            # Backtest this strategy
                            backtesting_start = datetime(2023, 1, 1)
                            backtesting_end = datetime(2023, 8, 1)

                            results = Momentum.backtest(
                                YahooDataBacktesting,
                                backtesting_start,
                                backtesting_end,
                                benchmark_asset="SPY",
                            )

            if AI_option_trading == 'Lumibots : Stock OCO Strategy':
                ticker = st.text_input("Please enter the ticker needed for investigation")
                if ticker:
                    message = (f"Ticker captured : {ticker}")
                    st.success(message)
                portfolio = st.number_input("Enter the portfolio size in USD")
                if portfolio:
                    st.write(f"The portfolio size in USD Captured is : {portfolio}")
                min_date = datetime(1980, 1, 1)
                # Date input widget with custom minimum date
                col1, col2 = st.columns([2, 2])
                with col1:
                    start_date = st.date_input("Start date:", min_value=min_date)
                with col2:
                    end_date = st.date_input("End Date:")
                years = end_date.year - start_date.year
                st.success(f"years captured : {years}")
                if st.button("Trade"):

                    """
                    Strategy Description

                    An example strategy for how to use OCO orders.
                    """


                    class StockOco(Strategy):
                        parameters = {
                            "buy_symbol": "SPY",
                            "take_profit_price": 405,
                            "stop_loss_price": 395,
                            "quantity": 10,
                        }

                        # =====Overloading lifecycle methods=============

                        def initialize(self):
                            # Set the initial variables or constants

                            # Built in Variables
                            self.sleeptime = "1D"

                            # Our Own Variables
                            self.counter = 0

                        def on_trading_iteration(self):
                            """Buys the self.buy_symbol once, then never again"""

                            buy_symbol = self.parameters["buy_symbol"]
                            take_profit_price = self.parameters["take_profit_price"]
                            stop_loss_price = self.parameters["stop_loss_price"]
                            quantity = self.parameters["quantity"]

                            # What to do each iteration
                            current_value = self.get_last_price(buy_symbol)
                            self.log_message(f"The value of {buy_symbol} is {current_value}")

                            if self.first_iteration:
                                # Market order
                                    main_order = self.create_order(
                                        buy_symbol, quantity, "buy",
                                    )
                                    self.submit_order(main_order)

                                    # OCO order
                                    order = self.create_order(
                                        buy_symbol,
                                        quantity,
                                        "sell",
                                        take_profit_price=take_profit_price,
                                        stop_loss_price=stop_loss_price,
                                        type="oco",
                                    )
                                    self.submit_order(order)


                    if __name__ == "__main__":
                        is_live = False

                        if is_live:

                            trader = Trader()

                            broker = Alpaca(ALPACA_CONFIG)

                            strategy = StockOco(broker=broker)

                            trader.add_strategy(strategy)
                            strategy_executors = trader.run_all()

                        else:
                            from lumibot.backtesting import YahooDataBacktesting

                            # Backtest this strategy
                            backtesting_start = datetime(2023, 3, 3)
                            backtesting_end = datetime(2023, 3, 10)

                            results = StockOco.backtest(
                                YahooDataBacktesting,
                                backtesting_start,
                                backtesting_end,
                                benchmark_asset="SPY",
                            )
                # Right column setup
                # Initialize session state for conversation history

        with right_column:
            # Now you can use the key in your code
            prompt = hub.pull("hwchase17/openai-tools-agent")
            llm = ChatOpenAI(model="gpt-3.5-turbo-0125", openai_api_key=os.environ.get("OPEN_AI_API"))
            agent = create_tool_calling_agent(llm, tools, prompt)
            agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

            st.markdown("### Frankline & Co. LP Bot 🤖")
            st.markdown("<hr style='border:1px solid gray'>", unsafe_allow_html=True)

            # Create a text input box for the user to ask a question
            user_query = st.text_input('Ask me to run any any finance tool..like `run idb irs rating from august 1 to sep 1`')

            # Check if user submitted input
            if st.button('Submit'):
                if user_query.strip() == '':
                    st.error("Please enter a query or function to run")
                else:
                    try:
                        st.success("Query running...wait for output")
                        # Use the agent_executor to handle the user query
                        result = agent_executor.invoke({"input": user_query})
                        if result:
                            st.success("Result returned")
                            # Update the conversation history
                            st.session_state.conversation += f"User: {user_query}\nBot: {result}\n"
                            # Display the updated conversation history
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()