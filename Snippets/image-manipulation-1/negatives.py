from PIL import Image

# prompt for file
name = input("File name: ")
img = Image.open(name)

# for each pixel, subtract value from 255
for y in range(img.height):
    for x in range(img.width):
        orginal_value = img.getpixel((x, y))
        img.putpixel((x, y), 255 - orginal_value)
img.save('output.png')
