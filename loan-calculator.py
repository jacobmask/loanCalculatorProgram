"""
Author: Jacob Mask
Created: 6/5/2021
Modified: 6/5/2021
Notes: An app that calculates multiple monthly loan payments.
"""

import pandas as pd
import os
import time

def main():
    if os.path.exists("data.csv"):
        print("Loading your data")
        UI()
    else:
        print("Welcome new user")
        print("Creating a data.csv file for your storage")
        dataFile = open("data.csv", "w+")
        dataFile.close()
        firstTimeUI()

def firstTimeUI():
    loanName = input("Enter loan name: ")
    print("Insert the yearly interest rate without symbols")
    interest = input("Example: 2.5 not .025: ")
    amount = input("Total amount of loan: ")
    data = [[loanName, amount, interest]]
    df = pd.DataFrame(data, columns = ['Name', 'Amount', 'Interest'])
    print(df)
    df.to_csv("data.csv",index=False)
    print("Congrats on inserting your first loan!")
    UI()

def UI():
    entry = "null"
    while entry != "Z":
        print("Type a letter from the below options")
        print("A: View Loans")
        print("B: Change/Add/Remove loans")
        print("C: Calculator")
        #print("D: Payments Simulator")
        print("Y: Restart program")
        print("Z: Close program")
        entry = input("Type a single letter: ")
        if entry == "A" or entry == "a":
            viewLoans()
        elif entry == "B" or entry == "b":
            changeLoans()
        elif entry == "C" or entry == "c":
            calculator()
        elif entry == "Y" or entry == "y":
            main()
        elif entry == "Z" or entry == "z":
            exit()
        else:
            print("\nEntry invalid, try again.\n")

def viewLoans():
    df = pd.read_csv("data.csv")
    print(df)


def changeLoans():
    entry = "null"
    while entry != "Z":
        print("\n\n\nUpdate Loan Options:")
        print("A: Add a loan")
        print("B: Update a loan")
        print("C: Delete a loan")
        print("Z: Back to main menu")
        entry = input("Type a single letter: ")
        if entry == "A" or entry == "a":
            addLoan()
        elif entry == "B" or entry == "b":
            updateLoan()
        elif entry == "C" or entry == "c":
            deleteLoan()
        elif entry == "Z" or entry == "z":
            UI()
        else:
            print("\nEntry invalid, try again\n")

def addLoan():
    df = pd.read_csv("data.csv")
    print('\n',df,'\n')
    loanName = input("Enter loan name: ")
    print("Insert the yearly interest rate without symbols")
    interest = input("Example: 2.5 not .025: ")
    amount = input("Total amount of loan: ")
    df2 = pd.DataFrame([[loanName, amount, interest]], columns=['Name','Amount','Interest'])
    frames = [df, df2]
    df = pd.concat(frames)
    df.to_csv("data.csv", index=False)
    print('\n',df,'\n')

def updateLoan():
    print("Not yet complete")

def deleteLoan():
    print("Not yet complete")

def calculator():
    print("Not yet complete")



if __name__ == '__main__':
    main()