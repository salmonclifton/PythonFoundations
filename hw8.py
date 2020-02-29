#!/usr/bin/env python

"""
For your homework, you'll need to create a Banking class that does the following:

Tracks an initial account balance
Tracks deposits in the account
Tracks withdrawals to the account
Prints out a current balance
Prints an error message if someone tries to withdraw more money than what is currently in the account

"""

class BankAccount():
    def __init__(self, name, balance = 10000.00):
        self.name = name
        self.balance = balance

#Add methods for deposits, withdrawals and printing current balance
    def deposit(self, amount):
        self.balance = float(self.balance)
        self.balance = self.balance + amount
        amount = format(amount, ",.2f")
        formatted_balance = format(self.balance, ",.2f")
        print("\nDeposit amount = ${}\nNew balance = ${}\n".format(amount, formatted_balance, ))

    def withdrawal(self, amount):
        self.balance = float(self.balance)
        if amount > float(self.balance):
            formatted_balance = format(self.balance, ",.2f")
            print("\nInsufficient funds.\nCurrent balance = ${}\n".format(formatted_balance))
        else:
            self.balance = self.balance - amount
            amount = format(amount, ",.2f")
            formatted_balance = format(self.balance, ",.2f")
            print("\nWithdrawal amount = ${}\nNew balance = ${}\n".format(amount, formatted_balance))


    def current_balance(self):
        formatted_balance = format(self.balance, ",.2f")
        print("\nCurrent balance = ${}\n".format(formatted_balance))

