import torch
import numpy as np

from etrade_api import Etrader
from value_network import ValueNetwork
from evaluation_network import EvaluationNetwork
from policy_network import PolicyNetwork

class StockBot(object):

    def __init__(self, credential_path):

        # define api handler
        self.etrader = Etrader(credential_path=credential_path)

        # define networks
        self.eval_net = PolicyNetwork()
        self.value_net = EvaluationNetwork()
        self.policy_net = PolicyNetwork()

    def buy(self, ticker, amount):
        pass

    def sell(self, ticker, amount):
        pass

    def get_quote(self, ticker):
        return self.market.get_quote(ticker)
