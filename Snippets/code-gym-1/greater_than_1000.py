# prompt
number = input("Enter a number: ")

# response
if int(number) > 1000:
    print("{0} is greater than 1000.".format(number))
elif int(number) < 1000:
    print("{0} is less than 1000.".format(number))
else:
    print("You entered 1000.")
