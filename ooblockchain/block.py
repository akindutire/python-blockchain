import hashlib
from time import time
from collections import OrderedDict

class Block:

    def __init__(self, index, previous_hash, transaction, nonce, time = time()):
        self.__previous_hash = previous_hash
        self.__hash = hashlib.sha256(str(self.__dict__).encode())
        self.__index = index
        self.__nonce = nonce
        self.__transactions = transaction
        self.__timestamp = time

    def get_transactions(self):
        return self.__transactions

    def get_nonce(self):
        return self.__nonce 

    def get_index(self):
        return self.__index

    def get_previous_hash(self):
        return self.__previous_hash

    def get_hash(self):
        return self.__hash

    def get_block(self):
        return OrderedDict([
            
            ('previous_hash', self.get_previous_hash()),
            ('hash', self.get_hash()),
            ('index', self.get_index()),
            ('transactions', self.get_transactions()),
            ('nonce', self.get_nonce())

        ])