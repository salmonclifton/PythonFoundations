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
valid = "no"
repeat = "yes"
correct_guesses = []
incorrect_guesses = []

while index < max_guesses:
    # get user input of a letter
    while valid == "no" or repeat == "yes":
        guess = input("What letter do you want to guess? ")
        #guess = input("What letter do you want to guess? ")
        guesses = incorrect_guesses + correct_guesses
        guesses.sort()
        # validate that the user is not repeating a guess
        if guess in guesses:
            print("\nPrevious guesses: ", ' '.join('{}'.format(*i) for i in (guesses)))
            print("Please enter a letter that you have not guessed before.")
        else:
            repeat = "no"
        #validate that the user is entering a single letter
        if (not guess.isalpha()) or (len(str(guess))) != 1:
            print("Please guess a single letter.")
        else:
            valid = "yes"

    valid = "no"
    repeat = "yes"

    # check if the letter is in the animal name
    # store the guessed letter in a list
    if guess in animal:
        correct_guesses.append(guess)
        print("Correct: ", correct_guesses)
    else:
        incorrect_guesses.append(guess)
        print("Inorrect: ", incorrect_guesses)
    # increment the sentry variable
    index += 1

    # print out the status of the game using a for loop (go though the letters in the animal name and see if they're in the guess letter list
    status =[]
    for letter in animal:
        if letter in correct_guesses:
            #print("Yes!")
            status.append(letter)
        else:
            #print("No!")
            status.append("-")
    print(' '.join('{}'.format(*i) for i in (status)))

    # if all of the letters in the animal are in the guess letter list, break and congratulate the user
    if "-" not in status:
        print("You win!")
        break
    # if the sentry variable is bigger or equal to the guesses, break and console the loser
    if index > length:
        print("You lose!")
        break
