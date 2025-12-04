import time
t0 = time.time()

from PIL import Image
t1 = time.time()

image1 = Image.open("6.7/lung1.png").load()
image2 = Image.open("6.7/lung2.png").load()
image3 = Image.open("6.7/lung3.png").load()
image4 = Image.open("6.7/lung4.png").load()
image5 = Image.open("6.7/lung5.png").load()
image6 = Image.open("6.7/lung6.png").load()
image7 = Image.open("6.7/lung7.png").load()
image8 = Image.open("6.7/lung8.png").load()
image9 = Image.open("6.7/lung9.png").load()
image10 = Image.open("6.7/lung10.png").load()

def colour(r, g, b):
    if 150 <= r <= 180 and 150 <= b <= 180 and 150 <= g <= 180
        return "pneumonia alert!" 