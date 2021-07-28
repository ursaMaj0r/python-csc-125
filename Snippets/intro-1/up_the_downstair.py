# input
input_steps = int(input("How many steps? "))
step = 1

# reponse
print("__")
while step < input_steps:
    print(" "*2*step + "|_")
    step += 1
print("_"*2*step + "|")
