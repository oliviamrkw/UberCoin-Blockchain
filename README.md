# UberCoin Blockchain
Made for the Uber Global Hackathon!

### SUMMARY;
This Python code is a prototype of a software that calculates the number of UberCoins earned by a user when taking public transit. It organizes this data by creating a basic blockchain. 

### FUNCTIONALITY: 
The code prompts the user to input:
1. a Wallet ID
2. distance travelled in kilometers

It then converts the distance to the number of ubercoins (2.6/km). 
All three of these values + the hash of the previous block (calculated by the Secure Hash Algorithm 256-bit from the haslib library) are then added to the current block in the blockchain. It displays all of these values as well as the total number of UberCoins for the Wallet ID inputted. 
