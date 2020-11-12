from PIL import Image

img = Image.open("../images/5.jpg")
img.show()
out = img.resize((128,128))
out.show()