import pandas as pd


class AlphaVantageAPI(object):
    def __init__(self, api_key="demo"):

        if api_key == "demo":
            print("Warning: the demo api key is being used")

        self._api_key = api_key
        self._example_link = "https://www.alphavantage.co/query?function=" \
                             "TIME_SERIES_INTRADAY&symbol=MSFT&interval=5" \
                             "min&apikey=demo&datatype=csv"

        self._link_main = "https://www.alphavantage.co/query?function="
        self._link_symbol = "&symbol="
        self._link_interval = "&interval="
        self._link_key = "&apikey="
        self._link_dtype = "&datatype="

    def fetch_intraday_example(self):
        df = pd.read_csv(self._example_link)
        return df

    def _create_link(self, func, ticker, interval, dtype):
        self._check_func(func)
        self._check_interval(interval)
        link = self._link_main + func + self._link_symbol + ticker + self._link_interval + \
               interval + self._link_key + self._api_key + self._link_dtype + dtype
        return link

    @staticmethod
    def _check_interval(interval):
        intervals = ["1min", "5min", "15min", "30min", "60min"]
        if interval not in intervals:
            raise Exception("Error: the interval entered is not valid")

    @staticmethod
    def _check_func(self, func):
        pass

    def fetch_intraday(self):
        pass

    def fetch_daily(self):
        pass

    def fetch_weekly(self):
        pass

    def fetch_monthly(self):
        pass

    def fetch_quote_endpoint(self):
        pass
