from PIL import Image

# prompt for file
pixels_over_200 = 0
name = input("File name: ")
img = Image.open(name)

# for each pixel check if over limit
for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        if pixel >= 200:
            pixels_over_200 += 1

print("{} pixels are bright.".format(pixels_over_200))
