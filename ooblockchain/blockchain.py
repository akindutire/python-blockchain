from block import Block
from transactions import Transaction

class Blockchains:

    __chain = []

    def __init__(self):
        b1 = Block(0, '', [], 0)
        genesis_block = b1.get_transactions()
        self.__chain.append(genesis_block)

    @classmethod
    def get_last_block_of_chain(cls):
        return cls.__chain[-1]

    def get_blockchain(self):
        return self.__chain