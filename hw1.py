"""
This solution prompts the user with three questions and stores
each answer in a variable.
A function is called passing it the three variables and the function
outputs the three responses in a sentence using string format.
"""
#Prompt the user with question 1 and store in the variable.
feline = input("What is your favorite feline? ")

#Prompt the user with question 2 and store in the variable.
canine = input("What is your favorite canine? ")

#Prompt the user with question 3 and store in the variable.
weather = input("What is your favorite weather condition? ")

#Create a function to form and output the sentence using the
# three parameters passed to it.
def sentence_maker(p1,p2,p3):
    print("\nTomorrow it will be raining {}s and {}s with "\
          "intermittent periods of {}.".format(p1, p2, p3))

#Call the function passing it the three user inputs as parameters.
sentence_maker(feline, canine, weather)

