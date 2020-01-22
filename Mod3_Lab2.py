#!/usr/bin/env python

# pseudocode
import random

# generate a random number between 1 and 10
number = random.randint(1,10)

# create a sentinel variable to track the number of guesses a user has used
counter = 0

print("Hi! Welcome to the number guesser.  I've picked a number between 1 and 10.\n\
You get three attempts to guess my number.")

# make a while loop using the number of guesses a user has used
while counter < 3:
       # increment the sentinel variable
    counter += 1
       # get a number from the user
    guess = input("Guess the number between 1 and 10:\n")
    guess = int(guess)
       # check that the sentinel variable for the guess doesn't match the number
    if guess == number:
             # if it does match print congratulations and break
        print("You are correct!")
        break
             # if it doesn't match see if it's higher or lower than the number and print a hint
    if guess < number:
        print("Higher!!!")
    if guess > number:
        print("Lower!!!")

# if the user didn't guess the number print a consolation
if counter == 3:
    print("You are a loser!!!\nThe number was ", number)