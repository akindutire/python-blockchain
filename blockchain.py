blockchain = [ [1] ]

def get_last_block_of_chain():
    return blockchain[-1]

def add_block(data):
    #Append the last block into the new block and then the new value for the current block
    #blockchain[-1] is the last block of the blockchain, however [1] is the genesis block of the blockchain
    blockchain.append( [get_last_block_of_chain(), data ])
    print(blockchain)

add_block(4.5)
add_block(3.5)