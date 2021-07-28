line = input('Line: ')
biagrams = []

# take input
while line:
    line = line.lower()
    data = line.split()
    # add biagrams to dictionary
    for word in data[:-1]:
        position = data.index(word)
        biagrams.append((data[position] + " " + data[position+1]))
    line = input('Line: ')

# find unique
unique_biagrams = set(biagrams)

for biagram in unique_biagrams:
    if biagrams.count(biagram) > 1:
        print("{}: {}".format(biagram, biagrams.count(biagram)))

print("EOF")
