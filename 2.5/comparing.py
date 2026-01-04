"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

file = open("2.4/responses.csv")
junk = file.readline()

print("Hello. Please enter your name! We will be comparing you with another person from this class to see how compatible you two are.")
yourname = input("Your name is: ").lower().strip()

# initialize variables
yourname_list = []
name2_list = []
found_yourname = False
found_name2 = False

# first look for the first name
for line in file:
    line_lower = line.lower()
    if yourname in line_lower and not found_yourname:
        yourname_list = line.strip().split(",")
        found_yourname = True
        break  # breaking because first name was found

# only ask for second name if first name was found
if found_yourname:
    print("Ok awesomesauce -_-. Now enter your classmates name please.")
    name2 = input("Classmate's name: ").lower().strip()
    
    # reset the file to look for second name
    file.seek(0)  # going back to start of file(i found this on youtube)
    junk = file.readline()  # skipping header again
    
    # now looking for second name
    for line in file:
        line_lower = line.lower()
        if name2 in line_lower and not found_name2:
            name2_list = line.strip().split(",")
            found_name2 = True
            break
else:
    quit("I don't have '" + yourname + "' in my list yo... Try again")

# checking if second name was found
if not found_name2:
    quit("I don't have '" + name2 + "' in my list yo... Try again")

# compare the responses (skip the first column which is the name)
similar = 0
total_qs = min(len(yourname_list), len(name2_list)) - 1  # minus 1 to exclude name

for i in range(1, total_qs + 1):  # start from 1 to skip name column
    if i < len(yourname_list) and i < len(name2_list):  # safety check!!!!!
        if yourname_list[i].strip().lower() == name2_list[i].strip().lower():
            similar += 1

# printing results and quirky lil messages
if similar == 0:
    print("Ok.. so you guys have 0 things in common. Hopefully you can still be friends!")
elif similar == 1:
    print("You have 1 thing in common with eachother! Maybe you guys like the same TV show then...?")
elif similar <= 3:
    print("Cool cool, you guys have " + str(similar) + " things in common. Be their friend :p")
elif similar <= 5:
    print("Nice! You guys have " + str(similar) + " things in common! That's pretty similar.")
elif similar <= 7:
    print("Alrighttt, I see good friends in the making. You guys have " + str(similar) + " things in common!")
elif similar == 8:
    print("P-P-Pause!! You guys have everything in common! Is this your twin perhaps?")


# print how compatibile you are
compatibility = (similar / total_qs) * 100
print("Your compatibility percent is: " + str(compatibility) + "%")