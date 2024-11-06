from PIL import Image
import numpy as np

# Load image
image = Image.open("house.jpg")
image_bw = image.convert("L") #converts image to monochrome


# Resize image to fit typical hanjie sizes (in this case 30x30 but can adjust)
image_resized = image_bw.resize((30, 30), Image.NEAREST)

# Convert image to numpy array and binarize (black/white as 0/255)
threshold = 185  # Threshold for binarization, alter depending on how pronouned the image is.
image_np = np.array(image_resized)
binary_image = (image_np > threshold).astype(int)  # 0 for black (filled), 1 for white (unfilled)
binary_image *= 255

#Shows black & white image solution
img = Image.fromarray(binary_image)
img.show()


# Function to calculate hanjie hints (rows & columns)
def calculate_hanjie_hints(binary_array):
    row_hints = []
    col_hints = []
    
    # Calculate row hints
    for row in binary_array:
        row_hint = []
        count = 0
        for pixel in row:
            if pixel == 0:  # If it's a filled pixel
                count += 1
            elif count > 0:
                row_hint.append(count) #Creates gap between numbers
                count = 0
        if count > 0:
            row_hint.append(count)
        row_hints.append(row_hint if row_hint else [0])
    
    # Calculate column hints
    for col in binary_array.T:
        col_hint = []
        count = 0
        for pixel in col:
            if pixel == 0: #Filled
                count += 1
            elif count > 0:
                col_hint.append(count) 
                count = 0
        if count > 0:
            col_hint.append(count)
        col_hints.append(col_hint if col_hint else [0])
    
    return row_hints, col_hints

# Calculate the nonogram hints
row_hints, col_hints = calculate_hanjie_hints(binary_image)
print("These are the row hints (top to bottom) for our hanjie):")
for hint in row_hints:
    print(hint)
print("And these are the column hints (from left to right):")
for hint in col_hints:
    print(hint)