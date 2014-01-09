# Convert Image to PNG/GIF/JPG format.

from PIL import Image

source_file_path = raw_input("What source file?")
im = Image.open(source_file_path)
convert_format = raw_input("What target format (png/jpg/gif)?")

if (convert_format == "jpg"):
		im.save(source_file_path + ".jpg");
		print "Converted to " + source_file_path + ".jpg"
elif (convert_format == "gif"):		
		im.save(source_file_path + ".gif");
		print "Converted to " + source_file_path + ".gif"
elif (convert_format == "png"):
		im.save(source_file_path + ".png");
		print "Converted to " + source_file_path + ".png"
else:
		print "Only supports jpg/gif/png.";
