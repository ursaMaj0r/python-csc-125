# prompt
number = input("Enter a number: ")

# response
if int(number) > 0:
    print("{0} is positive.".format(number))
elif int(number) < 0:
    print("{0} is negative.".format(number))
else:
    print("You entered zero.")
