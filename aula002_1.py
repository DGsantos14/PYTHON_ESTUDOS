from PIL import Image
# Carregar uma imagem
img = Image.open("../images/5.jpg")
img.show()
img.save("../images/5_salva.jpg")