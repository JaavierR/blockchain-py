# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """Return the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction):
    """Append a new value as well as the last blockchain value to the blockchain.

    Args:
        transaction_amount ([type]): The amount that should be added.
        last_transaction (list, optional): The last blockchain transaction.
            Defaults to [1].
    """
    if last_transaction is None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """Return the input of the user (a new transaction amount) as a float."""
    user_input = float(input("Your transaction amount please: "))
    return user_input


def get_user_choice():
    """Get the user choice."""
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """Output the blockchain list to the console."""
    for block in blockchain:
        print("Outputting Block")
        print(block)


def verify_chain():
    for index, block in enumerate(blockchain):
        if index >= 1 and block[0] != blockchain[index - 1]:
            return False

    return True


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchains blocks")
    print("h: Manipulate the chain")
    print("q: Quit")

    user_choice = get_user_choice()

    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")

    if not verify_chain():
        print("Invalid blockchain!")
        break

print("Done!")
