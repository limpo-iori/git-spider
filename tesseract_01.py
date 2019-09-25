import pytesseract
from PIL import Image
img = Image.open("test2.png")
text = pytesseract.image_to_string(img)
print(text)