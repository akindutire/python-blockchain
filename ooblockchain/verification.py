import hashlib
from transactions import Transaction
from blockchain import Blockchains
import json

class Verification:
    
    __proof_of_work_requirement = '00'

    def __init__(self):
        pass

    def generate_proof_of_work(self):
        #Proof of work takes the transactions, previoushash, and a number(nonce) such that when combined and hashed, the hash generated
        #contains a certain number of leading 0 or any character
        #str can be used to convert a string
        nonce = 0
        proof_of_work_part_input = (self.hash_block(Blockchains.get_last_block_of_chain()) + str(Transaction.Transaction_pool) + str(nonce)).encode()
        proof_of_work = hashlib.sha256(proof_of_work_part_input).hexdigest()
    
        while not proof_of_work[0:2] == self.__proof_of_work_requirement:
            nonce += 1
            proof_of_work_part_input = (self.hash_block(Blockchains.get_last_block_of_chain()) + str(Transaction.Transaction_pool) + str(nonce)).encode()
            proof_of_work = hashlib.sha256(proof_of_work_part_input).hexdigest()
        return nonce

    def hash_block(self, block):
        """
            block is expected to be a list or dictionary
        """
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def has_valid_proof(self, block):
        """
            block is expected to be a list or dictionary
        """

        proof = ( str(block['transactions'][1:]) + str(block['previous_hash']) + str(block['nonce']) ).encode()
        guess = hashlib.sha256(proof).hexdigest()
        return guess[0:2] == self.__proof_of_work_requirement

