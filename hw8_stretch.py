import hw8

account_name = input("Enter the name on your account: ")
print("Welcome, {}!\n\nYou get $10,000 and you get $10,000.\nIn fact everyone in the audience today gets $10,000!!\n".format(account_name))

account_name = hw8.BankAccount(name = account_name)

while True:
    try:
        user_input = 0
        user_input = int(input("What would you like to do?\n"
                        "1. Get Balance\n"
                        "2. Deposit\n"
                        "3. Withdraw\n"
                        "4. Exit\n\n"
                        "Enter your choice: "))
        if user_input == 1:
            account_name.current_balance()
        elif user_input == 2:
            amount = float(input("\nHow much do you want to deposit?"))
            account_name.deposit(amount)
        elif user_input == 3:
            amount = float(input("\nHow much do you want to withdraw?"))
            account_name.withdrawal(amount)
        elif user_input == 4:
            print("\nThanks for banking at Bank Oprah!")
            break
        else:
            print("\nPlease. Work with me. It is not time to think outside of the box.")
    except SomeException:
        tb = sys.exc_info()[2]
        raise OtherException(...).with_traceback(tb)
    #except ValueError: print("\nPlease enter a valid number")