# Importing required libraries
from PIL import Image
import numpy as np

def process_image(image_path, output_folder):
    """
    This function processes an image to display in dark mode.
    It uses a dark charcoal grey background and a off-white text.
    """
    # Open the image file
    img = Image.open(image_path)
    # Convert the image to RGB
    img = img.convert('RGB')

    # Define the color transformation
    transformation = {
        'background': (38, 50, 56),  # dark charcoal grey
        'text': (200, 200, 200)  # dark white
    }

    # Apply the color transformation
    data = np.array(img)
    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask_background = (red == 255) & (green == 255) & (blue == 255)
    mask_text = np.invert(mask_background)
    data[:,:,:3][mask_background] = transformation['background']
    data[:,:,:3][mask_text] = transformation['text']

    # Create a new Image object
    img = Image.fromarray(data)

    # Save the processed image
    processed_image_path = image_path.replace('.png', '_processed.png')
    processed_image_path = processed_image_path.replace('page_', 'darkpage_')
    img.save(processed_image_path)

    return processed_image_path


