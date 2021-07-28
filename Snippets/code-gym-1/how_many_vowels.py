# input
input_word = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
num_vowels = 0

# response
for letter in input_word:
    if letter in vowels:
        num_vowels += 1
print(num_vowels)
