

#Update the code to create a function that turns the file into a list of lines
def list_create(file):
    with open(file) as file:
        lines = file.readlines()
    return lines

#Update the code to create a function that converts the list of book lines into a list of the words
def words_list_create(lines):
    word_list = []
    for line in lines:
        word_list.extend(line.strip().split(" "))
    return word_list

#Update the code to have a function that calculates the word count
def words_counter(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    return word_count



#print("The word that occurs most is '{}' with count {}".format(
#        max_word, word_count[max_word]))

#Update the code to have a function that calculates the minimum word count: takes  the word count dictionary and
#return the list of minimum count words
def mimimum_calculator(word_count):
    min_word_count = min(word_count.values())
    min_words = []
    for word, cnt in word_count.items():
        if cnt == min_word_count:
            min_words.append(word)
    return min_word_count, min_words

#Create a main section at the bottom of the code
#main
#Create a variable that stores the filename of the text file in the main section
filename = "./land_time_forgot.txt"
#Update the main section to call the function that turns the file into a list of lines (pass in the filename, store the
# output in a variable)
lines_list = list_create(filename)
#Update the main section to call the function that converts the list of book lines into a list (pass in the list of
# lines, store the output in a variable)
word_list = words_list_create(lines_list)
#Update the main section to : create a word set and print the sentence about unique words
word_set = set(word_list)
print("There are {} words in the book and {} of them are unique".format(len(word_list), len(word_set)))
#Update the main section to call the function that calculates the word count (pass in the list of words, store the
# results in a variable)
words_count = words_counter(word_list)
#Update the main section to find the word with the maximum count (hint: use max)
max_word = max(words_count, key=words_count.get)
#Update the main section to call the calculates the minimum word count (pass in the word count dictionary, store the
# results in a variable)
min_count, minimum_words = mimimum_calculator(words_count)
#Print a sentence with the minimum word count and the number of words with that count
print("The lowest word_count is {} and there are {}" + " words in the book with that word_count".format(min_count, len(minimum_words)))
