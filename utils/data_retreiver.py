import numpy as np
import torch
import finnhub
import pandas as pd


class DataRetreiver(object):

    def __init__(self):
        
        self.client = finnhub.Client(api_key="YOUR API KEY")

    def read_api_key(self):
    	pass

    def check_connection(self):
        pass

    def get_sentiment(self, ticker):
        pass
