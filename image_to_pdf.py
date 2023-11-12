# Importing required libraries
from fpdf import FPDF
from PIL import Image
import os

def image_to_pdf(image_paths, output_pdf_path):
    """
    This function converts a set of images into a PDF.
    Each image will be one separate page in the PDF.
    """
    print("Compiling PDF: ", output_pdf_path)
    # Create a PDF object
    pdf = FPDF()

    # Add each image to the PDF
    for image_path in image_paths:
        print("Building: ", image_path)

        # Open the image file
        img = Image.open(image_path)
        # Get the dimensions of the image
        width, height = img.size
        # Convert the dimensions from pixel to millimeter
        width, height = width * 0.264583, height * 0.264583
        # Add a page to the PDF with the dimensions of the image
        pdf.add_page(format=(width, height))
        # Add the image to the page
        pdf.image(image_path, 0, 0, width, height)

    # Save the PDF
    pdf.output(output_pdf_path, "F")
    print("PDF Saved: ", output_pdf_path)


