# create string and dictionary
lines = ""
occurrences = {}

# prompt for lines
line = input("Enter line: ")
while line:
    lines += line + " "
    line = input("Enter line: ")

# iterate through each color and store count
for word in set(lines.split()):
    occurrences[word] = lines.split().count(word)

# print results
for word in sorted(occurrences):
    print(word, occurrences[word])
