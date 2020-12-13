



class Etrader(object):

    def __init__(self, credential_path):

        ck, cs, rok, ros = self.get_credentials(filename=credential_path)

        self.client_key = ck
        self.client_secret = cs
        self.value_network = ValueNetwork()

    def get_credentials(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        key = lines[0]
        secret = lines[1]
        key = key.split(":")[1]
        secret = secret.split(":")[1]
