#Prompt the user with question 1 and store in the variable.
username = input("What is your username? ")

#Prompt the user with question 2 and store in the variable.
phone = input("Enter your phone number as 555-555-1212: ")

#Prompt the user with question 3 and store in the variable.
cheese = input("What is your favorite cheese? ")

#Prompt the user with question 4 and store in the variable as an int.
monthly_cost = input("How many dollars per month on average do you spend on your favorite cheese? ")
monthly_cost = int(monthly_cost)

#Calculate daily cost
daily_cost = monthly_cost/31

#Split and store the last 4 digits of the phone number
last_four_phone_number = phone.split("-")[-1]

#Store the first three letters of the username
first_three_username = username[0:4]

#Combine the last_four_phone_number with the first_three_username variable/
#to create account ID
account_ID = last_four_phone_number + first_three_username

#Replace the first letter of the account ID with a 'Z' and store as final account ID
account_ID = account_ID.replace(account_ID[0], "z", 1)

#Create a function to form and output the sentence using the
# three parameters passed to it.
def sentence_maker(p1,p2,p3):
    print("\n{}, do you really spend ${} per day on {}?".format(p1, p2, p3))

#Call the function passing it the three user inputs as parameters.
sentence_maker(account_ID, daily_cost, cheese)