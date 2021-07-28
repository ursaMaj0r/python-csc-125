fixed = ""

with open('letter.txt') as f:
    for line in f:
        if not line.startswith("WOOF!"):
            fixed += line

with open('fixed.txt', 'w') as f:
    f.write(fixed)
