s1 = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because \
he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about \
in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent \
than man — for precisely the same reasons."

s2 = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a \
double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was \
this: So long and thanks for all the fish."

#Number of unique words in each sentence
words1 = (set(s1.split(" ")))
print("Number of unique words in S1: ", len(words1))
words2 = (set(s2.split(" ")))
print("Number of unique words in S1: ", len(words2))

#The number of words that only appear in both sentences
shared_words = words1.intersection(words2)
print("The number of words that only appear in both sentences: ", (len(shared_words)))

#The number of words that are contained in either one sentence or the other, but not in both
unshared_words= words1^words2
print("The number of words that are contained in either one sentence or the other: ", len(unshared_words))
