# Initializing our blockchain list
blockchain  = []


def get_last_blockchain_value():
    """Returns the last value of current blockchain."""
    return blockchain[-1]


def add_value(transaction_amount,last_transaction_value=[1]):
    """Append a new value as well as last value to the blockchain
            Arguments:
            :transaction_amout: The amount that should be added
            :last_transaction_value: The last blockchain transaction (Deafult([1]))
    """
    blockchain.append([last_transaction_value,transaction_amount])


def get_user_input():
    """ Returns the inpput to thw user"""
    return(float(input('Your Transaction Amount Please: ')))


  
tx_amount= get_user_input()
add_value(tx_amount)

tx_amount= get_user_input()
add_value(last_transaction_value=get_last_blockchain_value(),transaction_amount=tx_amount)

tx_amount= get_user_input()
add_value(tx_amount,get_last_blockchain_value())

print(blockchain)