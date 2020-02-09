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
    job_rates[key].append(rate)

#Write the dictionary to a file
w = csv.writer(open("job_rates.csv", "w"))
for key, val in job_rates.items():
    w.writerow([key, val])

