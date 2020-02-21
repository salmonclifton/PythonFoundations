#!/usr/bin/env python

"""
Program accepts user input for a url and tag that the user wants to scrape data from and save to a txt file.
It is designed currently to only work with https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon.
The only tags that it will currently handle are li and div.
Entering the li tag will scrape the crater name and crater diameter data.
Entering the div tag will count the number of times the div tag occurs on the page.
"""

import csv
import requests
import lxml
from bs4 import BeautifulSoup



# get user input for a url and return it
def get_user_input():
    url = ""
    tag = ""
    # set valid inputs
    valid_tags = ("li", "div")
    valid_urls = ("https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon")
    print(url, tag)
    while url != valid_urls:
        url = input("Enter the full url of the page you would like to scrape data from: ")
        if url != valid_urls:
            print("Only allows https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon in this version.\n")
    while tag not in valid_tags:
        tag = input("Enter the tag from which you would like to scrape data from: ")
        if tag not in valid_tags:
            print("Only li and div tags are handled in this release!\n")
    return url, tag

# get a tag from a url and return the result set of tags
def pull_out_tag(url, tag):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')

    # for li tag will return all li tags that have the class: gallerybox
    if tag == "li":
        results = soup.find_all(tag, "gallerybox")
        return results
    # for div tag will return all div tags
    elif tag == "div":
        results = soup.find_all(tag)
        return results

# format the tag information
def meaningful_format(tag, tag_lines):
    # for li tags it will assign a filename for file output, create a dict with the crater
    # name and diameter. Returns dict and filename.
    if tag == "li":
        name = "crater_diam.txt" #./
        crater_diam_dict = {"Crater": "Diameter"}

        for line in tag_lines:
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
                crater_diam_dict[crater] = diameter
        return crater_diam_dict, name
    # for div tags it will assign a filename for file output, create a dict with the count
    # of the div tags. Returns dict and filename.
    elif tag == "div":
        name = "div_count.txt"  # ./
        div_count_dict = {"Tag": "Count"}
        count = 0

        for line in tag_lines:
            div_tag = line.find("div", "gallerytext")
            if div_tag is not None:
                count += 1
        div_count_dict[tag] = count
        return div_count_dict, name
    else:
        pass

# write the data to a file
def write_to_file(output, filename):
    # print dictionary key/value to a file as two columns separated by a comma
    with open(filename, "w") as outfile:
        for crater, diameter in output.items():
            outfile.writelines("{}, {}".format(crater, diameter))
            outfile.write("\n")

if __name__ == "__main__":
    # for testing - in reality get user input
    #url ="https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon"
    #tag ="a"

    # real code
    # call get_user_input function to get the url and tag
    url, tag = get_user_input()


    # call the pull_out_tag function to use soup to find all of the tags
    contents = pull_out_tag(url, tag)

    # call the meaningful format function
    result_dict, name = meaningful_format(tag, contents)

    # call the write to file function
    write_to_file(result_dict, name)

    # Open newly created txt file and print
    text_file = open(name, "r")
    print(text_file.read())
    text_file.close()
