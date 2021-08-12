# title:          proj01.py
# description:    CSC-125 Project 1: Caesar Cipher
# author:         jmalavasi
# date:           06242021
# version:        1.0
# ==============================================================================

# define variables
keep_going = True
alphabet = 'abcdefghijklmnopqrstuvwxyz'

while keep_going != False:
    # prompt for input
    input_choice = input("Would you like to (e)ncode, (d)ecode, or (q)uit?: ")

    # switch on input choice
    if input_choice == 'e':
        # prompt for message and rotation
        plain_text = input("What is the message?: ")
        rotation = int(input("Enter an rotation number (0-25): "))

        # encode string
        cipher_text = ""
        for char in plain_text:
            if char in alphabet:
                char_index = alphabet.index(char)
                cipher_text += alphabet[((alphabet.index(char)+rotation)) % 26]
            elif char == " ":
                cipher_text += " "
        print("Secret Message: " + cipher_text)
    elif input_choice == 'd':
        # prompt for encrypted message and secret word
        secret_text = input("What is the secret message?: ")
        secret_word = input("Enter a secret word: ")

        # find rotation
        rotation = 1
        decryption_keys = []
        for rotation in range(1, 26):
            test_phrase = ""
            for char in secret_text:
                if char in alphabet:
                    test_phrase += alphabet[((alphabet.index(char)-rotation)) % 26]
                elif char == " ":
                    test_phrase += " "
            if secret_word in test_phrase.split():
                decryption_keys.append(rotation)
            rotation += 1
        if decryption_keys:
            print("Rotations found: {}".format(*decryption_keys))
        else:
            print("No decryption key found.")

        # decode string
        for key in decryption_keys:
            plain_text = ""
            for char in secret_text:
                if char in alphabet:
                    char_index = alphabet.index(char)
                    plain_text += alphabet[((alphabet.index(char)-key)) % 26]
                elif char == " ":
                    plain_text += " "
            print("Decrypted Message, Rotation({0}): {1}".format(
                key, plain_text))
    elif input_choice == 'q':
        print("Exiting program...mischief managed")
        keep_going = False
    else:
        print('ERROR: Please enter "e", "d", or "q".')
