#!/usr/bin/env python

"""
Make a word guess game of your favorite animals.

Goal: A user must guess an animal name by guessing the letters in the name, one letter at a time.

Store an animal name in a variable
A user gets a number of guesses equal to 3 plus the length of the animal name
Use a while loop to get user input (guess a letter!) until they run out of guesses
Output the game status:  currently matching letters of the animal using a for loop
The game ends when they run out of guesses or when they guess the animal

Stretch goals:

- Instead of guessing one animal, each game should get a new animal!

Create a list of animals
Pick one animal for each game
- Clean the user input before checking it against the animal name.

Make sure the user is guessing letters
Make sure they're guessing one letter
- Use the longest animal name as the number of guesses

- Use a list comprehension to output the game status
"""
play_again = []
def animal_guess():
    #Create a list of animals
    animals = ("ardvark", "bobcat", "cat", "dog", "elephant", "fox", "guerilla", "hyena", "ibis", "jaguar", "kangaroo",\
               "lemur", "monkey", "nightingale", "opossum", "peacock", "rabbit", "squirrel", "tortoise", "vole", "wombat",\
               "zebra")
    animals = list(animals)

    # Randomly pick one of the animals from the list make a variable with an animal name
    number = len(animals)
    import random
    random_animal = random.randint(0, number-1)
    animal = animals[random_animal]
    # get the number of letters in the animal name (use len)
    length = len(animal)

    # set the number of guesses to be the animal name with the most letters plus 3
    maxlength = max(len(i) for i in animals)
    max_guesses = maxlength + 3

    # use a while loop with a sentry variable
    index = 0
    valid = "no"
    repeat = "yes"
    correct_guesses = []
    incorrect_guesses = []

    #Show user the number of letter in the current animal name
    status = ["-" for letter in animal]
    print(' '.join('{}'.format(*i) for i in (status)))
    #Start loop for guesses
    while index <= max_guesses:
        # get user input of a letter
        while valid == "no" or repeat == "yes":
            guess = input("\nWhat letter do you want to guess? ")

            # Store all guesses
            guesses = incorrect_guesses + correct_guesses
            guesses.sort()

            # validate that the user is not repeating a guess
            if guess in guesses:
                print("\nPrevious guesses: ", ' '.join('{}'.format(*i) for i in (guesses)))
                print("Please enter a letter that you have not guessed before.")
            else:
                repeat = "no"

            # validate that the user is entering a single letter
            if (not guess.isalpha()) or (len(str(guess))) != 1:
                print("Please guess a single letter.")
            else:
                valid = "yes"

        valid = "no"
        repeat = "yes"

        # check if the letter is in the animal name
        # append the guessed letter to either the incorrect or correct guesses list
        if guess in animal:
            correct_guesses.append(guess)
            print("\nCorrect, you have", max_guesses - index, "guesses remaining.")
        else:
            incorrect_guesses.append(guess)
            print("\nInorrect, you have", max_guesses - index, "guesses remaining.")

        # increment the sentry variable
        index += 1

        # print out the status of the game using a for loop (go though the letters in the animal name and
        # see if they're in the guess letter list
        status =[]
        status = [letter if letter in correct_guesses else "-" for letter in animal]
        """
        for letter in animal:
            if letter in correct_guesses:
                #print("Yes!")
                status.append(letter)
            else:
                #print("No!")
                status.append("-")
                """
        print(' '.join('{}'.format(*i) for i in (status)))

        # if all of the letters in the animal are in the guess letter list, break and congratulate the user
        if "-" not in status:
            print("You win!")
            index = 100

        # if the sentry variable is bigger or equal to the guesses, break and console the loser
        elif index > max_guesses:
            print("You lose!")
            index = 100

def main():
    if input("\nWant to guess an animal (y/n)? ") == "y":
        animal_guess()

main()