import turtle

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    return t

def draw_koch(t, length, depth, call_count):
    """Draw Koch Curve"""
    call_count += 1
    
    if depth == 0:
        t.forward(length)
        return call_count
    
    length /= 3.0
    call_count = draw_koch(t, length, depth - 1, call_count)
    t.left(60)
    call_count = draw_koch(t, length, depth - 1, call_count)
    t.right(120)
    call_count = draw_koch(t, length, depth - 1, call_count)
    t.left(60)
    call_count = draw_koch(t, length, depth - 1, call_count)
    
    return call_count

def draw_square_fractal(t, length, depth, call_count):
    """Draw a square fractal pattern"""
    call_count += 1
    
    if depth == 0:
        for _ in range(4):
            t.forward(length)
            t.right(90)
        return call_count
    
    # Draw smaller squares at each corner
    length /= 3
    
    for i in range(4):
        # Draw main square side
        t.forward(length)
        
        # Save position for smaller square
        t.left(90)
        call_count = draw_square_fractal(t, length, depth - 1, call_count)
        t.right(90)
        
        t.forward(length)
        t.right(90)
    
    return call_count

def main():
    t = setup_turtle()
    
    # Fractal settings dictionary
    fractals = {
        "1": {"name": "Koch Snowflake", "color": "cyan"},
        "2": {"name": "Square Fractal", "color": "yellow"}
    }
    
    print("FRACTAL GENERATOR")
    print("1. Koch Snowflake") 
    print("2. Square Fractal")
    
    choice = input("Choose a fractal 1 or 2: ")
    
    if choice not in fractals:
        print("NOO. Fine, I'll pick the Koch snowflake then.")
        choice = "1"
    
    depth = int(input("Enter depth (1-6): "))
    
    # Set color and position
    t.color(fractals[choice]["color"])
    t.penup()
    
    if choice == "1":
        t.goto(-150, 100)
        t.pendown()
        # Draw triangle of Koch curves to make snowflake
        calls = 0
        for _ in range(3):
            calls = draw_koch(t, 300, depth, calls)
            t.right(120)
    else:  # Square fractal
        t.goto(-100, -100)
        t.pendown()
        calls = draw_square_fractal(t, 200, depth, 0)
    
    # Display results
    t.penup()
    t.goto(0, -200)
    t.color("white")
    
    t.goto(-200, -150)