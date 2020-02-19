#!/usr/bin/env python

import requests
import lxml
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon (Links to an external site.)"
# use requests to get the url
# get the content from the response

# parse the content with soup
soup = BeautifulSoup(content, 'lxml')

# look at the web page source and find out the container for the information we want
# each crater is stored in a li that has the class 'gallerybox'
# tell soup to get the li gallerybox

# crater name and crater diameter are inside a div that has the class 'gallerytext'
# tell soup to get the div gallerytext from div gallerybox

# crater name the string of an anchor tag that is inside a div that has a class 'gallerytext'
# tell soup to get the anchor tag from div gallerytext

# crater diameter is the string of a span tag that is inside a div that has class 'gallerytext'
# tell soup to get the span tag from div gallerytext

# crater thumbnail is inside of the div that has the class 'thumb'
# tell soup to get the div thumb from div gallerybox

# crater thumbnail source is the 'src' key inside the 'attrs' dictionary of the img tag from div thumb
# tell soup to get the img tag from div thumb

#store name = diameter or name = thumbnail in a dictionary

# print dictionary key/value to a file as two columns separated by a comma