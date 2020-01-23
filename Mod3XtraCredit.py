#!/usr/bin/env python

"""
Make a word guess game of your favorite animals.

Goal: A user must guess an animal name by guessing the letters in the name, one letter at a time.

Store an animal name in a variable
A user gets a number of guesses equal to 3 plus the length of the animal name
Use a while loop to get user input (guess a letter!) until they run out of guesses
Output the game status:  currently matching letters of the animal using a for loop
The game ends when they run out of guesses or when they guess the animal


Pseudocode

# make a variable with an animal name

# get the number of letters in the animal name (use len)

# set the number of guesses to be the animal name length plus 3

# use a while loop with a sentry variable

   # get user input of a letter

  # check if the letter is in the animal name

  # store the guessed letter in a list

  # increment the sentry variable

  # print out the status of the game using a for loop (go though the letters in the animal name and see if they're in the guess letter list

  # if all of the letters in the animal are in the guess letter list, break and congratulate the user

  # if the sentry variable is bigger or equal to the guesses, break and console the loser
"""

# make a variable with an animal name
animal = list("elephant")

# get the number of letters in the animal name (use len)
length = len(animal)
print(length)

# set the number of guesses to be the animal name length plus 3
max_guesses = length + 3

# use a while loop with a sentry variable
index = 0
while index <= length:
    # increment the sentry variable
    index += 1

    # get user input of a letter
    guess = input("What letter do you guess? ")

    # check if the letter is in the animal name
    if animal.index(guess):
        for index, letter in enumerate(animal):
            print("yes!")
            check = animal.index(guess)
            print(check)
    # store the guessed letter in a list

    # increment the sentry variable

    # print out the status of the game using a for loop (go though the letters in the animal name and see if they're in the guess letter list

    # if all of the letters in the animal are in the guess letter list, break and congratulate the user

    # if the sentry variable is bigger or equal to the guesses, break and console the loser