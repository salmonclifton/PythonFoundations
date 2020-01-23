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
    print("This program prompts you for a range of numbers and then outputs the even numbers and\
the sum of the odd numbers.\n")
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
        #Create list of odd numbers based on the first odd number (rather than accumulating through looping)
        elif index == 1 or index ==2:
            odd_numbers = list(range(start_num, end_num + 1, 2))

    #Print out the number and index of each item in the list that is odd
    print("\nHere are all of the odd numbers in your range:\n[Index] Number")
    for index, number in enumerate(odd_numbers):
        print("[" + str(index) + "] " +str(number))
    print("The sum of the odd numbers in your range equals: " + str(sum(odd_numbers)))

evensAndOdds()


"""
Stretch Goal:

Upgrade FizzBuzz with a for loop and submit as a separate file!
Does your fizzbuzz print out the right values that you expect?
"""
def threesAndFives():
    print("\n\nThis program prompts you for how many random numbers between 50 and 100 do you want to generate and\
tests to see if they are divisible by three and five.\n")
    #Prompt user for many random numbers that they want to generate
    quantity = int(input("How many random numbers do you want to generate between 50 and 100? "))
    #For loop will repeat for the number of times the user requested
    for i in range(1, quantity+1):
        #Generate a random number between 50 and 100 and store
        import random
        test_num = random.randint(50,100)
        print("\nThe pseudo-randomly generated number is: " + str(test_num))
        #Display 'fizzbuzz!' if test_num is divisible by both 3 and 5
        if (test_num%3) == 0 and (test_num%5) == 0:
            print("fizzbuzz!\n" + str(test_num) + " is evenly divisible by 3 & 5.")
        #Display 'buzz!' if test_num is divisible by 5
        elif (test_num%5) == 0:
            print("buzz\n" + str(test_num) + " is evenly divisible by 5.")
        #Display 'fizz!' if test_num is divisible by 3
        elif (test_num%3) == 0:
            print("fizz\n" + str(test_num) + " is evenly divisible by 3.")
        #Otherwise display the value
        else:
            print(str(test_num) + " is not divisible by 3 or 5.")

threesAndFives()