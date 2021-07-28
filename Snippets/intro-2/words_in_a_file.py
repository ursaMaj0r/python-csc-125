# prompt for input
keyword = input("Word to look for: ")

# open file
search_text = open('book.txt').read().lower()

# scan for keyword
if keyword in search_text:
    print("{} was found in the book.".format(keyword))
else:
    print("{} was not found in the book.".format(keyword))
