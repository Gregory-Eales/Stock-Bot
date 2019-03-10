from alpha_vantage_api import AlphaVantageAPI
import pandas as pd

my_api_key = "1HWD90PW0GC2JH38"

fetcher = AlphaVantageAPI(api_key=my_api_key)


df = fetcher.fetch_example()

print(df.head(1))