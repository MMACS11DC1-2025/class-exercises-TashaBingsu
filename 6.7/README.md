My theme is pneumonia xrays of lungs through multiple images. The visual feature my program will detect and count is the number of white and gray pixels in the image to determine whether the xray most likely contains pneumonia. This chosen feature will be identified through using a weighted score which takes the pixels and weights them based on medical logic. When the program counts the pixels, they will use the weighted pixels to calculate the overall score of the image. White is weighted the highest because white in the xray would mostly mean that its the most dense amount of fluid in the lungs.

To make sure each section workeed as intended, testing was performed on each section:
I tested with all 10 sample images (lung1.png through lung10.png) and validated pixel classification logic by checking edge cases.

![alt text](<Screenshot 2026-01-04 005453.png>)

I also verified that percentages sum to approximately 100% for each image by confirming the pixel counts match image dimensions (width × height). For selection sort testings, I sorting images from highest to lowest weighted score and confirmed it with displaying the top 5 most likely cases. For binary seach testings, the search returns correct images for the score ranges provided. I tested it by adding ranges with no matches and exact score matches.

Throughout the program, I implemented medical logic and had a 44% black pixels threshold to see whether the image
was an xray with pneumonia. I had consistent results across multiple runs. (I won't be providing an image because I can't prove they were different runs through screenshots.)

Some other points I used to ensure each tasks worked as intended:
Data integrity: All calculations use precise floating-point arithmetic before rounding for display.
Memory efficiency: Processes images one at a time to minimize memory usage.
Consistent outputs: Results are the same across multiple executions.


The program was profiled using Python's built-in time module. This is the timing report for processing 10 images:

![alt text](<Screenshot 2026-01-04 011043.png>)

The slowest parts of the program is using pixel-by-pixel processig. The nested loop processes every pixel individually. (O(n²) complexity)

One main challenge I faced was the threshold for deciding if the image contains enough of each pixel to be determined as pneumonia. I found this challenge to have quite an easy solution but it took me a very long while to think of it... Originally, this was the threshold:
![alt text](<Screenshot 2025-12-14 175057.png>)
Because I selected these images, I knew which ones did infact contain pneumonia or not but, the way I originally wrote this threshold with counting both the white and gray pixels, it was too complicated to find the numbers that determined the result of all images correctly. To solve this, instead of using white and grey and having to use < and >, I used just the black percentage because it was simpler. I did cheat though because I took the lowest percentage of an xray that contained pneumonia and used that as a threshold. Sorry, I will never become a scientist.