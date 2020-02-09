#!/usr/bin/env python

"""
Assignment 05 - Word Counts
Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
Calculate the word count for each word. (hint: see the section "Counting with Dictionaries")
Calculate the word with the maximum count (hint: use max (Links to an external site.))
Get the minimum word count (hint: use values (Links to an external site.))
Store all of the words that have the minimum word count in a list (hint: use a for loop and items (Links to an external site.))
Print a sentence including the minimum word count and the number of words with that count
Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
"""

#Read in a file, parse the lines and create a list of words from the lines
f = open("./land_time_forgot.txt")
lines = f.readlines()
word_list = []
for line in lines:
    line = line.strip()
    # Added for loop with continue to get rid of "" resulting from blank lines after stripping
    if line == "":
        continue
    words = line.split(" ")
    word_list.extend(words)

#Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
total_words = len(word_list)
unique_word_count = len(set(word_list))
print("The total number of words is {} and the number of unique words is {}".format(total_words, unique_word_count))

#Calculate the word count for each word.
word_counts = {}
for i in word_list:
    if i in word_counts:
        word_counts[i] = word_counts[i] + 1
    else:
        word_counts[i] = 1

#Calculate the word with the maximum count
max_count = max(word_counts.values())

#make dict.values() into a list
count_list = list(word_counts.values())

#Use the list index method to find the index of the maximum value and store it as max_index
max_index = count_list.index(max_count)

#Make dict.keys() into a list
word_list = list(word_counts.keys())

#Use the max_index to get the key at that index
frequent_word = word_list[max_index]

#Print a sentence using format that outputs the most common word and the number of occurences
#Add thousands separator to max_count
max_count = f'{max_count:,}'
print("The word that appears the most times in the book is \"{}\" and it occurs {} times.".format(frequent_word, max_count))

#Get the minimum word count (hint: use values)
min_count = min(word_counts.values())

#Store all of the words that have the minimum word count in a list (hint: use a for loop and items)
min_list = []
for k, v in word_counts.items():
    if v == 1:
        min_list.append(k)

#Print a sentence including the minimum word count and the number of words with that count
minimal_words_count = len(min_list)
print("The mimimum word count is equal to {} and {} words occur at that minimum frequency.".format(min_count, minimal_words_count))

#Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
pct_unique = minimal_words_count/total_words*100
print("The percentage of words that are unique in the book is {:.1f}%.".format(pct_unique))
