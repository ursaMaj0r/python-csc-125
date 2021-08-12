import collections
words_upper = []

f = open('novel.txt').read()
words = f.split()
for word in words:
  if word[0].isupper():
    words_upper.append(word)
top_three_words = {}
top_three_words = collections.Counter(words_upper).most_common(3)

print("{1} {0}".format(top_three_words[0][0],top_three_words[0][1]))
print("{1} {0}".format(top_three_words[1][0],top_three_words[1][1]))
print("{1} {0}".format(top_three_words[2][0],top_three_words[2][1]))