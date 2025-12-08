import time
t0 = time.time()

from PIL import Image
t1 = time.time()

images = ["6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png", "6.7/lung1.png" ]

for i in images:
    file = Image.open(i)
    lungimage = file.load()

def colour(r, g, b):
    if 150 <= r <= 180 and 150 <= b <= 180 and 150 <= g <= 180
        return "grey"

t2 = time.time()

for i in range(len(images)):
    width = file.width
    height = file.height

    grey_pixels = []
    white_pixels = []
    black_pixels = []

    for x in range(width):
        for y in range(height):
            pixel_r = lungimage[x,y][0]
            pixel_g = lungimage[x,y][1]
            pixel_b = lungimage[x,y][2]

            if colour(pixel_r, pixel_g, pixel_b) == "grey":
                grey_pixels.append(lungimage[x,y])
                file.putpixel((x, y), (255, 255, 255))
            if colour(pixel_r, pixel_g, pixel_b) == "white":
                white_pixels.append(lungimage[x,y])