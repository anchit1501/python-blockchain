# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """Returns the last value of current blockchain."""
    # len inbuild fuction for checking length of a variable
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction_value=[1]):
    """Append a new value as well as last value to the blockchain
            Arguments:
            :transaction_amout: The amount that should be added
            :last_transaction_value: The last blockchain transaction (Deafult([1]))
    """
    if last_transaction_value == None:
        last_transaction_value = [1]
    blockchain.append([last_transaction_value, transaction_amount])


def get_transaction_value():
    """ Returns the input to the user"""
    return(float(input('Your Transaction Amount Please: ')))


def get_user_choice():
    """ Returns the input to the user"""
    return(input('Your Choice: '))


def print_blockchain_elements():
    # Output the blockchain list to the console
    # For Loop
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-'*50)


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            # break
    return is_valid
            
waiting_for_input = True


# While Loop
while waiting_for_input:
    print('Please Choose')
    print('1. Add new trnsaction value')
    print('2. Output the blockchain blocks')
    print('3. Manipulate Blockchain')
    print('4. Quit')
    
    user_choice=get_user_choice()
    if user_choice == '1':
        tx_amount=get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())

    elif user_choice == '2':
        print_blockchain_elements()

    elif user_choice == '3':
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    elif user_choice == '4':
        # Option 1
        # break

        # continue
        # Skips the code to restart the loop
        
        # Option 2
        waiting_for_input = False


    else:
        print('Invalid Input, Please pick value from list')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain')
        break
    # print('Choice Registered!!!!')
# else with loop is executed after loop is exited
else:
    print('User Exited!!')
       
print('Done!')

# print(blockchain)
