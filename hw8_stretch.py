#!/usr/bin/env python

import hw8
account_name = ""
while (not account_name.isalpha()):
    account_name = input("\nEnter the name on your account: ")
    if not account_name.isalpha():
        print("\nPlease enter only letters for your name.")
print("Welcome, {}!\n\nYou get $10,000 and you get $10,000.\nIn fact everyone in the audience today gets $10,000!!\n".format(account_name))

account_name = hw8.BankAccount(name = account_name)

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