# input
input_currentFloor = int(input("Current floor: "))
input_destinationFloor = int(input("Destination floor: "))

# response
while input_currentFloor <= input_destinationFloor:
    print("Level {}".format(input_currentFloor))
    input_currentFloor += 1
