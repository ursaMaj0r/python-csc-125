# prompt
letter = input("Enter a letter: ")
vowels = ["a", "e", "i", "o", "u"]

# response
if letter in vowels:
    print("{0} is a vowel.".format(letter))
else:
    print("{0} is a consonant.".format(letter))
