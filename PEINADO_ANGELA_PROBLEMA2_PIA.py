import re

#usamos la librería re para optimizar la eliminacion de signos de puntuación y 
#homogeneizar todo
frase = input("Ingresa una frase o un párrafo")

frase_sin_diferencias = re.sub(r'[^\w\s]', '', frase).lower()

#creamos un diccionario de palabras para crear pares clave - valor

diccionario = {}

