blockchain = [ ]

def get_last_block_of_chain():
    #blockchain[-1] is the last block of the blockchain, however [1] is the genesis block of the blockchain
    return blockchain[-1]

def add_block(data = 0.1, last_block = [1] ):
    #Append the last block into the new block and then the new value for the current block
    blockchain.append( [last_block, data ])

def accept_block_data():
    #Returns a string, but to be casted to float
    tx_amount = input("Please enter transaction data/amount ")
    return float(tx_amount)

tx_amount = accept_block_data();
add_block(data = float(tx_amount) ) 

while True:
    add_block( accept_block_data(), get_last_block_of_chain())
    """ 
        Understanding loops 
        :for, while
    :conditional statement
    """
    for block in blockchain:
        print(block)







    





 