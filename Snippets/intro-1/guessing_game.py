# input
print('What is my favourite food?')
input_guess = input("Guess? ")

# response
while input_guess != 'electricity':
    print("Not even close.")
    input_guess = input("Guess? ")
print("You guessed it! Buzzzz")
