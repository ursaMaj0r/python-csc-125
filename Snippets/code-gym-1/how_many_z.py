# input
input_word = input("Enter a word: ")
num_z = 0

# response
for letter in input_word:
    if letter == 'z':
        num_z += 1
print(num_z)
