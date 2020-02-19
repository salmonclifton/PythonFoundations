#!/usr/bin/env python

import csv
import requests
import lxml
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon"

# use requests to get the url
response = requests.get(url)

# get the content from the response
content = response.content

# parse the content with soup
soup = BeautifulSoup(content, 'lxml')

# look at the web page source and find out the container for the information we want
# each crater is stored in a li that has the class 'gallerybox'
# tell soup to get the li gallerybox
gb_lines = soup.find_all("li", "gallerybox")

#For loop to get crater name from anchor tag and diameter from span tag within div galerytext within li gallerybox and
#add each pair to the dictionary

#Create dictionary by populating headers
crater_dict = {"Crater":"Diameter"}

# crater name and crater diameter are inside a div that has the class 'gallerytext'
# tell soup to get the div gallerytext from li gallerybox
for line in gb_lines:
    div_tag = line.find("div", "gallerytext")
    if div_tag is not None:
        # crater name the string of an anchor tag that is inside a div that has a class 'gallerytext'
        # tell soup to get the anchor tag from div gallerytext
        crater = div_tag.find("a")
        crater = crater.string

        # crater diameter is the string of a span tag that is inside a div that has class 'gallerytext'
        # tell soup to get the span tag from div gallerytext
        diameter = div_tag.find("span")
        diameter = diameter.string
        diameter = diameter.replace('(', '').replace(')', '')

        # store name = diameter in a dictionary
        crater_dict.update({crater: diameter})

# print dictionary key/value to a file as two columns separated by a comma
with open("crater_csv.csv", "w") as outfile:
    for crater, diameter in crater_dict.items():
        crater = crater.replace(':', '')
        outfile.writelines("{}, {}".format(crater, diameter))
        outfile.write("\n")

# Open newly created csv file and print
fh = open("./crater_csv.csv")
reader = csv.reader(fh)
for row in reader:
    print(row)