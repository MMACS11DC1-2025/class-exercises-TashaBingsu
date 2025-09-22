"""
Write an Age in 2049 program that asks your age and outputs how old you'll be 31 years from now.

Examples:

How old are you?
> 10
In 2056, you will be 41 years old!
--
How old are you?
> 25
In 2056, you will be 56 years old!
"""

age = int(input("How old are you? "))
result = age + 31

if age == 4:
    print("YOU ARE THE YOUNGEST PERSON EVER!!!!")
else:
    print("You will be " + str(result) + " years old in 2056!")
