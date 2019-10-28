import torch
import pyetrade
from pyetrade import ETradeAccessManager, ETradeAccounts, ETradeMarket
from pyetrade import ETradeOAuth, ETradeOrder
from pyetrade import

class StockBot(object):

    def __init__(self):

        self.client_key = None
        self.client_secret = None
        self.resource_owner_key = None
        self.resource_owner_secret = None

        self.access_manager = ETradeAccessManager(client_key=,
         client_secret=, resource_owner_key=, resource_owner_secret=)

        self.acounts = ETradeAccounts(client_key=,
         client_secret=, resource_owner_key=, resource_owner_secret=)

        self.market = ETradeMarket(client_key=, client_secret=,
         resource_owner_key=, resource_owner_secret=)

        self.oauth = ETradeOAuth(consumer_key=,
         consumer_secret=, callback_url='oob')

    def get_credentials(self, filename):
        pass

    def login(self):
        pass

    def buy(self, ticker, amount):
        pass

    def sell(self, ticker, amount):
        pass

    def get_data(self, ticker, amount):
        pass

    def trade(self):
        pass
