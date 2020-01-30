import functools


genesis_block = {
    'previous_hash': '',
    'index' : 0,
    'transactions' : []
}

blockchain = [ genesis_block ]
transaction_pool = [ ]
participants = ('Mark', 'Samuel', 'Deola', 'Manuel', 'Ay', '*')
Miner = participants[4]
mining_fee = 0.0002

def get_last_block_of_chain():
    #blockchain[-1] is the last block of the blockchain
    return blockchain[-1]

def add_transaction(recipient, sender=participants[0], amount = 2.0):
    if recipient in participants and (sender in participants):
        
        if get_balance(sender) <= amount:
            print("Insufficient balance")
            return

        global mining_fee
        amount -= mining_fee
        mining_fee += mining_fee
        
        transaction = { 'sender': sender, 'recipicient': recipient, 'amount' : amount }
        transaction_pool.append(transaction) 
    else:
        print("Unknown participant")

def hash_block(block):
    #return '-'.join( str(block[key])  for key in  block )
    return block['index']

def mine_block():
    
    last_block = get_last_block_of_chain()
    
    if valid_blockchain() == True:
        

        transaction = { 'sender': '*', 'recipicient': Miner, 'amount' : mining_fee }
        transaction_pool.append(transaction) 

        block = {
            'previous_hash': hash_block(last_block),
            'index' : len(blockchain),
            'transactions' : transaction_pool 
        }

        blockchain.append(block)
        return True
    else:
        print("Blockchain is invalid")
        return False



def accept_transaction_data():
    #Returns a string, but to be casted to float
    tx_amount = float(input("Please enter transaction data/amount "))
    tx_receipient = input("Please enter receipient ")
    return tx_amount, tx_receipient


def valid_blockchain():
    """ Verify that blockchain is valid """
    is_blockchain_valid = True

    for (index, block) in enumerate(blockchain):
        
        if index < 1:
            continue

        if block['previous_hash'] == hash_block(blockchain[index-1]):
            is_blockchain_valid = True
            continue
        else:
            is_blockchain_valid = False
            break

    else:
        #The else execute immediately loop completion, similar to final block in exception handling probably other PL
        print("Blockchain verification completed")

    return is_blockchain_valid


def get_balance(participant):
    tx_sender_amounts = [ [ tx['amount'] for tx in block['transactions'] if tx['sender'] == participant and len(tx) > 0] for block in blockchain ]
    tx_receiver_amounts = [ [ tx['amount'] for tx in block['transactions'] if tx['recipicient'] == participant and len(tx) > 0] for block in blockchain ]
    
    tx_dict = { 'credits': 0, 'debits': 0 }
    for block_of_amounts in tx_sender_amounts:
        if len(block_of_amounts) > 0:
            tx_dict['debits'] += sum(block_of_amounts)

    for block_of_amounts in tx_receiver_amounts:
        if len(block_of_amounts) > 0:
            tx_dict['credits'] += sum(block_of_amounts)

    return tx_dict['credits'] - tx_dict['debits']

if len(participants) == len(set(participants)):

    #Add genesis block
    add_transaction(recipient='Samuel', amount= 1.0)

    """ 
        Understanding loops 
        :for, while
        :conditional statement
    """

    while True:
        print("Please make a choice: 1-Add block, 2-Display blockchain, 4-Get balannce, 3-Quit loop")
        user_choice = input("Enter a choice ")
        
        if user_choice == '1':
        
            tx_amount, tx_receipient = accept_transaction_data()
            add_transaction( recipient=tx_receipient, amount= tx_amount )
        
        elif user_choice == '2':
            
            if mine_block() == True:
                transaction_pool = []
                for block in blockchain:
                    print(block)
                    print("-"*15)
                    
            else:
                print("Error mining new block")                

        elif user_choice == '3':
            break
        elif user_choice == '4':
            participant = input("Participant ")
            print("Balance is {:-^5.2f}".format(get_balance(participant)))
        else:
            print("Invalid input")

        
    
else:
    print('there are multiple participants.')








    





 