# input
input_text = input("Line: ")

if "robot" in input_text.lower():
    if "ROBOT" in input_text.split():
        print("There is a big robot in the line.")
    elif "robot" in input_text.split():
        print("There is a small robot in the line.")
    elif "robot" not in input_text.lower().split():
        print("No robots here.")
    else:
        if "robot" in input_text.lower().split():
            print("There is a medium sized robot in the line.")
else:
    print("No robots here.")
