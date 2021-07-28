# prompt
name = input("Enter your name: ")

# response
if len(name) <= 3:
    print("Hi {}, you have a short name.".format(name))
elif 4 <= len(name) <= 8:
    print("Hi {}, nice to meet you.".format(name))
else:
    print("Hi {}, you have a long name.".format(name))
