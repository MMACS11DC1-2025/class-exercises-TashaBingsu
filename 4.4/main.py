import turtle

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    return t

#koch snowflake
# I used these links to help with the code:
#https://inventwithpython.com/recursion/chapter9.html
#https://understanding-recursion.readthedocs.io/en/latest/13%20Koch%20Curves.html
def draw_koch(t, length, depth, calls):
    calls += 1 #when the function calls itself, calls increase by 1
    
    if depth == 0:
        t.forward(length)
        return calls
    
    length /= 3
    calls = draw_koch(t, length, depth - 1, calls)
    t.left(60)
    calls = draw_koch(t, length, depth - 1, calls)
    t.right(120)
    calls = draw_koch(t, length, depth - 1, calls)
    t.left(60)
    calls = draw_koch(t, length, depth - 1, calls)
    
    return calls

#square fractal
#I used inspiration from this link but reused variables from the snowflake
#https://stackoverflow.com/questions/59009062/generating-square-fractals-with-python
#similar process of dividing the length
def draw_sqr_frac(t, length, depth, calls):
    calls += 1
    
    if depth == 0:
        for _ in range(4):
            t.forward(length)
            t.right(90)
        return calls
    
    # drwas smaller squares at each corner
    length /= 3
    
    for i in range(4):
        #draws main square side
        t.forward(length)
        
        # saves the position for the smaller square
        t.left(90)
        calls = draw_sqr_frac(t, length, depth - 1, calls)
        t.right(90)
        
        t.forward(length)
        t.right(90)
    
    return calls

#starts generating here
t  = setup_turtle()

#fractal settings dictionary
fractals = {
    "1": {"name": "Koch Snowflake", "color": "pink"},
    "2": {"name": "Square Fractal", "color": "black"}
}

print("Recursive Fractal Art Generator!")
print("1. Koch Snowflake") 
print("2. Square Fractal")

choice = input("Please choose a fractal, 1 or 2: ")

if choice not in fractals:
    print("Sorry, I'll just pick for you then. I pick the Koch Snowflake.")
    choice = "1"

while True:
    depth = int(input("Enter depth (1-4): "))
    if 1 <= depth <= 4:
        break
    print("Please enter between 1-4.")

#setting the color and position of fractals
t.color(fractals[choice]["color"])
t.penup()

if choice == "1":
    t.goto(-120, 100)
    t.pendown()
    #first option: koch triangle
    calls = 0
    for _ in range(3):
        calls = draw_koch(t, 300, depth, calls)
        t.right(120)
else:  #second option: square fractal
    t.goto(-30, 80)
    t.pendown()
    calls = draw_sqr_frac(t, 200, depth, 0)

#i will admit i used ai to help fix errors but then it changed my code along with comments, 
# so i want to change them back to how i wouldve said it. 
# (if you're wondering about the difference in commits.)
