import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


class Bot(object):


	def __init__(self, path="credentials.txt"):

		self.load_credentials(path=path)

		self.api = tradeapi.REST(
			self.id,
			self.key,
			base_url='https://paper-api.alpaca.markets'
		)

		self.account = self.api.get_account()

	def update_account(self):
		self.account = self.api.get_account()

	def get_overview(self):

		self.update_account()

		data = []
		data.append(self.account)

		return data
		
	def load_credentials(self, path):

		with open(path, "r") as file:

			line = file.readlines()

			self.id = line[0].split(":")[1].strip()
			self.key = line[1].split(":")[1].strip()


	def get_quote(self, ticker):
		return self.api.get_last_quote(ticker)


	def get_positions(self):
		return self.api.list_positions()


	def get_barset(self, ticker):
		NY = 'America/New_York'
		start=pd.Timestamp('2020-08-28 9:30', tz=NY).isoformat()
		end=pd.Timestamp('2020-08-28 16:00', tz=NY).isoformat()
		return self.api.get_barset(ticker, 'minute', start=start, end=end).df