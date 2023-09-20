def calculate_ubercoins(distance): # calculates UberCoins based on distance
    return distance * 2.6 #2.6 ubercoins for 1 km

def calculate_money(ubercoins): # calculates money based on amount of UberCoins
    return ubercoins * (120/26) # $120/26 for every ubercoin

def add_id_to_list(id, dictionary): # adds a wallet id to a dictionary
    dictionary[id] = 0

def add_ubercoins_to_id(id, ubercoins, dictionary): # adds UberCoins to a wallet ID in a dictionary
    dictionary[id] += ubercoins