import time
t0 = time.time()

from PIL import Image

t1 = time.time()

def colour(r, g, b):
    if r > 160 and g > 0 and b > 1:
        return "red"
    elif r > 15 and g > 90 and b > 15:
        return "green"
    elif r > 45 and g > 55 and b > 178:
        return "blue"
    else:
        return "other"

file = Image.open("5.1/ysabelle.jpg")
jb_image = file.load()




module_load = t1- t0
image_open_load = t2 - t1
loop = t3 - t2
entire = t3 - t0

timings = "it took {:.2f}s to import PIL, {:.2f}s to load the image," \
            " {:.2f}s to do the loop. All in all it took {:.2f}s".format(module_load, image_open_load, loop, entire)
print(timings)