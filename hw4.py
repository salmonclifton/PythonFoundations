#!/usr/bin/env python

"""
Define two lists at the top of your file such as the ones below:

names = ["Aliyah", "Bob", "Cathy", "Dan", "Ed", "Frank", "Darnell",
    "Gary", "Shanice", "Irene", "Jack", "Kelly", "Demetrius"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19, 30]
These lists should match up, so Aliyah's age is 20, Bob’s age is 21, and so on. In this example,
the names should be the keys and the age should be the value.

Use the zip function to merge these lists into a dictionary.
Include a comment - What data type does zip() return?
Include a comment - How do you coerce that to the right data type?
Give a the user 5 tries to check to see if a name is in the dictionary
give them up to five tries by using a sentinel variable
use a while loop to continue to ask if they haven't found a name in the dictionary or until they run out of tries
ask the user to input a name
check if the name is in the dictionary (hint: use membership or get)
if the user is in the dictionary, return the user's age
if the user is not in the dictionary, return an error message
Your program should print out the response, as follows:

"Please input an user to find out their age: "
"Aliyah"
"Aliyah is 20!"

"Please input an user to find out their age: "
"Tabitha"
"There is nobody here named Tabitha, please try again: "
"""

# Dictionary creator function from two lists and returns the dictionary to main function
def dict_creator():
    # Crete names list
    names = ["Ma", "Mintwab", "Shierra", "Aaron", "Dave", "Dan", "Kim", "Brent", "Holly", "Mike", "Vanessa", "Jeff", "Ken", ]
    # Create ages list
    ages = [35, 25, 32, 47, 56, 47, 48, 48, 25, 32, 27, 25, 35]

    #Testing that the lists are of equal length
    #print(len(names))
    #print(len(ages))

    #Test to find the data type returned by zip(). It is <class 'zip'>.
    #print(type(zip(names, ages)))

    #'Coerce' the data type by casting as dict.
    people_dict = dict(zip(names, ages))

    #Test to find the data type returned by casting as dict() data type. It is <class 'dict'>.
    #print(type(people_dict))

    return (people_dict)

# People guesser function that prompts user for input, validates the input and searches the dictionary
def people_guesser(people_dict):
    # Initialize the sentry variable
    i = 0

    # while loop to limit the user to 5 incorrect guesses
    while i < 5:
        # Increment the sentry variable
        i += 1
        #prompt and store the user's input
        name_guess = input("\nWhat name would you like to guess? ")

        # validate that the user is entering a single letter
        while (not name_guess.isalpha()):
            print("Please guess a name containing letters only.")
            name_guess = input("\nWhat name would you like to guess? ")

        # Store what the .get returns as guess result
        guess_result = people_dict.get(name_guess)

        # If name guessed is not in the dictionary then inform the user
        if guess_result == None:
            print("I'm sorry, Dave, that name is not in the dictionary.")
        # User notified that name is in the dictionary and breaks from the while loop
        else:
            print("Success!")
            break

    # while loop ends and returns the guess result (the age or None) and the name guessed
    return guess_result, name_guess

# main function provides flow control by making calls to the dictionary creator and people guesser functions
def main():
    # Call to dictionary creator function expecting the dictionary to be returned
    people_dict = dict_creator()

    # Provides a brief functionality statement to the user
    print("\n\nYou have five tries to guess a first name that is in the dictionary. Good Luck!")

    # Calls the people guesser function and expects the guess result and name guessed to be returned
    guess_result, name_guess = people_guesser(people_dict)

    # If a dictionary value (age) is not returned (None) then outputs message to the user
    if guess_result == None:
        print("You obviously do not know any of these people. You should get out more!")

    # If a dictionary value is returned then output the name and age
    else:
        print(name_guess, "is", guess_result, "years old.")

main()