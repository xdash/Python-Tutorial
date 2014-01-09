# Resize Image to costomized width/height.

from PIL import Image

source_file_path = raw_input("What source file would you like to resize?")
img = Image.open(source_file_path.strip())
resize_width = raw_input("Width?")
resize_height = raw_input("Height?")

out = img.resize((int(resize_width),int(resize_height)))
out.save(source_file_path.strip())

print "Resized to " + resize_width + " x " + resize_height + "."
