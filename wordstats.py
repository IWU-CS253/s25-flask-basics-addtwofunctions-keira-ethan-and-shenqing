def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg

def word_count(user_string):
    words = user_string.split()
    return len(words)

def character_count(user_string):
    char_total = 0
    words = user_string.split()
    for word in words:
        char_total += len(word)
    return char_total

def num_letters(user_string):
    letter_count = {}
    words = user_string.split()
    com_let = ''
    highest_count = 0
    for word in words:
        for char in word:
            if letter_count.get(char) is None:
                letter_count[char] = 1
            else:
                letter_count[char] += 1
    for key in letter_count:
        if letter_count[key] > highest_count:
            com_let = key
            highest_count = letter_count[key]
    return com_let