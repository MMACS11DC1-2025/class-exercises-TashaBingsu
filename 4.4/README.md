This program uses a recursive fractal generation approach.

How to use the program:
Run the program and input which fractal you would like to generate.
Either option 1 or option 2.
Option 1 is a Koch snowflake fractal.
Option 2 is a square fractal.
(If you do not pick either, the program will automatically pick option 1.)
Then, input what you want the depth of the fractal to be.
Pick from depth (1-4).
Depth means how many times the pattern repeats itself but in smaller scales.
If you do not enter a valid depth, the program will ask you repeatedly until you answer within 1-4.
And then the fractal will be printed!

Here are screenshots for both options of the program as well as when the user does not input an option:

Option 1:
![alt text](<Screenshot 2025-11-08 235758.png>)

Option 2:
![alt text](<Screenshot 2025-11-08 235728-1.png>)

Neither Option (Option 1, depth 4)
![alt text](<Screenshot 2025-11-08 235907.png>)

Testing, Debugging, and fixing up:

At first, my program had the option of using depths 1-6. But after peer reviews, my fellow peer Bella stated that picking depth 6 made printing the fractal too slow (When using trinket). Although the speed was set to 0, I decided to make the code say "Enter depth (1-4):", for shorter waiting times. I also added code to prevent the user from entering anything higher than 4. (See attached image)
![alt text](<Screenshot 2025-11-08 233342.png>)
But I also realized if the user doesn't enter an integer, the code stops, so I added something to continuously ask the user to enter 1-4 until they do.
![alt text](<Screenshot 2025-11-08 235302.png>)
The reason why I chose this approach instead of choosing the depth for the user like, I did with the fractal options is because that would be boring!

Bella also said that my original choice of colour which was yellow, was hard to see so I changed the square fractal color to black. hoho

For expected vs. actual results, I expected the square fractal to be centered but in reality...:
![alt text](<Screenshot 2025-11-09 004050.png>)