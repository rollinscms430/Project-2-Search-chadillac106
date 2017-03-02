import time

# Initializing board
board_letters = ['u', 'n', 't', 'h', 'g', 'a', 'e', 's', 's', 'r', 't', 'r', 'h', 'm', 'i', 'a']
board = []
index = 0
board_size = 4
for row in range(board_size):
    board.append([])
    for column in range(board_size):
        board[row].append(board_letters[index])
        index += 1

num_rows = len(board)
num_cols = len(board[0])

# Create entries in the dictionary
dictionary = {}

with open('words.txt', 'rb') as w:
    for line in w:
        new_word = line.rstrip(' \t\r\n\0')
        for i in range(2, len(new_word) + 1):   # Iterates through the words, beginning with the first two characters
                                            # and ending with all the characters.
            dictionary.setdefault(new_word[:i], []).append(new_word)  # Appending the words for each
            # progression of the string ex. values 'progress, progression' for keys 'pr', 'pro', 'prog'.

results = {}


def extended_search(test_val, current_location):
    if test_val in dictionary:
        for val in dictionary[test_val]:
            if test_val == val:
                yield (test_val, current_location)
    for (around_x, around_y) in surrounding(current_location[-1]):
        if (around_x, around_y) not in current_location:
            new_test_val = test_val + board[around_y][around_x]
            if new_test_val in dictionary:
                # Recurses to spell possible words if partial string is in dictionary
                for result in extended_search(new_test_val, current_location + ((around_x, around_y),)):
                    yield result

def surrounding((x, y)):   # Ignored warning, avoided by indexing in other function.
    for around_x in range(max(0, x - 1), min(x + 2, num_cols)):     # Avoids going out of bounds when searching by
                                                                    # confining maximum index using number of columns.
        for around_y in range(max(0, y - 1), min(y + 2, num_rows)): # Avoids going out of bounds when searching by
            yield (around_x, around_y)                              # confining using number of rows.
            # returns surrounding tile location

if __name__ == "__main__":
    start_time = time.time()
    for y, row in enumerate(board):  # Retrieving y via enumeration
        for x, letter in enumerate(row):  # Retrieving x and the letter at that tile via enumeration
            for result in extended_search(letter, ((x, y),)):
                if result not in results:
                    results.setdefault(result[0], []).append(result[1])  # Appends the words to results dictionary,
                    # the tile locations used to spell them are the values.

    resulting_keys = []
    for key in results:
        resulting_keys.append(key)
    print sorted(resulting_keys)  # Prints sorted list of possible words.
    print 'The search of the boggle board yielded', len(
        results.keys()), 'words in', time.time() - start_time, 'seconds.'
