#!/usr/bin/env python

""" Wrap all of the following in a single function definition, or multiple functions, then invoke the function
(no parameters are needed). See Module 1 "Scripts, Statements and Functions" for a refresher.
Gather the following user inputs and store each item as a variable:
Purchaser name
Purchaser address
Purchaser phone number (entered as 503-555-1211)
Car Make and Model
Purchase Price
After the user inputs the above information, your program should add the following values to the sale price:
Sales tax as a percent of sale price (10.1% combined rate for ZIP 98101)
Licensing fee
Dealer prep fee
Calculate total cost (as a float)
Assign the transaction a unique ID composed of the last four letters of the purchaser's last name and their
area code, separated by an underscore
Print out the information to the screen, with the same line breaks as shown in the example   """

#Set fixed fee variables
tax_rate = 0.101
licensing_fee = 498.89
dealer_fee = 4999.99

#Create function to gather user input and return the values
def customer_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    street_address = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    phone = input("Enter your phone number as 555-555-1234: ")
    car_make = input("Enter the make of the car: ")
    car_model = input("Enter the model of the car: ")
    sales_price = float(input("Enter purchase price in dollars as 55000.99: "))
    taxes = (tax_rate * sales_price)
    return(first_name, last_name, phone, car_make, car_model, sales_price, taxes )

#Create function to calculate the total cost
def grand_total(sales_price, taxes, licensing_fee, dealer_fee):
    total_price = sales_price + taxes + licensing_fee + dealer_fee
    return total_price

#Create a function to create and return a unique ID number
def ID_creator(last_name, phone):
    unique_ID = last_name[-4:] + "_" + phone[:3]
    unique_ID = unique_ID.upper()
    return unique_ID

#Create a function to format and print the final output.
# Use format to display commas to designate 1000's place and display two significant digits.
def printout(first_name, last_name, car_make, car_model, \
             sales_price, taxes, licensing_fee,  dealer_fee, total_price, unique_ID):
    sales_price = format(sales_price, ",.2f")
    taxes = format(taxes, ",.2f")
    licensing_fee = format(licensing_fee, ",.2f")
    dealer_fee = format(dealer_fee, ",.2f")
    total_price = format(total_price, ",.2f")
    print("\n\nHello {} {}! \n\nThank you for your purchase of a {} {}. Following is a breakdown of your total price:\
\n\nSales Price: ${} \n\nTax: ${} \n\nLicensing Fee: ${} \n\nDealer Prep Fee: ${}\
\n\nTotal Price: ${} \n\nYou have been assigned an ID number of {}. Please refer to this ID \
number if you have any questions.".format(first_name, last_name, car_make, car_model,\
                                    sales_price, taxes, licensing_fee,  dealer_fee, total_price, unique_ID))

#Main function that calls the various other functions
def main():
    #Collects and returns customer data including calculating taxes
    first_name, last_name, phone, car_make, car_model, sales_price, taxes = customer_data()
    #Calls function create unique ID and return it
    unique_ID = ID_creator(last_name, phone)
    #Calls function to calculate total dollar amount and return it
    total_price = grand_total(sales_price, taxes, licensing_fee, dealer_fee)
    #Calls function that formats and prints out the summary of the sale
    printout(first_name, last_name, car_make, car_model, sales_price, taxes, licensing_fee,\
         dealer_fee, total_price, unique_ID)

#Calls the main function. Single point of entry and exit.
main()
