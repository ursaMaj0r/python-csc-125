# input
input_number_smaller = int(input("Enter the smaller number: "))
input_number_larger = int(input("Enter the larger number: "))
result = 0
# response
for i in range(input_number_smaller, input_number_larger+1):
    result += i**2
print(result)
