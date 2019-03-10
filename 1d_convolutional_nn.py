import torch


class StockConvNet(object):
    def __init__(self):
        # initiate weights
        self.conv_w = {}
        self.dense_w = {}

        # initiate z's
        self.conv_z = {}
        self.dense_z = {}

        # initiate activations
        self.conv_a = {}
        self.dense_a = {}

    def single_conv(self):
        pass

    def convolutional_forward(self):
        pass

