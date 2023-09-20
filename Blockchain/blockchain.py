import hashlib
from ubercoins import *

class UberCoinBlockchain:

    # initializes empty blockchain and creates initial block
    def __init__(self): 
        self.chain = [] 
        self.create_initial_block()

    # creates initial block and sets default values
    def create_initial_block(self): 
        initial_block = {
            'id': 0,
            'distance': 0.0,
            'ubercoins': 0.0,
            'previous_hash': '0',
        }
        initial_block['hash'] = self.calculate_hash(initial_block)

        self.chain.append(initial_block) # adds initial block to blockchain

    # adds a new block to the blockchain
    def add_block(self, id, distance):
        previous_block = self.chain[-1]

        if previous_block['hash'] != self.calculate_hash(previous_block): # checks if the previous hash is valid
            raise Exception("Previous block's hash is not valid.")

        ubercoins = calculate_ubercoins(distance)

        # assigns the values
        new_block = {
            'id': id,
            'distance': distance,
            'ubercoins': ubercoins,
            'previous_hash': previous_block['hash'],
        }
        new_block['hash'] = self.calculate_hash(new_block)

        self.chain.append(new_block) # adds the block

    # uses the hashlib library to create a unique hash based on the data
    def calculate_hash(self, block):
        return hashlib.sha256(f"{block['id']}_{block['distance']}_{block['previous_hash']}".encode()).hexdigest() 

    # prints a specific block hash
    def print_block_hash(self, index):
        print(f"{self.chain[index]['hash']}")

    # prints the block hash, the wallet id, and the ubercoins received
    def print_all(self):
        for index, block in enumerate(self.chain[1:], start = 1):
            print("-------")
            print(f"Block {index} Hash: {block['hash']}")
            print(f"Wallet ID: {block['id']}")
            print(f"UberCoins received: {block['ubercoins']:.2f}")
