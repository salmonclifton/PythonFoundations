#!/usr/bin/env python

#Read in the file and store in a list
#Read the file into a list
f = open("./land_time_forgot.txt")
full_lines = f.readlines()

#Convert the list of book lines into a list of the words (hint: use string.split(), a for loop and list.extend \
# (Links to an external site.) OR string.split, two for loops and list.append)
word_list = []
sentences = (full_lines)

for sentence in sentences:
    sentence = sentence.strip()
    #Added for loop with continue to get rid of "" resulting from blank lines after stripping
    if sentence == "":
        continue
    words = sentence.split(" ")
    word_list.extend(words)

# Print a sentence with the total amount of words
print("Total number of words: {}".format(len(word_list)))

# Reopen file
f = open("./land_time_forgot.txt")

# Get the first line
first_line = f.readline()

# Get the project title and author
first_split = first_line.split(", by ")
project_title = first_split[0]
author = first_split[1].strip()

# Get the project and title
second_split = project_title.split("'s ")
project = second_split[0]
title = second_split[1]

# Print the author, title, and project
print("Author: {}\nTitle: {}\n{}".format(author, title, project))

"""

# Stretch goal
word_count = {}

# Count word frequencies
for word in list_of_words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print("Word that appears most frequently: " + max(word_count))
#!/usr/bin/env python
f = open("./land_time_forgot.txt")

list_of_words = []
# Convert the list of book lines into a list of the words
for line in f:
    line = line.strip()
    list_of_words.extend(line.split(" "))

# Print a sentence with the total amount of words
print("Total number of words: {}".format(len(list_of_words)))

# Reopen file
f = open("./land_time_forgot.txt")

# Get the first line
first_line = f.readline()

# Get the project title and author
first_split = first_line.split(", by ")
project_title = first_split[0]
author = first_split[1].strip()

# Get the project and title
second_split = project_title.split("'s ")
project = second_split[0]
title = second_split[1]

# Print the author, title, and project
print("{} {} {}".format(author, title, project))

# Stretch goal
word_count = {}

# Count word frequencies
for word in list_of_words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

# Print result
print("Word that appears most frequently: " + max(word_count))
"""

#Print a sentence using format with the total number of words


#Use split to get the project_title and author from the first line of your book lines list (hint: what do you have to split on?)


#The first line of the book is: Project Gutenberg's The Land That Time Forgot, by Edgar Rice Burroughs
#project_title is : Project Gutenberg's The Land That Time Forgot
#author is : Edgar Rice Burroughs
#Use split to get the project and title from project_title (hint: use split to remove the preposition)
#project is : Project Gutenberg
#title is : The Land That Time Forgot


#Print the author, then the title, followed by the project using format.