from alpha_vantage_api import AlphaVantageAPI
import pandas as pd

my_api_key = "1HWD90PW0GC2JH38"

fetcher = AlphaVantageAPI(api_key=my_api_key)


#df = fetcher.fetch_intraday("MSFT", "1min")
#df = fetcher.fetch_daily("MSFT")
#df = fetcher.fetch_weekly("MSFT")
#df = fetcher.fetch_monthly("MSFT")
df = fetcher.fetch_quote_endpoint("AQB")

print(df.keys())