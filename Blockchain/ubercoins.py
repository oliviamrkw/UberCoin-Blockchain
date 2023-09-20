# calculates UberCoins based on distance
def calculate_ubercoins(distance): 
    return distance * 2.6 #2.6 ubercoins for 1 km

# calculates money based on amount of UberCoins
def calculate_money(ubercoins):
    return ubercoins * (120/26) # $120/26 for every ubercoin

# adds a wallet id to a dictionary
def add_id_to_list(id, dictionary):
    dictionary[id] = 0

# adds UberCoins to a wallet ID in a dictionary
def add_ubercoins_to_id(id, ubercoins, dictionary):
    dictionary[id] += ubercoins
