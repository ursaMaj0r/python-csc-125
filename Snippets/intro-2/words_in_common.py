# open files
english_words = set((open('english.txt').read()).split())
french_words = set((open('french.txt').read()).split())
# find intersection
intersection = english_words & french_words

for word in intersection:
    print(word)
