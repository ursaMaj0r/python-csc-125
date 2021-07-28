# input
input_word = input("Enter a word: ")
response = ""

# response
for letter in input_word:
    if letter == "e":
        response += "-"
    else:
        response += letter
print(response)
