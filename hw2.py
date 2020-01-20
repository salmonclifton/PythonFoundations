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
    total_price = (round(total_price, 2))
    return total_price

#Create a function to create and return a unique ID number
def ID_creator(last_name, phone):
    unique_ID = last_name[-4:] + "_" + phone[:3]
    unique_ID = unique_ID.upper()
    return unique_ID

#Create a function to format and print the final output
def printout(first_name, last_name, car_make, car_model, \
             sales_price, taxes, licensing_fee,  dealer_fee, total_price, unique_ID):
    sales_price = format(sales_price, ",.2f")
    taxes = format(taxes, ",.2f")
    licensing_fee = format(licensing_fee, ",.2f")
    dealer_fee = format(dealer_fee, ",.2f")
    total_price = format(total_price, ",.2f")
    print("\n\nHello {} {}! \n\nThank you for your purchase of a {} {}. Following is a breakdown of your total price:\
\n\nSales Price: ${} \n\nTax: ${} \n\nLicensing Fee: ${} \n\nDealer Prep Fee: ${}\
\n\nTotal Price: ${} \n\nYou have been assigned an ID number of {}. Please refer to this ID\
number if you have any questions.".format(first_name, last_name, car_make, car_model,\
                                    sales_price, taxes, licensing_fee,  dealer_fee, total_price, unique_ID))

#Main
first_name, last_name, phone, car_make, car_model, sales_price, taxes = customer_data()
unique_ID = ID_creator(last_name, phone)
total_price = grand_total(sales_price, taxes, licensing_fee, dealer_fee)
printout(first_name, last_name, car_make, car_model, sales_price, taxes, licensing_fee,\
         dealer_fee, total_price, unique_ID)
#print(first_name, last_name, phone, car_make, car_model,sales_price)

"""
customer_data(first_name, last_name, phone, car_make, car_model,sales_price)
print (first_name, last_name, phone, car_make, car_model, sales_price)
"""