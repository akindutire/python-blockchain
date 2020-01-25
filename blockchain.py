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

#Add genesis block
add_block() 

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
    elif user_choice == '3':
       break
    else:
        print("Invalid input")







    





 