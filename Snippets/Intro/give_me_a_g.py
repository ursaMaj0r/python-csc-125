# input
input_word = input("Cheer: ")

# response
for letter in input_word:
    print("Give me a {0}, {0}!".format(letter))
print("What does it spell?\n{0}".format(input_word.upper()))
