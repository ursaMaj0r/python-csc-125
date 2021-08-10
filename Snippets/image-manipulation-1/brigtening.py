from PIL import Image

# prompt for file
name = input("File name: ")
img = Image.open(name)

# for each pixel, add 50
for y in range(img.height):
    for x in range(img.width):
        orginal_value = img.getpixel((x, y))
        img.putpixel((x, y), orginal_value + 50)
img.save('output.png')
