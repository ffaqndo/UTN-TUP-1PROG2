# EJERCICIO 1: IMPRIMIR DEL 1 AL 100.
for contador in range (1, 100):
    print (contador)

# EJERCICIO 2: CONTADOR DE DIGITOS DE UN ENTERO.
numero = str(input("Ingrese un numero por pantalla para visualizar sus digitos\n"))
contador = 0 
for i in range (len(numero)):
    contador+=1

print (f"La cantidad de digitos presentes en {numero} es de: {contador}")

# EJERCICIO 3: SUMADOR DE ENTEROS ENTRE DOS NUMEROS.
numero1 = int(input("Ingrese el primer numero\n"))
numero2 = int(input("Ingrese el segundo numero\n"))
sumador = 0

for i in range ((numero1+1), (numero2)):
    sumador+=i
print (sumador)

# EJERCICIO 4: SUMADOR SECUENCIAL DE ENTEROS.
numero = 1
sumador = 0

while numero != 0:
    numero = int(input("Ingrese los valores que quiere sumar, presione 0 para salir y mostrar el resultado acumulado"))
    sumador = sumador + numero 
print(f"La suma de los numeros ingresados da como resultado {sumador}")

# EJERCICIO 5: ADIVINAR EL NUMERO ALEATORIO.
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



