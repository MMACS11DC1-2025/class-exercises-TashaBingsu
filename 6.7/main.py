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
    
width = file.width
height = file.height