# image_rotator.py

from PIL import Image # importa el módulo Image de la librería PIL

# carga una imagen llamada 'tripleten_logo.jpeg'.
im = Image.open('imagen_1.jpg')
print(im.size)
rotated = im.rotate(90)
rotated.save('rotated.png')