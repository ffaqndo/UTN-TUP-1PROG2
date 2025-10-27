# EJERCICIO 1:
with open("productos.txt", "w") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    archivo.write("lapicera,1500,10\n")
    archivo.write("cuaderno,4500,4\n")
    archivo.write("lapiz,900,25\n")

# EJERCICIO 2:
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        linea_split = linea_limpia.split(",")
        producto = linea_split[0]
        precio = linea_split[1]
        stock = linea_split[2]
        print (f"El producto '{producto}' tiene un costo de: ${precio} y hay disponibles {stock} unidades.")

# EJERCICIO 3:
with open("productos.txt", "a") as archivo:
    producto_agregar = str(input("Ingrese el nombre del producto que desea agregar: "))
    precio_agregar = int(input("Ingrese el precio del producto: "))
    stock_agregar = int(input("Ingrese la cantidad de unidades del producto: "))
    archivo.write(f"{producto_agregar},{precio_agregar},{stock_agregar}\n")

# EJERCICIO 4:
productos = []
with open("productos.txt", "r") as archivo:
    next(archivo)
    for linea in archivo:
        linea_split = linea.strip().split(",")
        producto_actual = {
            "nombre": (linea_split[0]).title(),
            "precio": (f"${linea_split[1]}"),
            "stock": (linea_split[2]),
        }
        productos.append(producto_actual)

    for i in range (len(productos)):
        print (productos[i])

# EJERCICIO 5: 
    llave5 = "si"
    encontrado = False
    while llave5 == "si":
        producto_averiguar = str(input("Ingrese el nombre del producto por el que desea consultar: ").title())
        for i in range (len(productos)):
            if producto_averiguar == productos[i]["nombre"]:
                print (productos[i])
                encontrado = True
        if encontrado == False:
            print ("El producto solicitado no se encuentra disponible")
        llave5 = str(input("Desea consultar por otro producto en especifico? (si/no): ").lower())

# EJERCICIO 6:
with open("productos.txt", "w") as archivo:
    
    archivo.write("nombre,precio,stock\n") 
    
    for i in range (len(productos)):
        producto = productos[i]
        precio_limpio = producto["precio"].replace('$', '')
        linea_csv = f"{producto['nombre']},{precio_limpio},{producto['stock']}\n"
        archivo.write(linea_csv)
