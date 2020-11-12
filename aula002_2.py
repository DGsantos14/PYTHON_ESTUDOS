from PIL import Image

img = Image.open("Z:\ARQUIVOS_IMAGENs\IMAGENS GERAIS\07-11-2013")
print("Formato:",img.format)
print("Tamanho: ",img.size)
print("MODO: ",img.mode)

print(img.width)
print(img.height)
