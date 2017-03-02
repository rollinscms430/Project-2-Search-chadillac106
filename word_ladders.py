import time


start_time = time.time()
total_words = 0
start_word = 'snakes'
end_word = 'brains'

dictionary = {}
with open('words.txt', 'rb') as w:
    for line in w:
        try:
            new_word = line.rstrip(' \t\r\n\0')  # Reads in the word, strips terminating character.

            if len(new_word) == len(end_word):
                for letter in range(len(new_word)):
                    omit = new_word[:letter] + ' ' + new_word[letter + 1:]
                    if omit in dictionary:
                        dictionary[omit].append(new_word)
                    else:
                        dictionary.setdefault(omit, []).append(new_word)
        except StopIteration:
            pass

test_word = start_word
to_visit = [test_word]
visited = {}

word_found = 'No'

tree = []

to_visit.append(start_word)

while len(to_visit) > 0 and word_found == 'No':

    word = str(to_visit.pop())
    visited[word] = word

    if word != end_word:
        for letters in range(len(word)):
            if word[letters] != end_word[letters]:
                index = word[:letters] + ' ' + word[letters + 1:]
            for entries in dictionary[index]:
                if entries == end_word and entries not in tree and word not in tree:
                    word_found ='Yes'
                    tree.append(word)
                    tree.append(entries)
                    break
                elif entries not in visited:
                    to_visit.append(dictionary[index][dictionary[index].index(entries)])
                    if word not in tree:
                        tree.append(word)

    else:
        print word
        word_found = 'Yes'
        break


print 'The program took', time.time() - start_time, 'seconds to reach goal word:', end_word
print 'It took', len(tree), 'moves to reach the goal word:', end_word
print tree