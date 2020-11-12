from PIL import Image

from PIL import Image
img = Image.open("../images/5.jpg")
img.show()
img_gray = img.convert("L")
img_pxMap = img.load()

for i in range(img.width):
    for j in range(img.height):
        pix = img.getpixel((i,j))
        lum = int((pix[0]*0.30 + pix[1]*0.59 + pix[2]*0.11))
        img_pxMap[i,j] = ((lum,lum,lum))
print(img.mode)
print(img_gray.mode)
