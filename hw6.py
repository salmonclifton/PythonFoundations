#!/usr/bin/env python

"""
Taking what we learned about functions, create a python script that will calculate the cost of pizza for movie night.

Get user input for the following:
Number of people who want pizza
Average number of slices per person
You can store each of these as a single integer, or use a dictionary to map names to slices, up to you
Create the following static (unchanging) variables:
Pizza cost = $15.99
Total slices = 8
Tax rate of 10.1%
Tip rate of 18%
Delivery fee of $3.99
Write functions to calculate:
How many pizzas to order based on number of people and average number of slices
Total pizza cost
Cost per person
Stretch goals:

Add an option to calculate the tip by person or by slice
Update your pizza script to read in a file (txt or csv) of how many slices of pizza different people want (ex: Daniel, 3) and calculate the cost for each person individually
How many slices are leftover?"""



#Get input from user for number of people and average slices per person
def userInput():
   while True:
        try:
            num_people = int(input("Enter the number of people having pizza: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        else:
            break

   while True:
       try:
           num_slices = int(input("Enter the average number of slices per person: "))
       except ValueError:
           print("Please enter a whole number.")
           continue
       else:
           return num_people, num_slices

#Calculate how many pizzas to order based on number of people and average number of slices
#Calculate remainder number of slices
def pizzaCalc(people_count, average_slices):
    pizza_count = people_count * average_slices // total_slices
    extra_slices = people_count * average_slices % total_slices
    return pizza_count, extra_slices

#Calculate total pizza cost
def costCalc(pizza_count):
    cost = pizza_count * pizza_cost + delivery_fee
    tax = cost * tax_rate
    tip = cost * tip_rate
    total = cost + tax + tip
    return cost, tax, tip, total

#Calculate cost per person
def perPersonCost(cost, number):
    cost_each = cost / number
    return cost_each

############
#main
############

#Set static variables
pizza_cost = 15.99
total_slices = 8
tax_rate = .101
tip_rate = .18
delivery_fee = 3.99

#Initialize variables
people = 0
slices_per = 0

people, slices_per = userInput()
print("people = {}\nslices per person = {}".format(people, slices_per))
pizza_total, remainder_slices = pizzaCalc(people, slices_per)
print("number of pizzas = {}\nextra slices = {}".format(pizza_total, remainder_slices))
total_cost, total_tax, total_tip, grand_total = costCalc(pizza_total)
print("cost of pizzas = {}\ntax = {}\ntip = {}\ngrand total = {}".format(total_cost, total_tax, total_tip, grand_total))
per_person = perPersonCost(grand_total, people)
print("Cost per person = {}".format(per_person))