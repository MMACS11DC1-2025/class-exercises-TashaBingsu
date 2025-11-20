from PIL import Image

def colour(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    elif r < 30 and g < 30 and b < 30:
        return "black"
    else:
        return "other"
    
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

print(jb_image[0,0])
print(colour(jb_image[0,0][0], jb_image[0,0][1], jb_image[0,0][2]))

yellow_pixels = []
black_pixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

        if colour(pixel_r, pixel_g, pixel_b) == "black":
            black_pixels.append(jb_image[x,y])
            file.putpixel((x,y), (255, 255, 255))

num_yellow = len(yellow_pixels)
total_pixels = width*height
file.save("output.png", "png")

yellow_ratio = num_yellow / total_pixels

print(len(yellow_pixels))
print(width*height)
