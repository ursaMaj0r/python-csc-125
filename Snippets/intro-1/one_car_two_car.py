# input
input_raw = input("Cars: ")
cars = input_raw.split()
red = 0
blue = 0

# reponse
for car in cars:
    if car == "red":
        red += 1
    elif car == "blue":
        blue += 1
print("red: {}".format(red))
print("blue: {}".format(blue))
