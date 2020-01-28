genesis_block = {
    'previous_hash': '',
    'index' : 0,
    'transactions' : []
}

blockchain = [ genesis_block ]
transaction_pool = [ ]
participants = ('Mark', 'Samuel', 'Deola', 'Manuel')


def get_last_block_of_chain():
    #blockchain[-1] is the last block of the blockchain
    return blockchain[-1]

def add_transaction(recipient, sender=participants[0], amount = 1.0):
    transaction = { 'sender': sender, 'recipicient': recipient, 'amount' : amount }
    transaction_pool.append(transaction) 

def hash_block(block):
    return '-'.join( [str(block[key])]  for key in  block )

def mine_block():
    
    last_block = get_last_block_of_chain()
    
    if valid_blockchain():
        block = {
            'previous_hash': hash_block(last_block),
            'index' : len(blockchain),
            'transactions' : transaction_pool 
        }

        blockchain.append(block)
        return True
    return False



def accept_transaction_data():
    #Returns a string, but to be casted to float
    tx_amount = input("Please enter transaction data/amount ")
    tx_receipient = input("Please enter receipient ")
    return tx_amount, tx_receipient


def valid_blockchain():
    """ Verify that blockchain is valid """
    block_index = 0
    is_blockchain_valid = True
    
    last_block = get_last_block_of_chain()

    for (index, block) in enumerate(blockchain):
        
        if index < 1:
            continue

        if (block['previous_hash'] == hash_block(last_block)) and (index > 0):
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


def get_balance(participant):
    pass

if len(participants) == len(set(participants)):

    #Add genesis block
    add_transaction(recipient='Samuel', amount= 1.0)

    """ 
        Understanding loops 
        :for, while
        :conditional statement
    """

    while True:
        print("Please make a choice: 1-Add block, 2-Display blockchain, 3-Quit loop")
        user_choice = input("Enter a choice ")
        
        if user_choice == '1':
        
            tx_amount, tx_receipient = accept_transaction_data()
            add_transaction( recipient=tx_receipient, amount= tx_amount )
        
        elif user_choice == '2':
            
            if mine_block() == True:
                transaction_pool = [];

            for block in blockchain:
                print(block)
            else:
                print("-"*15)

        elif user_choice == '3':
            break
        else:
            print("Invalid input")

        
    
    #Testing the range function
    for i in range(10):
        print(i)
    else:
        None
else:
    print('there are multiple participants.')








    





 