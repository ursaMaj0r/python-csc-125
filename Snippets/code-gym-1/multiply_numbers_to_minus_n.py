# input
input_number = int(input("Enter a negative number: "))
product = 1
# response
for i in range(-1, input_number-1, -1):
    product *= i
print(product)
