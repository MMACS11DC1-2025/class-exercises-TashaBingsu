from PIL import Image
import coolcolours

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_green = Image.open("kid-green.jpg").load()

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        im_r = image_green[i, j][0]
        im_g = image_green[i, j][1]
        im_b = image_green[i, j][2]

        if is_green(im_r,im_g,im_b):
            beach_colour = image_beach[i,j]
            xy = (i,j)
            image_output.putpixel(xy, beach_colour)

image_output.save("output.png", "png")