import time

# Start timing
t0 = time.time()

from PIL import Image

images = ["6.7/lung1.png", "6.7/lung2.png", "6.7/lung3.png", "6.7/lung4.png", "6.7/lung5.png", 
          "6.7/lung6.png", "6.7/lung7.png", "6.7/lung8.png", "6.7/lung9.png", "6.7/lung10.png"]

def colour(r, g, b):
    # Converts all colours to grayscale value
    gray_value = int((r + g + b) / 3)
    
    if gray_value <= 100:  # Black - normal lungs
        return "black"
    elif gray_value <= 190:  # Gray - suspicious
        return "gray"
    else:  # White - pneumonia
        return "white"

# Percentage list to store all results
percentage = []

# Processing each image
for i in range(len(images)):
    current_file = images[i]
    
    # Opens image
    image = Image.open(current_file)
    image_pixels = image.load()
    
    width, height = image.size
    
    gray_pixels = []
    white_pixels = []
    black_pixels = []
    
    for x in range(width):
        for y in range(height):
            # Gets the RGB values from original image
            pixels = image_pixels[x, y]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            
            pixel_type = colour(r, g, b)
            
            if pixel_type == "gray":
                gray_pixels.append((x,y))
            elif pixel_type == "white":
                white_pixels.append((x,y))
            elif pixel_type == "black":
                black_pixels.append((x,y))

            gray_pixels_count = len(gray_pixels)  # Number of gray pixels
            white_pixels_count = len(white_pixels)
            black_pixels_count = len(black_pixels)
    
    total_pixels = width * height
    
    gray_percent = (gray_pixels_count / total_pixels) * 100
    white_percent = (white_pixels_count / total_pixels) * 100
    black_percent = (black_pixels_count / total_pixels) * 100

    # Calculate ed pneumonia score * weight need to fix this
    # White = 1.0, Gray = 0.5, Black = 0.0
    weighted_score = ((white_pixels_count * 1.0) + (gray_pixels_count * 0.5)) / total_pixels * 100
    
    # Determine pneumonia likelihood
    likely_pneumonia = False
    # Medical logic: Healthy lungs have lots of black (air)
    # Pneumonia lungs have less black because white and gray could indicate fluid/infection
    if black_percent <= 44:
        likely_pneumonia = True  # Less than 44% black = likely pneumonia
    else:
        likely_pneumonia = False  # More than 44% black = likely normal
    
    # Rounding values for display purposes
    gray_percent_display = round(gray_percent, 1)
    white_percent_display = round(white_percent, 1)
    black_percent_display = round(black_percent, 1)
    weighted_score_display = round(weighted_score, 1)
    
    # Adds to master(percentage) list
    result = {
        'filename': current_file,
        'gray_percent': gray_percent,
        'white_percent': white_percent,
        'black_percent': black_percent,
        'weighted_score': weighted_score,
        'likely_pneumonia': likely_pneumonia,
        'gray_display': gray_percent_display,
        'white_display': white_percent_display,
        'black_display': black_percent_display,
        'score_display': weighted_score_display
    }
    
    percentage.append(result)
    
    # prints results for each imgae
    print("Image " + str(i + 1) + ": " + current_file)
    print("  Black (normal): " + str(black_percent_display) + "%")
    print("  Gray (suspicious): " + str(gray_percent_display) + "%")
    print("  White (pneumonia): " + str(white_percent_display) + "%")
    print("  Weighted score: " + str(weighted_score_display))
    print("  Likely pneumonia: " + ("YES" if likely_pneumonia else "NO"))
    print()

# end time
t1 = time.time()
processing_time = t1 - t0
avg_time = processing_time / len(images)

# Format times to 3 decimal places
print("=" * 50)
print("Processing time: {:.3f} seconds".format(processing_time))
print("Average per image: {:.3f} seconds".format(avg_time))
print("=" * 50)
print()

# Selection Sort (unit 6)- sort by weighted score (highest to lowest)
def selection_sort(items):
    # 'items' is what gets passed in (your percentage list)
    for i in range(len(items)):
        largest_score = items[i]['weighted_score']
        largest_index = i
        
        for j in range(i+1, len(items)):
            if items[j]['weighted_score'] > largest_score:
                largest_score = items[j]['weighted_score']
                largest_index = j
        
        items[largest_index], items[i] = items[i], items[largest_index]
    
    return items

# sorts the results
sorted_results = selection_sort(percentage)

# Display top 5 using list slicing
print("TOP 5 RESULTS (Most likely pneumonia):")
print("=" * 50)

# Show top 5 or fewer if less than 5 images
display_count = min(5, len(sorted_results))

for i in range(display_count):
    item = sorted_results[i]
    rank = i + 1
    print(str(rank) + ". " + item['filename'])
    print("   Score: " + str(item['score_display']))
    print("   White %: " + str(item['white_display']) + "%")
    print("   Gray %: " + str(item['gray_display']) + "%")
    print()

'''
# Binary Search function
def binary_search(data, target_score):
    """Find image with specific score using binary search"""
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        current_score = data[mid]['weighted_score']
        
        # Allow small difference
        if abs(current_score - target_score) < 0.5:
            return mid
        elif current_score < target_score:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1  # Not found


# Binary search demonstration
print("BINARY SEARCH DEMONSTRATION:")
print("=" * 50)

# Search for different scores **NEED TO FIX
search_scores = [10, 20, 30, 40]
for target in search_scores:
    result_idx = binary_search(sorted_results, target)
    if result_idx != -1:
        found = sorted_results[result_idx]
        print("Found image with score ~" + str(target) + ": " + found['filename'])
        print("  Actual score: " + str(found['score_display']))
    else:
        print("No image found with score ~" + str(target))
'''
        
# Summary statistics
if percentage:
    '''
    print("=" * 50)
    print("SUMMARY STATISTICS:")
    print("=" * 50)
    '''
    total_images = len(percentage)
    pneumonia_count = 0
    
    total_white = 0
    total_gray = 0
    total_black = 0
    
    for item in percentage:
        if item['likely_pneumonia']:
            pneumonia_count += 1
        total_white += item['white_percent']
        total_gray += item['gray_percent']
        total_black += item['black_percent']
    
    avg_white = total_white / total_images
    avg_gray = total_gray / total_images
    avg_black = total_black / total_images
    
    print("Likely pneumonia cases: " + str(pneumonia_count))
    print("Average white % (pneumonia): " + str(round(avg_white, 1)) + "%")
    print("Average gray % (suspicious): " + str(round(avg_gray, 1)) + "%")
    print("Average black % (normal): " + str(round(avg_black, 1)) + "%")