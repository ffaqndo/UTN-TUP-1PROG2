#EJERCICIO 1: 
def imprimir_hola_mundo():
    return ("Hola mundo")

print (imprimir_hola_mundo())

#EJERCICIO 2:
def saludar_usuario(nombre):
    return (f"Hola, {nombre}!")

nombre = str(input("¿Cual es su nombre? "))
print (saludar_usuario(nombre))

#EJERCICIO 3:
def informacion_personal(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años, y soy de {residencia}.")

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
residencia = str(input("Ingrese su residencia: "))
print (informacion_personal(nombre, apellido, edad, residencia))

#EJERCICIO 4:
def calcular_area_circulo(radio):
    area = 3.14 * (radio**2)
    return (f"El valor del area del circulo es de: {area}")
def calcular_perimetro_circulo(radio):
    perimetro = (2 * 3.14) * radio
    return (f"El valor del perimetro del circulo es de: {perimetro}")

radio = int(input("Ingrese el radio del circulo: "))
print (f"{calcular_area_circulo(radio)}\n{calcular_perimetro_circulo(radio)}")

#EJERCICIO 5:
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese los segundos que decia convertir a horas: "))
print (f"Los segundos ingresados equivalen a {segundos_a_horas(segundos)} hora/s.")

#EJERCICIO 6:
def tabla_multiplicar(numero):
    for i in range (10):
        print (numero * i)
numero = int(input("Ingrese el numero que desea ver su tabla de multiplicacion: "))
print (tabla_multiplicar(numero))

#EJERCICIO 7:
def operaciones_basicas(a, b):
    print (f"{a} + {b} = {a+b}")
    print (f"{a} - {b} = {a-b}")
    print (f"{a} * {b} = {a*b}")
    print (f"{a} / {b} = {a/b}")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
print (operaciones_basicas(a, b))

#EJERCICIO 8:
def calcular_imc(peso, altura):
     imc = peso / altura**2
     return imc
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
print (calcular_imc(peso, altura))

#EJERCICIO 9: 
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
celsius = float(input("Ingrese la temperatura en celsius: "))
print (f"La temperatura ingresada equivale a {celsius_a_fahrenheit(celsius)}° Fahrenheit")

#EJERCICIO 10:
def calcular_promedio (a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
print (f"El promedio de los numeros ingresados es de {calcular_promedio(a, b, c)}")
