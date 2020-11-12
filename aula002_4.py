'''
Eu preciso da imagem inteira para o trabalho de Visão Computacional?
'''
from PIL import Image

#Carregar a imagem a ser cortada (crop)
img = Image.open("../images/5.jpg")
dimensao = (100,260,480,480)
crop_img = img.crop(dimensao)
crop_img.save("../images/img_crop.jpg")
img.show()
crop_img.show()

