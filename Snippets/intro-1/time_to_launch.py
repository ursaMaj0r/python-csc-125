# input
countdown = int(input("Time to launch: "))

# response
print("Counting down ...")
while countdown > 0:
    print("{} ...".format(countdown))
    countdown -= 1
print("Lift Off!")
