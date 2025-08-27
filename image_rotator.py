from PIL import Image
import argparse # importa el módulo argparse

# inicializa el analizador sintáctico
parser = argparse.ArgumentParser()
parser.add_argument('input_file')      # primer argumento: archivo de entrada
parser.add_argument('output_file')     # segundo argumento: archivo de salida
parser.add_argument('angle', type=int) # tercer argumento: ángulo


args = parser.parse_args()              # analiza los argumentos
im = Image.open(args.input_file)        # carga una imagen del argumento input_file
print(im.size)
rotated = im.rotate(args.angle, expand=True)     # gira la imagen en un ángulo proporcionado como argumento
rotated.save(args.output_file)                   # guarda la imagen girada usando la ruta de salida de un argumento output_file
print(rotated.size)


