"""
Your friend's keyboard is misbehaving, 
and her "a", "e", and "o" keys are broken. 
To compensate, when she wants to type an o, she types ###. 
For an e she types ##, and for an a she types %%. 
Fed up with trying to interpret this ridiculous code, 
you decide to write a program to decipher her messages instead.
"""

# prompt
input_message = input("What did she say? ")

# fix o's
output_message = input_message.replace('###', 'o')

# fix e's
output_message = output_message.replace('##', 'e')

# fix a's
output_message = output_message.replace('%%', 'a')

# output
print("She meant to say:", output_message)
