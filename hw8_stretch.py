#!/usr/bin/env python

"""
Stretch goals:

Create a script that imports the Banking class and instantiates two users with balances.

Update the script to have the users withdraw from their bank account

Update the script to have the users deposit to their account

Print the user's balance.

Any user can enter a name and be gifted with a $10,00 bak account.
The user can select from a menu to check their balance, make a deposit or make a withdrawal.

"""
# imports the class that was created for hw8
import hw8

# instantiates the user by name that is inputted
# requires that only letters are inputted
account_name = ""
while (not account_name.isalpha()):
    account_name = input("\nEnter the name on your account: ")
    if not account_name.isalpha():
        print("\nPlease enter only letters for your name.")
print("Welcome, {}!\n\nYou get $10,000 and you get $10,000.\nIn fact everyone in the audience today gets $10,000!!\n".format(account_name))

account_name = hw8.BankAccount(name = account_name)

# menu that prompts the user for what action they would like to take
# validates that only integers 1 through 4 are entered
# makes calls to to methods in the imported class to complete the requested actions
while True:
    try:
        user_input = ""
        user_input = int(input("What would you like to do?\n"
                        "1. Get Balance\n"
                        "2. Deposit\n"
                        "3. Withdraw\n"
                        "4. Exit\n\n"
                        "Enter your choice: "))
    except ValueError:
            print("\nPlease enter a number from the menu.")

    if user_input == 1:
        account_name.current_balance()
    elif user_input == 2:
        while True:
            try:
                amount = float(input("How much do you want to deposit?"))
                account_name.deposit(amount)
                break
            except ValueError:
                print("\nPlease enter a number that includes only a decimal place.\n")

    elif user_input == 3:
        while True:
            try:
                amount = float(input("\nHow much do you want to withdraw?"))
                account_name.withdrawal(amount)
                break
            except ValueError:
                print("\nPlease enter a number that includes only a decimal place.")

    elif user_input == 4:
        print("\nThanks for banking at Bank Oprah!")
        break
    else:
        print("\nPlease. Work with me. It is not time to think outside of the box.\n")