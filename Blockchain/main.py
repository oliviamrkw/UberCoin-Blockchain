from blockchain import UberCoinBlockchain
from ubercoins import *

blockchain = UberCoinBlockchain()

id_list = {} # dictionary to store amount of UberCoins for each Wallet ID

while True:
    id_input = input("\nEnter Wallet ID (1 digit only): ") # for this prototype the id is 1 digit long for simplicity
    
    # checks if the id and distance inputted are valid, assigns them to variables
    if id_input.isdigit() and len(id_input) == 1 and id_input != '0': 
        id = int(id_input)
        try:
            distance = float(input("How many kilometers: "))
            if distance <= 0: 
                print("Distance must be a number over 0")
                continue
        except ValueError:
            print("Invalid input.")
            continue # restarts loop
        
        # checks if id is in the list already, adds the id if not and adds the number of ubercoins (calculated from the distance) as the value
        if id not in id_list: 
            add_id_to_list(id, id_list)
        add_ubercoins_to_id(id, calculate_ubercoins(distance), id_list)

        blockchain.add_block(id, distance) # adds new block to blockchain

        blockchain.print_all() # prints block hash, wallet id, ubercoins received
        print(f"Total UberCoins for Wallet ID {id}: {id_list.get(id):.2f}")
    else:
        print("Wallet ID must be a non-zero 1 digit number.")
