from PIL import Image

# prompt for file
name = input("File name: ")
img = Image.open(name)

# split into 3 profiles
red, green, blue = img.split()

# swap red and green
new_image = Image.merge('RGB', (green, red, blue))
new_image.save('output.png')
