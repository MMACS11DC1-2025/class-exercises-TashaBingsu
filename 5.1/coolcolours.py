def is_green(r, g, b):
    if r <= 24 and g <= 255 and b <= 24:
        return("green")
    if r <= 24 and g <= 24 and b <= 255:
        return("blue")
    if r <= 255 and g <= 24 and b <= 24:
        return("red")
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b > 230 and b <= 255:
        return ("white")
    if r < 25 and r >= 0 and g < 25 and g >= 0 and b < 25 and b >= 0:
        return ("black")
    if r > 230 and r <= 255 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return ("yellow")
    if r > 230 and r <= 255 and g < 25 and g >= 0 and b > 230 and b <= 255:
        return ("magenta")