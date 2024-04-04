"""
Class name:  ChangePurse

Class attributes:    ( * denotes private access )
    amount *

Class methods:
    __init__(self, amount = 0)     
        # changepurse initially contains amount cents, unless the parameter
        is not provided, in which case the default 0 is used

    __str__(self)   
        #returns string with amount in changepurse in format $dollars.cents

    addChange(self, amount)  
        #parameter amount is added to contents of the changepurse

    removeChange(self, amount)  
        #parameter amount is deducted from contents of changepurse 
        if rhere is enough money. Otherwise an an exception is thrown

    __lt__(self, purse)   
        #returns True if  the amount in calling object is less than parameter 
        object amount. Otherwise False is returned

    __gt__(self, purse) 
        #returns True if the amount in the calling object is greater than 
        parameter object amount. Otherwise False is returned

    __eq__(self, purse)  
        #returns True if the amount in the calling object is equal to the amount 
        in the parameter object. Otherwise False is returned.

Code the class as described above. Place this class in a file purse.py.

In another file write a main program which creates 2 objects of ChangePurse, 
    and demonstrates that each method of ChangePurse works correctly.  Be sure 
    to import ChangePurse in the main file so that the class is available.
"""
# this is "the other file"
import purse
import random

# initialize purses
momsPurse = purse.ChangePurse(random.randint(1,10000)/100)
grannysPurse = purse.ChangePurse(random.randint(1,10000)/100)

# make comparisons
print(f"momsPurse: {momsPurse}")
print(f"grannysPurse: {grannysPurse}")
if momsPurse > grannysPurse: print("mom has more money.")
elif momsPurse < grannysPurse: print("granny has more money.")
elif momsPurse == grannysPurse: print("mom and grannys money are the same")

# perform transactions
myWallet=purse.ChangePurse()
myWallet.addChange(grannysPurse.removeChange(
    max(grannysPurse.balance, random.randint(1,100)/100)))
myWallet.addChange(momsPurse.removeChange(
    max(grannysPurse.balance, random.randint(1,100)/100)))
print(f"I have {myWallet} which I absolutely did not take from anyones purse.")
