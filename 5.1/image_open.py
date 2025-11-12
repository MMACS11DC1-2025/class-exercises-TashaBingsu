from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

def is_green(r, g, b):
    if r >= 0 r < 25 and g > 230 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False

image_green = Image.open("kid-green.jpg").load()
image_beach = Image.open("beach.jpg").load()

print(image_greem[0,0])

pixel = image_green[0,0]
r = pixel[0]
g = image_green