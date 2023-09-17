import fitz
from io import BytesIO
from PIL import Image

doc = fitz.open("games.pdf")
page = doc.load_page(0)

# get a cross reference(xref) to the image
image_xref = page.get_images()

# get the actual xref value of the image
xref_value = image_xref[0][0]

# extract the image
img_dictionary = doc.extract_image(xref_value)

# get file extenstion
img_extension = img_dictionary["ext"]

# get the actual image binary data
img_binary = img_dictionary["image"]

# create a BytesIO object to work with the image bytes
image_io = BytesIO(img_binary)

# open the image using PIL library 
image = Image.open(image_io)

#specify the path where you want to save the image
output_path = "image_1.png"

# save the image
image.save(output_path)

# Close the BytesIO object 
image_io.close()