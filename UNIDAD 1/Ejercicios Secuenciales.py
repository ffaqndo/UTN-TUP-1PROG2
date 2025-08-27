# Ejercicio a: HOLA MUNDO! 
print("Ejercicio a: HOLA MUNDO!")

print("Hola mundo!")

print("Ejercicio a TERMINADO")

# Ejercicio b: SALUDO PERSONAL 
print ("Ejercicio b: SALUDO PERSONAL")

nombre = input("¿Cual es tu nombre?\n")
print (f"Hola {nombre}!")

print("Ejercicio b TERMINADO")

# Ejercicio c: PRESENTACION 
print ("Ejercicio c: PRESENTACION")

nombre = input("¿Cual es tu nombre?\n")
apellido = input("¿Cual es tu apellido?\n")
edad = input("¿Cual es tu edad?\n")
lugar = input("¿Donde vivis?\n")

print (f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {lugar}")   

print ("Ejercicio c TERMINADO")

# Ejercicio d: CIRCULO   
print ("Ejercicio d: CIRCULO")

PI = 3.14
radio = float(input("Ingrese el radio del circulo\n"))
area = PI * radio**2
perimetro = 2 * PI * radio 

print (f"El area del circulo es de {area:.2f}")
print (f"El perimetro del circulo es de {perimetro:.2f}")

print("Ejercicio d TERMINADO")

# Ejercicio e: SEGUNDOS A HORAS
print ("Ejercicio e: SEGUNDOS A HORAS")

segundos = int(input("Ingrese los segundos que desea convertir a horas\n"))
horas = segundos / 3600
print (f"{segundos} segundos equivale a {horas:.2f} horas")

print("Ejercicio e TERMINADO")

# Ejercicio f: TABLA DE MULTIPLICAR
print ("Ejercicio f: TABLA DE MULTIPLICAR")

Numero = int(input("Ingrese el numero del cual desea averiguar su tabla de multiplicar\n "))
print (f"{Numero} * 1: {Numero * 1}")
print (f"{Numero} * 2: {Numero * 2}")
print (f"{Numero} * 3: {Numero * 3}")
print (f"{Numero} * 4: {Numero * 4}")
print (f"{Numero} * 5: {Numero * 5}")
print (f"{Numero} * 6: {Numero * 6}")
print (f"{Numero} * 7: {Numero * 7}")
print (f"{Numero} * 8: {Numero * 8}")
print (f"{Numero} * 9: {Numero * 9}")
print (f"{Numero} * 10: {Numero * 10}")

print("Ejercicio f TERMINADO")

# Ejercicio g: OPERACION DE ENTEROS 
print ("Ejercicio g: OPERACION DE ENTEROS")

Numero1 = 0
Numero2 = 0
while Numero1 == 0:
    Numero1 = int(input("Ingrese el primer numero:\n"))
    if Numero1 == 0:
        print("ERROR. No puedes ingresar 0")    
while Numero2 == 0:
    Numero2 = int(input("Ingrese el segundo numero:\n"))
    if Numero2 == 0:
        print("ERROR. No puedes ingresar 0")

print(f"{Numero1} + {Numero2} = {Numero1 + Numero2}")
print(f"{Numero1} - {Numero2} = {Numero1 - Numero2}")
print(f"{Numero1} * {Numero2} = {Numero1 * Numero2}")
print(f"{Numero1} / {Numero2} = {Numero1 / Numero2}")

print("Ejercicio g TERMINADO")

# Ejercicio h: INDICE CORPORAL 
print ("Ejercicio h: INDICE CORPORAL")

peso = float(input("Ingrese su peso en kg\n"))
altura = float(input("Ingrese su altura en mts\n"))
IMC = (peso / (altura**2))

print (f"Su peso de {peso}kg y su altura de {altura}mts dan como resultado un indice corporal de {IMC:.2f}")

print("Ejercicio h TERMINADO")

# Ejercicio i: CELSIUS A FAHRENHEIT
print ("Ejercicio i: CELSIUS A FAHRENHEIT")

Celsius = int(input("Ingrese la temperatura el Celsius\n"))
Fahrenheit = 9 / 5 * Celsius + 32

print(f"La temperatura ingresada en Celsius, da como resultado {Fahrenheit}° Fahreinheit")

print("Ejercicio i TERMINADO")

# Ejercicio j: PROMEDIO
print ("Ejercicio j: PROMEDIO")

a = int(input("Ingrese el valor 1\n"));
b = int(input("Ingrese el valor 2\n"));
c = int(input("Ingrese el valor 3\n"));

d = float(a + b + c);

Promedio = d // 3;

print (f"El promedio de los numeros ingresados {a}, {b} y {c}, dan como resultado: {Promedio}")

print("Ejercicio j TERMINADO")

# FINAL DE ALGORITMO