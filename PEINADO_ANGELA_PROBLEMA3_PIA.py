#definimos una función para crear conjuntos 

def CreateArray(Array):
    while True:
        numero = input("Ingresa un número (o 'x' para terminar): ")  

        if numero.lower() == "x":  
            break  

        numero = float(numero)
        Array.append(numero)  

#Declaro la lista vacia en la que se insertaran los numeros
numerosArray1 = [] 
numerosArray2 = [] 

#Insertamos por teclado estos numeros

print("Ingresa números por teclado para formarel primer conjunto.")
CreateArray(numerosArray1)

print("Ingresa números por teclado para formar el segundo conjunto.")
CreateArray(numerosArray2)


print("La unión de ambos conjuntos es", list(set(numerosArray1) | set(numerosArray2))) #eliminamos los elementos duplicados
print("La intersección de ambos conjuntos es", list(set(numerosArray1) & set(numerosArray2))) #devolvemos los elementos que están presentes en ambos arrays
print("La diferencia de ambos conjuntos es", list(set(numerosArray1) - set(numerosArray2)))
