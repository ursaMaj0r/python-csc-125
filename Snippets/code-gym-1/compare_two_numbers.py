# prompt
number = int(input("Enter a number: "))
anotherOne = int(input("Enter another number: "))

# response
if number > anotherOne:
    print("{0} is greater than {1}.".format(number, anotherOne))
else:
    print("{0} is less than or equal to {1}.".format(number, anotherOne))
