import pandas as pd

class AlphaVantageAPI(object):

    def __init__(self, api_key="demo"):

        if api_key == "demo":
            print("Warning: the demo api key is being used")

        self._api_key = api_key
        self._example_link = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo&datatype=csv"
        self._link_start = "https://www.alphavantage.co/query?function="
        self._link_symbol = "&symbol"


    def fetch_example(self):
         df = pd.read_csv(self._example_link)
         return df

    def fetch_intraday(self, ticker="MSFT"):
        return 1
