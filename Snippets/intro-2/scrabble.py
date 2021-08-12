rules = {}
for line in open('scrabble_letters.txt'):
    points, letter = line.split(' ')
    rules[letter.rstrip('\n')] = points

# prompt for english
test_word = input('Word: ').upper()

while test_word:
    # translate
    word_value = 0
    for letter in test_word:
        word_value += int(rules[letter])
    print(word_value, "points")

    # reprompt
    test_word = input('Word: ').upper()
