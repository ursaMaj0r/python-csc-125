line = input('Line: ')
monolingual_people = set()

while line:
    data = line.split()
    language = data[0]
    if language == "English":
        for speaker in data[1:]:
            monolingual_people.add(speaker)
    else:
        for speaker in data[1:]:
            if speaker in monolingual_people:
                monolingual_people.remove(speaker)
    line = input('Line: ')


if len(monolingual_people) == 0:
    print("Everyone is multilingual!")
else:
    for person in monolingual_people:
        print("{} is monolingual.".format(person))
