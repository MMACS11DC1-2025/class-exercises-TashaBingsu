"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

score = 0
judy = ["Rate the performance from 1-10! ", "Rate the performance from 1-10! ", "Rate the performance from 1-10! ", "Rate the performance from 1-10! ", "Rate the performance from 1-10! "]

for i in judy:
    rate = float(input(i))
    score += rate
    
whatever = len(rate)

print("You got an average of " + str(score/whatever) + "!")