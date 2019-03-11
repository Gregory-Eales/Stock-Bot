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
        self._link_output = "&outputsize="

    def fetch_intraday_example(self):
        df = pd.read_csv(self._example_link)
        return df

    def _create_intraday_link(self, func, ticker, interval, output_size="compact", dtype="csv"):
        self._check_interval(interval)
        link = self._link_main + func + self._link_symbol + ticker + self._link_interval + interval + \
               self._link_output + output_size + self._link_key + self._api_key + self._link_dtype + dtype
        return link

    def _create_daily_link(self, ticker, output_size="compact", dtype="csv"):
        func = "TIME_SERIES_DAILY"
        link = self._link_main + func + self._link_symbol + ticker + self._link_output +\
               output_size + self._link_key + self._api_key + self._link_dtype + dtype
        return link

    def _create_weekly_link(self, ticker, dtype="csv"):
        func = "TIME_SERIES_WEEKLY"
        link = self._link_main + func + self._link_symbol + ticker + \
               self._link_key + self._api_key + self._link_dtype + dtype
        return link

    def _create_monthly_link(self, ticker, dtype="csv"):
        func = "TIME_SERIES_MONTHLY"
        link = self._link_main + func + self._link_symbol + ticker + \
               self._link_key + self._api_key + self._link_dtype + dtype
        return link

    def _create_endpoint_link(self, ticker, dtype="csv"):
        func = "GLOBAL_QUOTE"
        link = self._link_main + func + self._link_symbol + ticker + \
               self._link_key + self._api_key + self._link_dtype + dtype
        return link


    @staticmethod
    def _check_interval(interval):
        intervals = ["1min", "5min", "15min", "30min", "60min"]
        if interval not in intervals:
            raise Exception("Error: the interval entered is not valid")

    def fetch_intraday(self, ticker, interval, output_size="compact", dtype="csv"):
        func = "TIME_SERIES_INTRADAY"
        self._check_interval(interval)
        link = self._create_intraday_link(func, ticker, interval, output_size, dtype)
        df = pd.read_csv(link)
        return df

    def fetch_daily(self, ticker, output_size="compact", dtype="csv"):
        func = "TIME_SERIES_DAILY"
        link = self._create_daily_link(ticker, output_size, dtype)
        df = pd.read_csv(link)
        return df

    def fetch_weekly(self, ticker, dtype="csv"):
        link = self._create_weekly_link(ticker, dtype)
        df = pd.read_csv(link)
        return df

    def fetch_monthly(self, ticker, dtype="csv"):
        link = self._create_monthly_link(ticker, dtype)
        df = pd.read_csv(link)
        return df

    def fetch_quote_endpoint(self, ticker, dtype="csv"):
        link = self._create_endpoint_link(ticker, dtype)
        df = pd.read_csv(link)
        return df
