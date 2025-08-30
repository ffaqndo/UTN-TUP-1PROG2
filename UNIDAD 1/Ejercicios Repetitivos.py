# EJERCICIO 1: IMPRIMIR DEL 1 AL 100.
print ("EJERCICIO 1: IMPRIMIR DEL 1 AL 100.\n")
for contador in range (1, 100):
    print (contador)

# EJERCICIO 2: CONTADOR DE DIGITOS DE UN ENTERO.
print ("EJERCICIO 2: CONTADOR DE DIGITOS DE UN ENTERO.\n")
numero = str(input("Ingrese un numero por pantalla para visualizar sus digitos\n"))
contador = 0 
for i in range (len(numero)):
    contador+=1

print (f"La cantidad de digitos presentes en {numero} es de: {contador}")

# EJERCICIO 3: SUMADOR DE ENTEROS ENTRE DOS NUMEROS.
print ("EJERCICIO 3: SUMADOR DE ENTEROS ENTRE DOS NUMEROS.\n")
numero1 = int(input("Ingrese el primer numero\n"))
numero2 = int(input("Ingrese el segundo numero\n"))
sumador = 0

for i in range ((numero1+1), (numero2)):
    sumador+=i
print (sumador)

# EJERCICIO 4: SUMADOR SECUENCIAL DE ENTEROS.
print ("EJERCICIO 4: SUMADOR SECUENCIAL DE ENTEROS.\n")
numero = 1
sumador = 0

while numero != 0:
    numero = int(input("Ingrese los valores que quiere sumar, presione 0 para salir y mostrar el resultado acumulado"))
    sumador = sumador + numero 
print(f"La suma de los numeros ingresados da como resultado {sumador}")

# EJERCICIO 5: ADIVINAR EL NUMERO ALEATORIO.
print ("EJERCICIO 5: ADIVINAR EL NUMERO ALEATORIO.\n")
from random import randint
numero_aleatorio = randint(0,10)
numero_ingresado = 11
intentos = 0
while numero_ingresado != numero_aleatorio:
    numero_ingresado = int(input("Ingrese un numero\n"))
    intentos+=1
    if numero_ingresado < numero_aleatorio:
        print ("El numero aleatorio es mayor al numero ingresado")
    elif numero_ingresado > numero_aleatorio:
        print ("El numero aleatorio es menor al numero ingresado")

print (f"El numero aleatorio era {numero_aleatorio}\nsu cantidad de intentos fue de: {intentos}")

# EJERCICIO 6: CONTADOR DE PARES, DE FORMA DECRECIENTE.
print ("EJERCICIO 6: CONTADOR DE PARES, DE FORMA DECRECIENTE.\n")
i = 0
for i in range (100, -1, -1):
    if i % 2 == 0:
        print (i)

# EJERCICIO 7: SUMA DE NUMEROS ENTRE 0 Y NUMERO INGRESADO.
print ("EJERCICIO 7: SUMA DE NUMEROS ENTRE 0 Y NUMERO INGRESADO.\n")
numero_ingresado = int(input("Ingrese el numero hasta el cual desea que se sumen los enteros\n"))
sumador = 0
if numero_ingresado > 0:
    for i in range (0, (numero_ingresado)):
        sumador+=i
else:
    print ("Ingrese un numero positivo")

print (f"La suma de los enteros comprendidos entre 0 y {numero_ingresado} da como resultado: {sumador}")

# EJERCICIO 8: CONTADOR DE PARES, IMPARES, NEGATIVOS Y POSITIVOS.
print ("EJERCICIO 8: CONTADOR DE PARES, IMPARES, NEGATIVOS Y POSITIVOS.\n")
cantidad_de_numeros = int(input("Ingrese la cantidad de numeros que desea analizar"))
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
print ("Ingrese los numeros que desea analizar")
for i in range (0, (cantidad_de_numeros)):
    numero_ingresado = int(input())
    if numero_ingresado % 2 == 0:
        contador_pares+=1
    elif numero_ingresado % 2 != 0:
        contador_impares+=1
    if numero_ingresado < 0:
        contador_negativos+=1
    elif numero_ingresado > 0:
        contador_positivos+=1

print (f"Segun los numeros ingresados por pantalla:\n * La cantidad de pares es de: {contador_pares}\n * La cantidad de impares es de: {contador_impares}\n * La cantidad de negativos es de: {contador_negativos}\n * La cantidad de positivos es de: {contador_positivos}")

# EJERCICIO 9: MEDIA DE LOS NUMEROS INGRESADOS.
print("EJERCICIO 9: MEDIA DE LOS NUMEROS INGRESADOS.\n")
from statistics import mean
cantidad = int(input("Ingrese la cantidad de numeros que desea ingresar\n"))
numeros = [0] * cantidad
for i in range (cantidad):
    numero = (int(input(f"Ingrese el numero {i+1}: ")))
    numeros [i] = numero


media = mean (numeros)
print (f"La media de los numeros ingresados es de: {media}")   

# EJERCICIO 10: INVERTIR EL NUMERO INGRESADO.
print ("EJERCICIO 10: INVERTIR EL NUMERO INGRESADO.\n")
numero = str(input("Ingrese el numero que desee invertir:\n"))
invertido = ""
for i in range (len(numero)-1, -1, -1):
    invertido+= numero[i]

print (f"El numero {numero} invertido es: {invertido}")