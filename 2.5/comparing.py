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

print("Hello. Please enter your full name! We will be comparing you with another person from this class to see how compatible you two are.")
yourname = input("Your name is: ").lower().strip()

print("Ok awesomesauce -_-. Now enter your classmates name please.")
name2 = input("Classmate's name: ").lower().strip()

reccomendation= []
yourname_list = []
name2_list = []

for hi in file:
if str(yourname) in hi.lower():
yourname_list = hi.split(",")


