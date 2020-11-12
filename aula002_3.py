from PIL import Image
img = Image.open("../images/5.jpg")
pixel = img.getpixel((50,50))
print(pixel)
print("R:",pixel[0])
print("G:",pixel[1])
print("B:",pixel[2])

