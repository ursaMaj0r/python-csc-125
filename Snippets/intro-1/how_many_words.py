# input
input_words = []
input_word = input("Word: ")

# reponse
while input_word != '':
    input_words.append(input_word)
    input_word = input("Word: ")
print("You know {} unique word(s)!".format(len(set(input_words))))
