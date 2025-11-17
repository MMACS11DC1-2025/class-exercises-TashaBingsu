from PIL import Image
import coolcolours

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for x in range(width):
    for y in range(height):
        im_r = image_green[x, y][0]
        im_g = image_green[x, y][1]
        im_b = image_green[x, y][2]

        if coolcolours.is_green(im_r,im_g,im_b) == "green":
            beach_colour = image_beach[x,y]
            image_output.putpixel((x, y), beach_colour)

image_output.save("output.png", "png")