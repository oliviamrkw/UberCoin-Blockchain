# UberCoin Blockchain
This GitHub repository contains files for the frontend (website) and backend (python code) of our Uber Global Hackathon submission!

## Frontend
### SUMMARY:
This HTML and CSS code is a prototype for how UBERCoins would be integrated onto the Uber website. It consists of two pages, the first information page, and the second functional page. The first page holds information for what UBERCoins are and how they work. The second page is a mockup of how customers would be able to check how many UBERCoins they would earn for their trip and check their personal Wallet for their UBERCoin balance. The two webpages were styled with the Uber website design in mind.

### INTEGRATION WITH BACKEND:
The frontend is not currently integrated with the backend due to time restrictions. In the future, we would use a web framework software called Flask in order to integrate the frontend with the backend.

## Backend
### SUMMARY:
This Python code is a prototype of a software that calculates the number of UberCoins earned by a user when taking public transit. It organizes this data by creating a basic blockchain. 

### FUNCTIONALITY: 
The code prompts the user to input:
1. a Wallet ID
2. distance travelled in kilometers

It then converts the distance to the number of ubercoins (2.6/km). 
All three of these values + the hash of the previous block (calculated by the Secure Hash Algorithm 256-bit from the haslib library) are then added to the current block in the blockchain. It displays all of these values as well as the total number of UberCoins for the Wallet ID inputted. 
