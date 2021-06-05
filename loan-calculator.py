"""
Author: Jacob Mask
Created: 6/5/2021
Modified: 6/5/2021
Notes: An app that calculates multiple monthly loan payments.
"""

import os

def main():
    if os.path.exists("data.txt"):
        print("Loading your data")
        firstTimeUI()
    else:
        print("Welcome new user")
        print("Creating a data.txt file for your storage")
        dataFile = open("data.txt", "w+")
        dataFile.write("test")
        dataFile.close
        firstTimeUI()
s
def firstTimeUI():
    loans = {}
    loanName = input("Enter loan name: ")
    print("Insert the yearly interest rate without symbols")
    interest = input("Example: 2.5 not .025: ")
    amount = input("Total amount of loan: ")
    loans[loanName] = [amount, interest]

if __name__ == '__main__':
    main()