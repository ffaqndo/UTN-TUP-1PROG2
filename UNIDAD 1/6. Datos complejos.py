# EJERCICIO 1:
precios_frutas = {
    "banana": 1200,
    "anana": 2500,
    "melon": 3000,
    "uva": 1450
}

precios_frutas["naranja"] = 1200
precios_frutas["manzana"] = 1500
precios_frutas["pera"] = 2300
print (f"La lista de precios es la siguiente: {precios_frutas}")

# EJERCICIO 2:
precios_frutas["banana"] = 1330
precios_frutas["manzana"] = 1700
precios_frutas["melon"] = 2800
print (f"La nueva lista y con precios actualizados es la siguiente: {precios_frutas}")

# EJERCICIO 3:
frutas_sin_precio = list(precios_frutas.keys())
print (frutas_sin_precio)

# EJERCICIO 4:
contactos = {}
for i in range (5):
    contacto_agregar = str(input("Ingrese el nombre del contacto que desea agregar: ").title())
    numero_agregar = int(input("Ingrese el numero del contacto: "))
    contactos[contacto_agregar] = numero_agregar
print (f"Esta es su lista de contactos: {contactos}")

llave = str(input("Desea consultar por algun contacto en especifico? (si/no)").lower())
while llave == "si":
    contacto_averiguar = str(input("Ingrese el nombre del contacto por el que desea consultar: ").title())
    if contacto_averiguar in contactos:
        print (f"{contacto_averiguar}: {contactos[contacto_averiguar]}")
    else:
        print ("El contacto solicitado no corresponde a la agenda")
    llave = str(input("Desea consultar por otro contacto? (si/no): ").lower())

# EJERCICIO 5:
frase = str(input("Ingrese la frase deseada: ").lower())
lista_frase = frase.split()
frase_sin_repetir = set(lista_frase)

palabras_repetidas = {}

for palabra in lista_frase:
    if palabra in palabras_repetidas:
        palabras_repetidas[palabra] += 1
    else:
        palabras_repetidas[palabra] = 1

print (f"La palabra ingresada fue: {frase}")
print (f"Su frase, sin repetir: {frase_sin_repetir}")
print (f"Conteo de palabras repetidas: {palabras_repetidas}")

# EJERCICIO 6:
alumnos = {}
promedios = []

for i in range (3):
    alumno_agregar = str(input(f"Ingrese el nombre del {i+1}° alumno que desea agregar: ").title())

    notas = []

    for x in range (3):
        nota_agregar = int(input(f"Ingrese la {x+1} nota del alumno: "))
        notas.append (nota_agregar)
        notas_tupla = tuple(notas)
        alumnos[alumno_agregar] = notas_tupla
  
print (alumnos)

for alumno, notas_tupla in alumnos.items():
    promedios.append(alumno)
    promedio = sum(notas_tupla) / len(notas_tupla)
    print (f"El promedio del alumno {alumno} es de: {promedio}")

# EJERCICIO 7:
parcial1 = []
parcial2 = []

for i in range(3):
    alumno_agregar = input(f"Ingrese el nombre del {i+1}° alumno del P1: ").title()
    parcial1.append(alumno_agregar)
parcial1 = set(parcial1)

for x in range(3):
    alumno_agregar = input(f"Ingrese el nombre del {x+1}° alumno del P2: ").title()
    parcial2.append(alumno_agregar)
parcial2 = set(parcial2)

aprobaron_ambos = parcial1 & parcial2
aprobaron_solo_uno = parcial1 ^ parcial2
aprobaron_al_menos_uno = parcial1 | parcial2

print(f"\nAlumnos que aprobaron ambos: {aprobaron_ambos}")
print(f"Alumnos que aprobaron solo uno: {aprobaron_solo_uno}")
print(f"Lista total (al menos uno): {aprobaron_al_menos_uno}")

# EJERCICIO 8:
"""Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""

stock_productos = {
    "fideos": 250,
    "aceite": 140,
    "gaseosa": 200
}


llave1 = "si"
while llave1 == "si":
    consultar_producto = str(input("Ingrese el producto por el cual desea consultar su stock: "))
    if consultar_producto in stock_productos:
        print  (f"{consultar_producto}: {stock_productos[consultar_producto]}")
    llave1 = str(input("Desea consultar por otro producto en especifico? (si/no): ").lower())

for i in range (len(stock_productos)):
    agregar_stock = str(input("Ingrese el nombre del producto del cual desea aumentar su stock. " \
    "O bien, ingrese el nombre del nuevo producto que desea agregar al stock: "))

    if agregar_stock in stock_productos:
        unidades_agregar = int(input("Ingrese la cantidad de unidades que desea agregar: "))
        stock_productos[agregar_stock] += (unidades_agregar)
        print (f"Se añadieron {unidades_agregar} unidades al stock del producto {agregar_stock}, \
               el mismo ahora cuenta con {stock_productos[agregar_stock]} unidades.")
    else: 
        unidades_agregar = int(input("Ha ingresado un nuevo producto, ingrese las unidades del mismo: "))
        stock_productos[agregar_stock] = (unidades_agregar)
        print (f"Se agregó el producto {agregar_stock} al stock, con: {unidades_agregar} unidades.")

# EJERCICIO 9:
agenda = {
    
}
llave9 = "si"   
while llave9 == "si":

    evento_agregar = str(input("Ingrese el nombre del evento: "))
    dia = str(input("Ingrese el dia del evento"))
    hora = str(input("Ingrese la hora del evento"))

    llave_tupla = (dia, hora)

    agenda[llave_tupla] = evento_agregar
    print("El evento fue agregado con exito a su agenda.")
    llave9 = str(input("Desea agregar otro evento a la agenda? (si/no): ").lower())
print ("------ AGENDA ------")
print (agenda)

# EJERCICIO 10:
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}
invertido = {}

for pais, capital in original.items():
        invertido[capital] = pais

print (original)
print (invertido)
