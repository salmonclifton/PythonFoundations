
#Read the file into a list
f = open("./land_time_forgot.txt")
infile = f.readlines()

#Calculate the total number of lines in the file
line_count = len(infile)

#Calculate the lines that are in 1/3rd of the file
one_third = line_count//3
print("One third of the lines = ", one_third)

#Store the middle third of the book's lines in a list (hint: use list slicing)
start_line = one_third +1
end_line = one_third * 2
print("Start of middle third = ", start_line)
print("End of middle third = ", end_line)
middle_third = infile[start_line:end_line]

#Print the number of lines in the file and the number of lines in the middle third of the book
print("Line count = ", line_count)
print(len(middle_third))

#Print the line that is 1/3rd of the way through the book and the line that is 2/3 of the way through the book
first_third_line = infile[start_line]
second_third_line = infile[end_line + 1]
print("Line that is a third of the way through: ", first_third_line)
print("Line that is two thirds of the way through: ", second_third_line)

#Write the lines you printed above to a file
two_lines = first_third_line + second_third_line
print(two_lines)
with open('output.txt', 'w') as f:
    f.write(two_lines)
    # with open('output.txt', 'a') as o:
    # o.write(one_third_print)
    # o.write(two_third_print)