from PIL import ImageOps,Image
from matplotlib import pyplot as plt

img = Image.open("../images/ceu.jpg")


img_gray = img.convert("L")
histo001 = img_gray.histogram()

img_gray = ImageOps.equalize(img_gray)
histo002 = img_gray.histogram()

plt.subplot(211)
plt.xlabel("Níveis de cinza")
plt.ylabel("Ocorrências")
plt.axis([0,256,0,max(histo001)])
for i in range(0,256):
    plt.bar(i,histo001[i])

plt.subplot(212)
plt.xlabel("Níveis de cinza")
plt.ylabel("Ocorrências")
plt.axis([0,256,0,max(histo002)])
for i in range(0,256):
    plt.bar(i,histo002[i])

plt.show()


