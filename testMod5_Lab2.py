#!/usr/bin/env python
f = open("./land_time_forgot.txt")

list_of_words = []
# Convert the list of book lines into a list of the words
for line in f:
    line = line.strip()
    list_of_words.extend(line.split(" "))

print(list_of_words)
# Print a sentence with the total amount of words
print("Total number of words: {}".format(len(list_of_words)))
