from PIL import Image
img = Image.open("../images/5.jpg")
r,g,b = img.split()
r.show()
g.show()
b.show()

im = Image.merge("RGB",(r,g,b))
im.show()