from time import time
from collections import OrderedDict
class Transaction:

    Transaction_pool = []

    def __init__(self, sender, recipient, amount):
        self.__sender = sender
        self.__recipient = recipient
        self.__amount = amount
        self.__timestamp = time()

        self.Transaction_pool.append(self.get_transaction())

    def get_transaction(self):

        return OrderedDict([
            ('sender', self.__sender),
            ('recipient', self.__recipient),
            ('amount', self.__amount),
            ('timestamp', self.__timestamp)
        ])


"""

    @staticmethod
    def ma():
        pass

    @classmethod
    def po():
        pass

    def __init__(self):
        self.chain

    @chain.setter
    def chain(self, val):
        self.__chain = val

    @property
    def chain(self):
        return self.__chain[:]

"""