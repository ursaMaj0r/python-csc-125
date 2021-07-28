# create list
cars = []

# prompt for cars
car = input("Car: ")
while car:
    cars.append(car)
    car = input("Car: ")

# iterate through each color and print count
for color in set(cars):
    print("Cars that are {0}: {1}".format(color, cars.count(color)))
