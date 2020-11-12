from PIL import Image

img = Image.open("../images/5.jpg")

img_pxMap = img.load()
#img1 = img.quantize(5)

for i in range(img.width):
    for j in range(img.height):
        pix = img.getpixel((i,j))
        lumR = int((pix[0]/5))
        lumG = int((pix[1]/5))
        lumB = int((pix[2]/5))
        img_pxMap[i,j] = (lumR,lumG,lumB)



img.show()


