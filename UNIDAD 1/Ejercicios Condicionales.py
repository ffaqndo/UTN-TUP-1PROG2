
# EJERCICIO 1: MAYORIA DE EDAD.

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


# EJERCICIO 6: MEDIA, MEDIANA Y MODA.

from random import randint
from statistics import median, mode, mean 
numeros_aleatorios = [randint(1,100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print ("Sesgo positivo")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo")
elif media == mediana and mediana == moda:
    print ("Sin Sesgo")

print (f"Los numeros aleatorios seleccionados son: {numeros_aleatorios}")
print (f"La media es: {media:.2f}")
print (f"La mediana es: {mediana:.2f}")
print (f"Y la moda, es: {moda:.2f}")


# EJERCICIO 7: PALABRA CON Y SIN VOCAL.

palabra = str(input("Ingrese una palabra"))
vocales = "aeiouAEIOU"
palabra[-1]

if palabra[-1] in vocales:
    print (f"{palabra}!")
else:
    print (palabra)

# EJERCICIO 8: NOMBRE EN MAY, MIN, O TITTLE.

nombre = str(input("Ingrese su nombre\n"))
opcion = int(input("SELECCIONE UN NUMERO SEGUN LA OPCION QUE SOLICITE\n1: Para printear su nombre en Mayúsculas\n2: Para printear su nombre en Minusculas\n3: Para printear su nombre con una Mayuscula en el comienzo\n"))

if opcion == 1:
    print (nombre.upper())
elif opcion == 2:
    print (nombre.lower())
elif opcion == 3:
    print (nombre.tittle())
else:
    print ("Ingrese una opcion entre el 1 y el 3")

# EJERCICIO 9: MAGNITUD DE TERREMOTOS.

magnitud = int(input("Ingrese la magnitud del terremoto\n"))

if magnitud < 3:
    print ("Muy leve (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve (Ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado (Sentido por personas, pero generalmente no ocasiona daños)")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte (Puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte (Puede causar daños significativos)")
elif magnitud >=7:
    print ("Extremo (Puede causar graves daños a gran escala)")

# EJERCICIO 10: ESTACION DEL AÑO SEGUN HEMISFERIO.

    hemisferio = int(input("Ingrese en que hemisferio se encuentra\n1: HEMISFERIO NORTE\n2: HEMISFERIO SUR\n"))
dia = int(input("Ingrese el dia del mes\n"))
mes = int(input("Ingrese el mes del año\n"))

  #HEMISFERIO NORTE:
if hemisferio == 1:
    if ((dia >= 21 and dia <=31) and (mes == 12)) or ((dia >=1 and dia<=31) and (mes >=1 and mes <=2)) or ((dia>=1 and dia <=20) and (mes == 3)):
        print ("Estas en invierno")
    elif ((dia >=21 and dia <=31) and (mes == 3)) or ((dia >= 1 and dia <=31) and (mes>= 4 and mes <=5)) or ((dia>=1 and dia<=20) and (mes== 6)):
        print ("Estas en primavera")
    elif ((dia >=21 and dia <=31) and (mes == 6)) or ((dia >= 1 and dia <=31) and (mes>= 7 and mes <=8)) or ((dia>=1 and dia<=20) and (mes== 9)):
        print ("Estas en verano")
    elif ((dia >=21 and dia <=31) and (mes == 9)) or ((dia >= 1 and dia <=31) and (mes>= 10 and mes <=11)) or ((dia>=1 and dia<=20) and (mes== 12)):
        print ("Estas en Otoño")

  #HEMISFERIO SUR:
elif hemisferio == 2:
    if ((dia >= 21 and dia <=31) and (mes == 12)) or ((dia >=1 and dia<=31) and (mes >=1 and mes <=2)) or ((dia>=1 and dia <=20) and (mes == 3)):
        print ("Estas en verano")
    elif ((dia >=21 and dia <=31) and (mes == 3)) or ((dia >= 1 and dia <=31) and (mes>= 4 and mes <=5)) or ((dia>=1 and dia<=20) and (mes== 6)):
        print ("Estas en otoño")
    elif ((dia >=21 and dia <=31) and (mes == 6)) or ((dia >= 1 and dia <=31) and (mes>= 7 and mes <=8)) or ((dia>=1 and dia<=20) and (mes== 9)):
        print ("Estas en invierno")
    elif ((dia >=21 and dia <=31) and (mes == 9)) or ((dia >= 1 and dia <=31) and (mes>= 10 and mes <=11)) or ((dia>=1 and dia<=20) and (mes== 12)):
        print ("Estas en primavera")
