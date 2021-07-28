guess = input('Guess: ')
guesses = set()

while guess != "":
    # check if in set
    if guess not in guesses:
        print("Hit {}".format(guess))
        guesses.add(guess)
    else:
        print("You've chosen that square already")

    # reprompt
    guess = input('Guess: ')
