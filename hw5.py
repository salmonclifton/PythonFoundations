


#Read in a file, parse the lines and create a list of words from the lines
f = open("./land_time_forgot.txt")

infile = f.readlines()

for line in open("./rose_winners.txt"):
...     line = line.strip()
...     parts = line.split(" - ")
...     print(parts)

for line in open("./rose_winners.txt"):
...     line = line.strip()
...     name, year = line.split(" - ")
...     names.append(name)
...     years.append(year)


#Calculate the word counts
#Create an empty dictionary
name_counts = {}

#Create a for loop that iterates through the names list
#Using the name as the key, increment the count of that name in the dictionary
for x in names:
    if x in name_counts:
        name_counts[x] = name_counts[x] + 1
    else:
        name_counts[x] = 1

#Get the word with the maximum count
#Find the most frequent value (hint: use max) and print
max_count = (max(name_counts.values()))
print("Maximum count is: ", max_count)

#Get the minimum count and a list of words with that count
#Find the most frequent value (hint: use min) and print
min_count = (min(name_counts.values()))
print("Miniimum count is: ", min_count)


#Calculate the percentage of words that are unique in the book and print it
