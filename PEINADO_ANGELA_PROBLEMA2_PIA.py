import re

#hacemos una funcion que s encarge del conteo
def ContarPalabrasRepetidas(palabras, diccionario):

#Si la palabra ya está en el diccionario, incrementamos su valor en 1.
#Si la palabra no está en el diccionario, la agregamos con un valor inicial de 1.
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    # mostramos el diccionario ordenado por la palabra 
    for palabra in sorted(diccionario):
        print(f"{palabra}: {diccionario[palabra]}")


#usamos la librería re para optimizar la eliminacion de signos de puntuación y 
#homogeneizar todo
frase = input("Ingresa una frase o un párrafo")

frase_sin_diferencias = re.sub(r'[^\w\s]', '', frase).lower()

#creamos un diccionario de palabras para crear pares clave - valor

palabras = frase_sin_diferencias.split()

diccionario = {}

ContarPalabrasRepetidas(palabras, diccionario)



    