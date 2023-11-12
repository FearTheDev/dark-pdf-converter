# Importing required libraries
from pdf_to_image import pdf_to_image
from image_processing import process_image
from image_to_pdf import image_to_pdf
import os

def main(pdf_path, output_folder, output_pdf):

    print("PDF file: ", pdf_path)
    print("Output Path: ", output_folder)

    """
    This function converts a PDF into a set of images, processes each image to display in dark mode,
    and then converts the processed images back into a PDF.
    """
    # Convert the PDF into a set of images
    image_paths = pdf_to_image(pdf_path, output_folder + '\\raw')

    processed_image_paths = []

    # Process each image to display in dark mode
    for image_path in image_paths:
        print("Processing image: ", image_path)
        processed_image_path = process_image(image_path, output_folder)
        processed_image_paths.append(processed_image_path)

    # Convert the processed images back into a PDF
    output_pdf_path = os.path.join(output_folder, output_pdf)
    image_to_pdf(processed_image_paths, output_pdf_path)

if __name__ == "__main__":

    # Greet the user in the command-line.
    print("👋🏼Welcome to Dark PDF Converter")

    # Define the name of the ebook.
    pdf_name = (input("Choose a file: ") + ".pdf")

    # Define the path to the PDF file.
    pdf_path = 'ebooks\\' + pdf_name

    # Define the location to store the dark mode PDF.
    output_pdf = 'dark_' + pdf_name

    # Define the output folder PDF will be saved.
    output_folder = 'output\\' + pdf_name.split('.')[0]

    # Run the main function
    main(pdf_path, output_folder, output_pdf)
