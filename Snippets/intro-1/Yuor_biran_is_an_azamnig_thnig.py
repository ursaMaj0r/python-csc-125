# input
input_raw = input("Enter words: ")
input_words = input_raw.split()

# tests
if (set(input_words[0]) == set(input_words[-1])) and (set(input_words[0][0]) == set(input_words[-1][0])) and (set(input_words[0][-1]) == set(input_words[-1][-1])) and (len(input_words[0]) == len(input_words[-1])):
    print("Super Anagram!")
else:
    print("Huh?")
