
#Primero declaro la lista vacia en la que se insertaran los numeros
#y las dos listas donde se guadaran los numeros positivos y negativos

numeros = [] 
numerosPositivos = []
numerosNegativos = []

#Insertamos por teclado estos numeros

print("Ingresa números por teclado. Para finalizar, escribe 'x'.")

while True:
    numero = input("Ingresa un número (o 'x' para terminar): ")  

    if numero.lower() == "x":  
        break  

    numero = float(numero)
    numeros.append(numero)  

    if numero > 0:
        numerosPositivos.append(numero)  
    elif numero < 0:
        numerosNegativos.append(numero)  
    
#Hacemos las comprobaciones
for i in range(len(numeros)):
    if i >= 0:
        numerosPositivos.append(i)
    else:
        numerosNegativos.append(i)

print("La lista inicial era:",  numeros)
print("La lista de numeros positivos es:", numerosPositivos)
print("La lista de numeros negativos es:", numerosNegativos)


