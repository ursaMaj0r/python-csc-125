favorite_colors = {}

line = input("Name and colour: ")
while line:
    name, colour = line.split()
    favorite_colors[name] = colour
    line = input('Name and colour: ')

for name, colour in favorite_colors.items():
    print(name, colour)
