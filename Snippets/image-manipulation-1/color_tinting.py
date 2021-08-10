from PIL import Image

# prompt for file
name = input("File name: ")
red_tint = int(input("Red tint: "))
green_tint = int(input("Green tint: "))
blue_tint = int(input("Blue tint: "))
img = Image.open(name)

# split into 3 profiles
red, green, blue = img.split()


# for each pixel, subtract value from 255
for y in range(img.height):
    for x in range(img.width):
        # red
        orginal_value_red = red.getpixel((x, y))
        red.putpixel((x, y), orginal_value_red + red_tint)
        # green
        orginal_value_green = green.getpixel((x, y))
        green.putpixel((x, y), orginal_value_green + green_tint)
        # blue
        orginal_value_blue = blue.getpixel((x, y))
        blue.putpixel((x, y), orginal_value_blue + blue_tint)


# output new image
new_image = Image.merge('RGB', (red, green, blue))
new_image.save('output.png')
