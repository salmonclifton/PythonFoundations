#!/usr/bin/env python

# get user input for a url and return it
def get_user_input():
    pass

# get a tag from a url and return the result set of tags
def pull_out_tag(url, tag):
    pass

# format the tag information
def meaningful_format(results):
    pass

# write the data to a file
def write_to_file(filename, output):
    pass

if __name__ == "__main__":
    # for testing - in reality get user input
    #url ="https://en.wikipedia.org/wiki/List_of_cities_in_Canada"
    # real code
    # url = get_user_input()
    url = input("Enter the full url of the page you would like to scrape data from: ")
    tag ="a"
    # call the pull_out_tag function to use soup to find all of the tags
    contents = pull_out_tag(url, tag)

    # call the meaningful format function

    # call the write to file function
