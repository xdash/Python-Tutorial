# Convert Image to PNG/GIF/JPG format.

from PIL import Image

source_file_path = raw_input("What source file?")
im = Image.open(source_file_path.strip())
convert_format = raw_input("What target format (png/jpg/gif)?")

if (convert_format == "jpg"):
		im.save(source_file_path.strip() + ".jpg");
		print "Converted to " + source_file_path.strip() + ".jpg"
elif (convert_format == "gif"):		
		im.save(source_file_path.strip() + ".gif");
		print "Converted to " + source_file_path.strip() + ".gif"
elif (convert_format == "png"):
		im.save(source_file_path.strip() + ".png");
		print "Converted to " + source_file_path.strip() + ".png"
else:
		print "Only supports jpg/gif/png.";
