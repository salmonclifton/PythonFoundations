#Create the following name list and add in at least five female names (with repeats)
names = ['mark', 'henry', 'matthew', 'paul', 'robert',
'joseph', 'carl', 'luke', 'mark', 'robert', 'joseph', 'carl',
'michael', 'mark', 'henry', 'matthew']

names.extend(['mary', 'ellen', 'mary', 'amy', 'susan', 'michelle', 'sarah'])

#Create an empty dictionary
name_counts = {}

#Create a for loop that iterates through the names list
#Using the name as the key, increment the count of that name in the dictionary
for x in names:
    if x in name_counts:
        name_counts[x] = name_counts[x] + 1
    else:
        name_counts[x] = 1

#Output names and counts
print(name_counts)

#Find the most frequent value (hint: use max) and print
max_count = (max(name_counts.values()))
print("Maximum count is: ", max_count)

#make dict.values() into a list
name_list = list(name_counts.values())

#Use the list index method to find the index of the maximum value and store it as max_index
max_index = name_list.index(max_count)

#Make dict.keys() into a list
count_list = list(name_counts.keys())

#Use the max_index to get the key at that index
frequent_name = count_list[max_index]
print(frequent_name.capitalize())