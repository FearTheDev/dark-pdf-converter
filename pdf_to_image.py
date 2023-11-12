# Importing required libraries
from pdf2image import convert_from_path
import os

def pdf_to_image(pdf_path, output_folder):
    """
    This function converts a PDF into a set of images.
    Each page will be one separate image.
    Returns a list of image_paths.
    """

    print("Starting page extractions...")
    # Convert PDF to list of images
    images = convert_from_path(pdf_path)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        print("Creating director: ", output_folder)
        os.makedirs(output_folder)

    image_paths = []

    # Save each image
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i+1}.png')
        image.save(image_path, 'PNG')
        print("Saved image to: ", image_path)
        image_paths.append(image_path)

    print("Extraction completed...")
    return image_paths

