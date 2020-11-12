'''
Eu preciso da imagem inteira para o trabalho de Visão Computacional?
'''
from PIL import Image

#Carregar a imagem a ser cortada (crop)
img = Image.open("../images/5.jpg")
ret = (100,260,480,480)
crop_img = img.crop(ret)

crop_img = crop_img.transpose(Image.ROTATE_90)
crop_img.show()