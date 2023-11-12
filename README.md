# 👋🏼Welcome to Dark PDF Converter

### About Dark PDF Converter
***Dark PDF Converter** is a conversion tool, that was created to resolve the glaring issue of light themed ebooks. It was created as a quick solution to continue working on the [FCC Python For Everybody](https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody) course without being constantly blinded.*

## REQUIRES POPPLER TO RUN
*This tool relies on poppler which can be downloaded, extracted, and added to your system environment variable path. If you don't have it installed, and configured the program will not run successfully.*

You can download [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows) which is a binary build nicely zipped for your convenience by *oschwartz*.

**What is Poppler?**\
*Poppler is a PDF rendering library based on the xpdf-3.0 code base. You can learn more on the Poppler official website [here](https://poppler.freedesktop.org/).*

## Getting Started:

- Create an input folder, where you will store the original PDF that you wish to convert.

- Run `pip install -r requirements.txt` to install the required modules to run the project.

- Run `py main.py`

```diff
You will be prompted to enter the name of the PDF you want to have converted. You should enter the name of the PDF without providing the extension. Once you hit enter it will show you where files will be stored.

Once the program has completed, there will be a folder called output that contains a folder with the name of the PDF that you wanted to convert. In that folder will be the dark_[PDF_NAME].pdf which is the completed dark theme PDF.

+ Maps each page into an image, and stores it in a list.
+ Saves each page of the PDF as an image.
+ Modifies each image, masking white to a dark gray.
+ Converts processed images into final PDF.

- Image optimization could be improved, currently the final PDF after processing all the images is a bit large.

- Known issue is that the images are removed in the final dark themed PDF. This is one of the problems that need to be resolved eventually. 

```

### Project Started By

**Waco Stimson**\
*AI Prompt Engineer*\
[Connect on LinkedIn](https://www.linkedin.com/in/waco-stimson-3abb992b/)

**Johnathan Shoff**\
*Software Engineer*\
[Connect on LinkedIn](https://www.linkedin.com/in/fearthedev/)

**Jaquita Shoff**\
*Data Analyst*\
[Connect on LinkedIn](https://www.linkedin.com/in/jaquitashoff/)