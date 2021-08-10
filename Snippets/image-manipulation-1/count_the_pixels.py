from PIL import Image
name = input("File name: ")

img = Image.open(name)
print("{} pixels!".format(img.width*img.height))
