with open('input.txt') as f:
    line_number = 1
    for line in f:
        line = line.lower()
        if (line.count('a') >= 3) and (line.count('r') >= 2) and ('d' in line) and ('v' in line) and ('k' in line):
            print("Aardvark on line {}".format(line_number))
        line_number = line_number + 1
