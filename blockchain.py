blockchain = [ ]
transaction_pool = [ ]


def get_last_block_of_chain():
    #blockchain[-1] is the last block of the blockchain, however [1] is the genesis block of the blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_block(data, last_block):
    #Append the last block into the new block and then the new value for the current block
    if last_block == None:
        last_block = [1]
    
    if valid_blockchain():
        blockchain.append( [last_block, data ])
        return True
    return False

def accept_block_data():
    #Returns a string, but to be casted to float
    tx_amount = input("Please enter transaction data/amount ")
    return float(tx_amount)


def valid_blockchain():
    """ Verify that blockchain is valid """
    block_index = 0
    is_blockchain_valid = True
    for block in blockchain:
        if block_index < 1:
            continue

        if (block[0] == blockchain[block_index-1]) and (block_index > 0):
            is_blockchain_valid = True
            continue
        else:
            is_blockchain_valid = False
            break

        block_index += 1
    else:
        #The else execute immediately loop completion, similar to final block in exception handling probably other PL
        print("Blockchain verification completed")

    return is_blockchain_valid




#Add genesis block
add_block(0.1, last_block = get_last_block_of_chain())

""" 
    Understanding loops 
    :for, while
    :conditional statement
"""

while True:
    print("Please make a choice: 1-Add block, 2-Display blockchain, 3-Quit loop")
    user_choice = input("Enter a choice ")
    if user_choice == '1':
        tx_amount = accept_block_data()
        add_block( tx_amount, get_last_block_of_chain())
    elif user_choice == '2':
        for block in blockchain:
            print(block)
        else:
            print("-"*15)
    elif user_choice == '3':
       break
    else:
        print("Invalid input")

    if not valid_blockchain():
        break
    
   
#Testing the range function
for i in range(10):
    print(i)
else:
    None









    





 