import fitz

# Open the PDF file
doc = fitz.open("games.pdf")

# Print out the number of pages
#print(doc.page_count)

# load the first page from the PDF
page = doc.load_page(0)

# extract all links from the page and store it under - links
links = page.get_links()

# print the links object
#print(links) 

# print the actual links stored under the key "uri"
# for obj in links:
#   print(obj["uri"])

# Extract all the links in a PDF document
def extract_link(path_to_pdf):
  links = []
  doc = fitz.open(path_to_pdf)

  for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    page_links = page.get_links()
    links.extend(page_links)
  return links

# print out all the links returned from the PDF document
def print_all_links(links):
  for link in links:
    print(link["uri"])

# Call the function to extract all the links in a pdf
# all the return links are stored under all_links
all_links = extract_link("games.pdf")

# call the function to print all links in the PDF
print_all_links(all_links)