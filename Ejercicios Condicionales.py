
# EJERCICIO 1: Mayor de edad.

es_mayor_de_edad = 18
edad = int(input("¿Cual es tu edad?"))
if edad >= es_mayor_de_edad:
    print ("Eres mayor de edad")

elif edad < es_mayor_de_edad:
    print ("Eres menor de edad")


# EJERCICIO 2: APROBADO/DESAPROBADO.

nota = int(input("Ingrese su nota"))
if nota >= 6:
    print ("APROBADO")
else:
    print ("DESAPROBADO")

# EJERCICIO 3: NUMEROS PARES E IMPARES.

numero = int(input("Ingrese un numero par"))
if numero % 2 == 0:
    print ("HAS INGRESADO UN NUMERO PAR")
else:
    print ("POR FAVOR, INGRESE UN NUMERO PAR")


# EJERCICIO 4: CATEGORIA POR EDAD.

edad = int(input("Ingrese su edad"))

if edad > 0 and edad <12:
    print ("NIÑO")
elif edad>=12 and edad<18:
    print ("ADOLESCENTE")
elif edad >=18 and edad <30:
    print ("ADULTO JOVEN")
elif edad >= 30:
    print ("ADULTO")

    # EJERCICIO 5: CONTRASEÑA.

contraseña = str(input("Ingrese una contraseña de entre 8 y 14 caracteres"))
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print ("HA INGRESADO UNA CONTRASEÑA CORRECTA")
else:
    print ("INGRESE UNA CONTRASEÑA DE ENTRE 8 a 14 CARACTERES")

# EJERCICIO 6:

from random import randint
numeros_aleatorios = [randint(1,100) for i in range(50)]
print (numeros_aleatorios)

# EJERCICIO 7: PALABRA CON Y SIN VOCAL.

