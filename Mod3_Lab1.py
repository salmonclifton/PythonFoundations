#!/usr/bin/env python

"""For the following number list:

print out all the even numbers and their index in the list
don't print any numbers that come after the number 237 in the list """
numbers = [
951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
743, 527
]

#pseudocode

# use a for loop and enumerate to iterate through the numbers
for index, number in enumerate(numbers):
    # if the number is 237 then break the loop
    if number ==  237:
        break
    # if the number is even print the number and index
    if (number%2) == 0:
        print(index, number)

print ("\n")

found_index = numbers.index(237)
print(found_index, "is the index of 237")
print("\n")
for i in range(0, found_index):
    print(numbers[i])
numbers.sort()
length = len(numbers)
print("Minimum is ", numbers[0], "Maximum is ", numbers[found_index])

