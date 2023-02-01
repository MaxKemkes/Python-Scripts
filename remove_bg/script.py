from rembg import remove
import easygui as eg
from PIL import Image
import os


image_filetypes= ["*.jpeg", "*.jpg", "*.png", "*.webp", "*.bmp"]
image_naming = "Image Files"

input_path = eg.fileopenbox(title="Select image file", filetypes=[["*.jpeg", "*.jpg", "*.png", "*.webp", "*.bmp", "Image Files"]], multiple=True)
outputpath = eg.diropenbox(title="Select path to save to")

if input_path and outputpath:

  for path in input_path:
    tmp_path = os.path.abspath(path)
    tmp_file = os.path.basename(path)
    tmp_filename, tmp_extension = tmp_file.split(".")
    
    print(tmp_filename)
    
    input_img = Image.open(tmp_path)
    output_img = remove(input_img)
    
    output_filepath = outputpath+"/"+tmp_filename+"_no-bg."+tmp_extension.lower()
    output_img.save(output_filepath)
    image = Image.open(output_filepath)
    image.show()

# print(input_path)