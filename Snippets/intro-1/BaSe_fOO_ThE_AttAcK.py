# input
input_raw = input("code: ")
input_reverse = input_raw.split()
input_reverse.reverse()
response = ""

# reponse
for word in input_reverse:
    upper_test = word[0].upper()
    if word[0] == upper_test:
        response += word.lower() + " "
print("says: {}".format(response.rstrip().replace("!", "")))
