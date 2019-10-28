import torch
import numpy as np
import pyetrade
from pyetrade import ETradeAccessManager, ETradeAccounts, ETradeMarket
from pyetrade import ETradeOAuth, ETradeOrder

from value_network import ValueNetwork

class StockBot(object):

    def __init__(self, credential_path):

        ck, cs, rok, ros = self.get_credentials(filename=credential_path)

        self.client_key = ck
        self.client_secret = cs
        self.resource_owner_key = rok
        self.resource_owner_secret = ros

        self.access_manager = ETradeAccessManager(client_key=ck,
         client_secret=cs, resource_owner_key=rok, resource_owner_secret=ros)

        self.acounts = ETradeAccounts(client_key=ck,
         client_secret=cs, resource_owner_key=rok, resource_owner_secret=ros)

        self.market = ETradeMarket(client_key=ck, client_secret=cs,
         resource_owner_key=rok, resource_owner_secret=ros)

        self.oauth = ETradeOAuth(consumer_key=ck,
         consumer_secret=cs, callback_url='oob

        self.value_network = ValueNetwork()

    def get_credentials(self, filename):
        pass

    def login(self):
        pass

    def buy(self, ticker, amount):
        pass

    def sell(self, ticker, amount):
        pass

    def get_quote(self, ticker):
        return self.market.get_quote(ticker)
