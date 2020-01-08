#Prompt the user with question 1 and store in the variable
answer1 = input("Question1?")

#Prompt the user with question 2 and store in the variable
answer2 = input("Question2?")

#Prompt the user with question 3 and store in the variable
answer3 = input("Question3?")

#Create a function to create and output the sentence
def sentence_maker(p1,p2,p3):
    print("This is how it works {} {} {}".format(answer1 + answer2 + answer3))

sentence_maker(answer1, answer2, answer3)


