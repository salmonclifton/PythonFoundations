#!/usr/bin/env python

"""
Read in the CSV file using csv.reader
Store the header line in a variable using next (Links to an external site.)
Create a dictionary to store the list of 'Hourly Rate' by job title (hint: this is a dictionary where the value is
a list - seattle[job] = [rates].  You'll need to use key in dictionary or dictionary.get to see if the key exists in
each dictionary and create it if it does not, similar to counting with dictionaries.)
Write the dictionary to a file
"""

#Read in the CSV file using csv.reader
import csv
fh = open("./City_of_Seattle_Wage_Data.csv")
reader = csv.reader(fh)

#Store the header line in a variable using next
header = next(reader)

#Create a dictionary to store the list of 'Hourly Rate' by job title (hint: this is a dictionary where the value is
# a list - seattle[job] = [rates].  You'll need to use key in dictionary or dictionary.get to see if the key exists in
# each dictionary and create it if it does not, similar to counting with dictionaries.)

from collections import defaultdict
job_rates = defaultdict(list)
for dept, last, first, key, rate in reader:
    job_rates[key].append(float(rate))

#Write the dictionary to a file
w = csv.writer(open("job_rates.csv", "w"))
for key, val in job_rates.items():
    w.writerow([key, val])

"""
Stretch goals below
"""
#After your data structure is created, use a for loop to go over each job and calculate the average pay
#Print a sentence for each job saying how many people work that job and what the average pay is.
max_rate = 0
for key, val in job_rates.items():
    average = sum(val)/len(val)
    if len(val) > 1:
        print("There are {} {} employees and the average pay is ${:,.2f}".format(len(val), key, average))
    else:
        print("There is {} {} employee and the pay is ${:,.2f}".format(len(val), key, average))
    if average > max_rate:
        highest_avg_rate = average
        highest_paying = key

#Calculate the highest paying job
#print(job_rates.keys(job_rates.values()))
print("\nThe highest paying position is the {} position which pays an average of ${:,.2f}.".format(highest_paying, highest_avg_rate))