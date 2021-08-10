dictionary = {}
for line in open('dictionary.txt'):
    english, aboriginal = line.split(',')
    dictionary[english] = aboriginal

# prompt for english
english_sentence = input('English: ')

while english_sentence:
    # translate
    translation = ""
    for word in english_sentence.split():
        translation += dictionary[word].rstrip('\n') + ' '
    print(translation.rstrip(' '))

    # reprompt
    english_sentence = input('English: ')
