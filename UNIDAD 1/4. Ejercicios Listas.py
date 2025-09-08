# EJERCICIO 1:
lista_de_numeros = []
for i in range (0, 101):
    if i % 4 == 0:
        lista_de_numeros.append(i)

print (lista_de_numeros)

# EJERCICIO 2: 
lista_aleatoria = [1, 2, 3, 4, 5]
print (lista_aleatoria[3])

# EJERCICIO 3: 
lista_de_palabras = []
for i in range (0, 3):
   palabra = input (f"Ingrese la palabra {i+1} ")
   lista_de_palabras.append(palabra)

print (lista_de_palabras)

# EJERCICIO 4:
animales = ["perro", "gato", "conejo", "pez"]
for i in range (len(animales)):
    respuesta = str(input(f"Desea cambiar el valor {i+1} de la lista? "))
    if respuesta == "si":
        animales[i] = str(input("Ingrese el valor por el cual desea reemplazarlo "))
    elif respuesta == "no":
        pass
    
print (animales)

# EJERCICIO 5:
numeros = [1, 2, 3, 4, 5]
numeros.remove(max(numeros))
print (numeros)
print ("Lo que hace este codigo es eliminar el valor mas grande de la lista")

# EJERCICIO 6:
lista_de_numeros = list(range(10, 31, 5))
print (lista_de_numeros[:2])

# EJERCICIO 7:
autos = ["sedan", "polo", "suran", "gol"]
print (f"Su cadena actual es: {autos}")
autos[1] = str(input(f"Ingrese el segundo valor: "))
autos[2] = str(input(f"Ingrese el tercer valor: "))

print (f"Su nueva cadena es: {autos}")

# EJERCICIO 8:
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print (dobles)

# EJERCICIO 9:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"]]

compras[0].append("jugo")
compras[1][1] = ("tallarines")

del compras[0][0]

print (compras)

#EJERCICIO 10:
lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]
print (lista_anidada)
#FIN
