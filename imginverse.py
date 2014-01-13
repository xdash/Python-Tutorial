# Inverse Image

from PIL import Image
import PIL.ImageOps

source_file_path = raw_input("What source file would you like to inverse?")
img = Image.open(source_file_path.strip())

reverted_img = PIL.ImageOps.invert(img)
reverted_img.save(source_file_path.strip())

print "Inversed."
