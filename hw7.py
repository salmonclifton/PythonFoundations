#!/usr/bin/env python
import csv
import requests
import lxml
from bs4 import BeautifulSoup

# get user input for a url and return it
def get_user_input():
    url = input("Enter the full url of the page you would like to scrape data from: ")
    tag = input("Enter the tag from which you would like to scrape data from: ")
    return url, tag

# get a tag from a url and return the result set of tags
def pull_out_tag(url, tag):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')
    if tag == "li":
        results = soup.find_all(tag, "gallerybox")
        return results
    elif tag == "div":
        results = soup.find_all(tag)
        return results

# format the tag information
"""
div - Generally used for spacing on the page and don't contain text or useful attributes. 
Meaningful for div tags might be counting the number of divs that are on the page.
li - Most of these have the `class=gallerybox` that makes them a container for the crater 
information that we're looking for on the page, but they don't contain text or useful attributes.  
Meaningful for li tags might be counting the number of divs that are on the page.
a - Have a href attribute.  Some a tags on this page contain img tags and some contain text. 
Meaningful for a tags might be displaying the href attribute and checking if it has text or title attribute.
img - Have a src attribute and a width and height attribute.  Meaningful for img tags might be displaying 
the src attribute or counting how many images have the same width or height.
"""


def meaningful_format(tag, tag_lines):
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

    elif tag == "div":
        name = "div_count_csv.txt"  # ./
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
    #url ="https://en.wikipedia.org/wiki/List_of_cities_in_Canada"
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
"""
    tag_list = []
    for tags in contents:
        if tags is not None:
            tags = tags.string
            tag_list.append(tags)
            print(tags)
"""



    # call the write to file function
"""
"""