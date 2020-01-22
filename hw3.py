#!/usr/bin/env python

"""
Ask the user to enter a starting and ending number
The user must not enter a starting number less than 1
The user must enter an ending number at least 5 times greater than the starting number
Create checks and error messages for the above
Create a list of integers in the range of the user's starting and ending numbers
Print out the number and index of each item in the list that is even
Sum all the odd numbers in the list using a for loop ( hint: append odd numbers to a list and then sum() that list)
Print out the cumulative sum calculated above (running total)
Wrap your steps in a function and call the function
 Upload your python file to Canvas.
"""
def evensAndOdds():
    #Prompt user to enter a starting number
    while True:
        start_num = int(input("Enter a starting number greater than zero (integer): "))

        #The user must not enter a starting number less than 1
        if start_num > 0:
            break
        else:
            print("Your starting number, " + str(start_num) + ", is not greater than zero.")

    #Prompt user to enter an ending number
    while True:
        end_num = int(input("Enter an ending number (integer) that is greater than " +  str(5*start_num -1) + ": "))

        #The user must enter an ending number at least 5 times greater than the starting number
        if end_num >= 5*start_num:
            break
        else:
            print("Your ending number, " + str(end_num) + ", is not at least 5 times greater than your starting number, " \
                  + str(start_num) + ".")
    #Print out the number and index of each item in the list that is even
    numbers = list(range(start_num, end_num+1))
    print("\nHere are all of the even numbers in your range:\n[Index] Number")
    for index, number in enumerate(numbers):
        if number%2 == 0:
            print("[" + str(number) + "] " +str(number))
        elif index == 1 or index ==2:
            odd_numbers = list(range(start_num, end_num + 1, 2))

    #Print out the number and index of each item in the list that is odd
    print("\nHere are all of the odd numbers in your range:\n[Index] Number")
    for index, number in enumerate(odd_numbers):
        print("[" + str(index) + "] " +str(number))
    print("The sum of the odd numbers in your range equals: " + str(sum(odd_numbers)))

evensAndOdds()
