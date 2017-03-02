import time

start_time = time.time()
dictionary = {}
total_words = 0

with open('words.txt', 'rb') as words:
    for line in words:
        try:
            newWord = next(words).rstrip(' \t\r\n\0')  # Reads in the word, strips terminating character.
            letterKey = str(sorted(newWord))           # Creates a letter-sorted version of
            total_words += 1                           # the word to use as a dictionary key.

            if letterKey in dictionary:
                dictionary[letterKey].append(newWord)  # Adds unsorted word as another value
                                                       # for the sorted key.
            else:
                dictionary.setdefault(letterKey, []).append(newWord)  # Creates new entry in the dictionary.
        except StopIteration:
            pass


anagram_count = 0

for key in dictionary:
    if len(dictionary[key]) > 1:  # If the key has more than one entry, it
        print dictionary[key]  # gets printed.
        anagram_count += 1

print 'The program found', anagram_count, 'anagrams in', total_words, 'words.'
print "The program took", time.time() - start_time, " seconds to run."
