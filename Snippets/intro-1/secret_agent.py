# input
input_text = input("Message? ")
first_letter = True
# response
for letter in range(0, len(input_text)-1):
    if first_letter == True:
        print(input_text[letter], end='')
        first_letter = False
    else:
        print(" {}".format(input_text[letter]), end='')
print()
