blockchain = [ ]

def get_last_block_of_chain():
    #blockchain[-1] is the last block of the blockchain, however [1] is the genesis block of the blockchain
    return blockchain[-1]

def add_block(data = 0.1, last_block = [1] ):
    #Append the last block into the new block and then the new value for the current block
    blockchain.append( [last_block, data ])


add_block(4.5)
add_block(3.5, get_last_block_of_chain())

#Returns a string, but to be casted to float
tx_amount = input("Please enter transaction data/amount ")

add_block(last_block = get_last_block_of_chain(), data = float(tx_amount) ) 

print(blockchain)