import time

t0 = time.time()
from PIL import Image
t1 = time.time()


def colour(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    elif r > 160 and g > 0 and b > 1:
        return "red"
    elif r > 15 and g > 90 and b > 15:
        return "green"
    elif r > 45 and g > 55 and b > 178:
        return "blue"
    elif r > 0 and g > 0 and b > 0:
        return "black"
    elif r > 210 and g > 110 and b < 10:
        return "orange"
    else:
        return "other"

   
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

yellow_pixels = []
red_pixels = []
green_pixels = []
blue_pixels= []
black_pixels= []
orange_pixels = []

width = file.width
height = file.height

t2 = time.time()

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x, y), (255, 255, 255))
        if colour(pixel_r, pixel_g, pixel_b) == "red":
            red_pixels.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "green":
            green_pixels.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "blue":
            blue_pixels.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "black":
            black_pixels.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "orange":
           orange_pixels.append(jb_image[x,y])


t3 = time.time()
       
num_yellow = len(yellow_pixels)
num_red = len(red_pixels)
num_green = len(green_pixels)
num_blue = len(blue_pixels)
num_black = len(black_pixels)
num_orange = len(orange_pixels)


total_pixels = width*height
file.save("output.png", "png")


yellow_ratio = num_yellow / total_pixels
red_ratio = num_red / total_pixels
green_ratio = num_green / total_pixels
blue_ratio = num_blue / total_pixels
black_ratio = num_black / total_pixels
orange_ratio = num_orange / total_pixels


num_yellow = len(yellow_pixels)
num_red = len(red_pixels)
num_green = len(green_pixels)
num_blue = len(blue_pixels)
num_black = len(black_pixels)
num_orange = len(orange_pixels)

yellow_percent = yellow_ratio * 100
red_percent = red_ratio * 100
green_percent = green_ratio * 100
blue_percent = blue_ratio * 100
black_percent = black_ratio * 100
orange_percent = orange_ratio * 100

report = "there are {:.2f}% yellow jelly beans, {:.2f}% red jelly beans, {:.2f}% green jelly beans," \
          " {:.2f}% blue jelly beans, {:.2f}% black jelly beans, {:.2f}% orange jelly beans".format(yellow_percent, red_percent, green_percent, blue_percent, black_percent, orange_percent)
print(report)

module_load = t1- t0
image_open_load = t2 - t1
loop = t3 - t2
entire = t3 - t0

timings = "it took {:.2f}s to import PIL, {:.2f}s to load the image," \
            " {:.2f}s to do the loop. All in all it took {:.2f}s".format(module_load, image_open_load, loop, entire)
print(timings)