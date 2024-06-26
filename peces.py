import os
import pyfiglet
from datetime import datetime


#  día/mes/año
now = datetime.now()
formato_fecha = now.strftime("%d-%m-%Y")
# Lista de productos
productos = [
    # ID, Producto, Género, Stock, Precio   
]
# Lista de ventas
ventas = [
     #Folio     #Fecha    #ID   #Cantidad     #Total    
]
ventas_fecha = [
     #Folio     #Fecha    #ID   #Cantidad     #Total
]
#ELIMINAR FUNCION DIRECTA DEL TXT Y AGREGAR LISTA NUEVA PARA AGREGAR AL TXT Y QUE EL CAJERO NUEVO PUEDA CARGAR TODOS LOS PRODUCTOS NUEVOS

lista_productos_nueva = [

]

lista_ventas_nueva = [

]

# ingresa los productos agregados al archivo #

def guardar_productos(archivo):
    with open(archivo, "w") as file:
        for producto in productos:
            linea = ','.join(map(str, producto))
            file.write(linea + '\n')

# Ingresa la venta al archivo txt #

def guardar_ventas(archivo):
    with open(archivo, "w") as file:
        for venta in ventas:
            linea = ','.join(map(str, venta))
            file.write(linea + '\n')

# Verifica stock y entrega valor total

def pantalla_carga():
    os.system("cls")
    print(pyfiglet.figlet_format("Venta de peces"))
    print("                                                     integrantes:  Sara Carvajal")
    print("                                                                   Jassack Mendoza")

def cargar_productos(archivo):
    productos.clear()
    with open(archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            if not linea:
                continue
            datos = linea.split(',')
            if len(datos) < 5:
                print(f"Línea con formato incorrecto: {linea}")
                continue
            try:
                id_producto = int(datos[0])
                nombre_producto = datos[1]
                genero_producto = datos[2]
                stock_producto = int(datos[3])
                precio_producto = int(datos[4])
                productos.append([id_producto, nombre_producto, genero_producto, stock_producto, precio_producto])
            except ValueError as e:
                print(f"Error de valor en la línea: {linea} -> {e}")



def cargar_ventas(archivo):
    with open(archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            if not linea:  # Ignorar líneas vacías
                continue
            datos = linea.split(',')
            if len(datos) < 5:  # Verificar que la línea tenga al menos 5 elementos
                print(f"Línea con formato incorrecto: {linea}")
                continue
            try:
                folio = int(datos[0])
                fecha = datos[1]
                id_producto = datos[2]
                if len(datos) == 5:
                    stock_vendido = int(datos[-2])
                    precio_producto = int(datos[-1])
                    ventas.append([folio, fecha, id_producto, stock_vendido, precio_producto])
            except ValueError as e:
                print(f"Error de valor en la línea: {linea} -> {e}")
    


# Definir las variables globales


carga_prod_vent = 0
carga_archivos_txt = 0
def cargar_datos(tipo_de_dato):
    global carga_prod_vent, carga_archivos_txt, folio
    ingreso_cajero()
    try:
        if tipo_de_dato == 1:
            
            if carga_prod_vent == 0:
                print("carga 1")
                cargar_productos("productos.txt")
                cargar_ventas('ventas.txt')
                print("Datos cargados correctamente.")
                os.system("pause")
                carga_prod_vent = 1
                folio = get_folio()
            else:
                print("Los productos ya fueron cargados previamente")
                os.system("pause")

                    
        elif tipo_de_dato == 2:
            if carga_archivos_txt == 0:
                for producto in productos:
                    print(producto)
                    guardar_productos("productos.txt")
                for venta in ventas:
                    guardar_ventas("ventas.txt")
                carga_archivos_txt = 1
                print("Archivos guardados correctamente.")
                os.system("pause")
            else:
                print("Los archivos ya han sido guardados previamente.")
                os.system("pause")
    except Exception as e:
        print(f"Error: {e}")

def ingreso_cajero():

    os.system("cls")

    try:
        cajero = input("Ingresa tu numero de cajero: ")
        cajero = int(cajero)

        if cajero == 1234:
            print("Cajero autenticado y listo para cargar datos.")
            print("CARGANDO DATOS...")
            os.system("pause")
            

        else:
            print("Cajero no autorizado.")
    except:
        print("Error, ingreso no valido")


#DEJAR BONITO 

def mostrar_tabla_ventas():
                       #0       #1      #2      #3         #4
    tabla_ventas = [["FOLIO", "Fecha", "ID", "Cantidad", "Total"]]
                       #-5      #-4     #-3     #-2        #-1
        #lo que se obtiene
    for venta in ventas:
            # de donde se obtiene
        folio = venta[0]
        fecha = venta[1]
        id = venta[2]
        cantidad = venta[3]
        total = venta[4]
        fila = [folio, fecha, id, cantidad, total]
        tabla_ventas.append(fila)

    col_widths = [max(len(str(value)) for value in column) for column in zip(*tabla_ventas)]
    separador = "-+-".join('-' * width for width in col_widths)

    for i, row in enumerate(tabla_ventas):
        print(" | ".join(f"{str(value).ljust(width)}" for value, width in zip(row, col_widths)))
        if i == 0:
            print(separador)


# obtener el ultimo folio 

def get_folio():
    if len(ventas) == 0:
        os.system("cls")
        print("Debe cargar los productos!")
    else:

        elemento= len(ventas)-1
        return (ventas[elemento])[0]


# ingresa folio nuevo con id, desde la ultima encontrada

def ingresar_folio(fecha, id, c_items, total_productos):
    folio = get_folio()+1
    nuevo_folio = [folio, fecha, id, c_items , total_productos]
    ventas.append(nuevo_folio)
    print('folio asignado con el numero: ',get_folio())

# Busca un producto por ID en la lista 

def buscar_producto_por_id(id_producto):
    
    for producto in productos:
        if producto[0] == id_producto:
            return producto
    return None


# Muestra la informacion del producto

def mostrar_producto(producto):
    
    if producto:
        print("\nID: ", producto[0])
        print("NOMBRE:", producto[1])
        print("GENERO:", producto[2] if len(producto) == 5 else "")
        print("STOCK:", producto[-2])
        print("PRECIO:", producto[-1])

# Muestra una tabla con todos los productos

def mostrar_tabla_productos():
    
    tabla_productos = [["ID", "Producto", "Género", "Stock", "Precio"]]
    for producto in productos:
        id_producto = producto[0]
        nombre_producto = producto[1]
        genero_producto = producto[2] if len(producto) == 5 else ""
        stock_producto = producto[-2]
        precio_producto = producto[-1]
        fila = [id_producto, nombre_producto, genero_producto, stock_producto, precio_producto]
        tabla_productos.append(fila)

    col_widths = [max(len(str(value)) for value in column) for column in zip(*tabla_productos)]
    separador = "-+-".join('-' * width for width in col_widths)

    for i, row in enumerate(tabla_productos):
        print(" | ".join(f"{str(value).ljust(width)}" for value, width in zip(row, col_widths)))
        if i == 0:
            print(separador)


# Verifica stock y entrega valor total

def procesar_venta(id_producto):
    producto = buscar_producto_por_id(id_producto)
    if producto:
        mostrar_producto(producto)
        c_items = int(input('¿Cuántos productos desea? '))
        if c_items > 0 and producto[-2] > c_items:
            valor = producto[-1] * c_items
            print('\nSu valor total por esta venta es de: ', valor)
            producto[-2] -= c_items  # Actualizar el stock
            agregar_carrito(valor)
            ingresar_folio(formato_fecha, id_producto, c_items, valor)
             # Guardar cambios en el archivo
                       #MODIFICAR RANGO DE MARGEN EN INGRESO DE ARCHIVOS AL TXT, NO DEBE GRABAR SI LA OPCION ES N
        else:
            print('No disponemos de esa cantidad de items.')
            print('Ingresa una cantidad menor a ', producto[-2]) 
    else:
        print("Producto no encontrado")

carrito_final = 0


def agregar_carrito(valor):
    global carrito_final
    carrito_final += valor
    print(f'Su carrito es de: {carrito_final}')

    if valor ==0:
        return valor


def ultimo_id():
    for producto in productos:
        id_producto = producto[0]+1

    return id_producto 


# Busca un producto y lo elimina por su ID

def eliminar_producto(id_producto):
    producto = buscar_producto_por_id(id_producto)
    if producto:
        productos.remove(producto)
        print("Producto eliminado")
        reasignacion_id()
        
    else:
        print("Producto no encontrado")

# Al eliminar un producto este leera las id, y si estas no corresponden al largo de la lista las reasignara desde 1 hasta el largo que tenga la lista

def reasignacion_id():
    nuevo_id = 1
    for producto in productos:
        id_producto = int(producto[0])
    if len(productos) < id_producto:
        print('Reasignando IDs!')
        for producto in productos:
            producto[0] = nuevo_id  # Asigna nueva ID
            nuevo_id += 1
            
    else:
        print('Sin novedades')

# Agrega un nuevo producto a la lista, este debera ingresarlo el usuario mediante diferentes preguntas
        """ agregar opcion de producto nuevo o ya existente  [ Agregado :) ] """ 
def agregar_producto():
    resp = input('El producto que se ingresara es uno existente? [S]/[N]: ')
    if resp.lower()=='s':
        try:
            id_producto = int(input('Ingrese el ID del producto: '))
            producto = buscar_producto_por_id(id_producto)
            if producto:
                mostrar_producto(producto)
                c_items = int(input('¿Cuántos productos desea agregar? '))
                producto[-2]=producto[-2]+c_items
                mostrar_producto(producto)
                print('Agregado con exito!')
                os.system('pause')

        except ValueError:
            print('Entrada no válida. Por favor, ingrese los datos correctamente.')

    elif resp.lower() == 'n':
        try:
            id_producto = ultimo_id()
            nombre_producto = input('Ingrese el nombre del producto: ')
            if nombre_producto.isnumeric():
                print('El nombre del producto no debe ser  numérico.')
                os.system("pause")
                return
            genero_producto = input('Ingrese el género del producto (opcional): ')
            if genero_producto and genero_producto.isnumeric():
                print('El género del producto no debe ser completamente numérico.')
                os.system("pause")
                return
            stock_producto = int(input('Ingrese el stock del producto: '))
            precio_producto = int(input('Ingrese el precio del producto: '))
            nuevo_producto = [id_producto, nombre_producto, genero_producto, stock_producto, precio_producto]
            productos.append(nuevo_producto)
            print('Producto agregado exitosamente.')
        except ValueError:
            print('Entrada no válida. Por favor, ingrese los datos correctamente.')
        os.system('pause')

def mostrar_tabla_ventas_fecha(ventas):
    total = 0
    tabla_ventas = [["FOLIO", "Fecha", "ID", "Cantidad", "Total"]]
    for venta in ventas:
        fila = [venta[0], venta[1], venta[2], venta[3], venta[4]]
        tabla_ventas.append(fila)
        total = total + venta[-1]
    
    col_widths = [max(len(str(value)) for value in column) for column in zip(*tabla_ventas)]
    separador = "-+-".join('-' * width for width in col_widths)

    for i, row in enumerate(tabla_ventas):
        print(" | ".join(f"{str(value).ljust(width)}" for value, width in zip(row, col_widths)))
        if i == 0:
            print(separador)

    print('El total de las fechas listadas es de: ', total    )




# Para agregarla se debe ingresar el valor de 1/2/3 , siendo 1 para fecha unica, 2 para rango de fechas y 3 para todas las fechas

def obtener_fecha(c_fechas):
    os.system('cls')
    total=0

    try:
        if c_fechas == 1:
            for venta in ventas:
                total=total+venta[-1]
            mostrar_tabla_ventas()
            print(f'\nSu total de ventas dan un total de: {total}')
        
        if c_fechas == 2:
            fecha_inicio = input('Ingresa la fecha inicial con el formato [DD-MM-AAAA]: ')
            fecha_termino = input('Ingresa la fecha de termino con el formato [DD-MM-AAAA]: ')
            fecha_inicio_dt = datetime.strptime(fecha_inicio, '%d-%m-%Y')
            fecha_termino_dt = datetime.strptime(fecha_termino, '%d-%m-%Y')
            
            for venta in ventas:
                fecha_venta_dt = datetime.strptime(venta[1], '%d-%m-%Y')
                if fecha_inicio_dt <= fecha_venta_dt <= fecha_termino_dt:
                    ventas_fecha.append(venta)

            if ventas_fecha:
                mostrar_tabla_ventas_fecha(ventas_fecha)

            else:
                print("No hay datos que mostrar")

                
            
        elif c_fechas ==3:
            fecha_inicio = input('Ingrese la fecha con el siguiente formato [dd-mm-aaaa]: ')
            for venta in ventas:
                if venta[1] == fecha_inicio:
                    total=total+venta[-1]
                    print(venta[0],' ',venta[1],' ', venta[2],' ', venta[-2],' ',venta[-1])

            else:
                print("No hay datos que mostrar")
            print(f'El total de ventas en la fecha solicitada es de {total}')

    except:
        print('Rangos no validos') 

folio = 10000

opcion = 0
pantalla_carga()
os.system("pause")

while opcion != 5:
    # Menú principal
    os.system("cls")
    print(f'''
    
    ¡Bienvenido a Pecezuelos!          {formato_fecha}     V: 002                  
    ¿Qué deseas hacer?              {folio}
                                        

    1. Vender productos
    2. Reportes
    3. Mantenedor
    4. Menu administrador
    5. Salir
    ''')
    try:
        opcion = int(input("  Ingresa una opción: "))
        if opcion == 1:
            # Menú de ventas
            nueva_venta = 0
            while nueva_venta == 0:
                os.system("cls")
                print('''
                    ¡Bienvenido a Pecezuelos!
                    ¿Qué deseas comprar?
                \n''')
                mostrar_tabla_productos()
                
                try:
                    if nueva_venta == 0:
                        nueva_venta = "s"
                        while True:
                            if nueva_venta.lower() == "s" :
                                os.system('cls')
                                mostrar_tabla_productos()
                                ingreso_id = int(input("\nIngrese el ID del producto: "))
                                procesar_venta(ingreso_id)
                                nueva_venta = input("¿Desea una nueva venta? [S]/[N] : ")
                                if nueva_venta.lower() == 'n':
                                    agregar_carrito(0)
                            else:
                                nueva_venta = 1
                                break
                    else:
                        break
                except ValueError:
                    nueva_venta = 0
                    print("Error, rango no válido")
                    
                    
                os.system("pause")

        elif opcion == 2:
            # menu para sistema de reportes
        
            while True:
                os.system("cls")
                print('''
                            REPORTES
    -------------------------------------------------------------------
                1. General de ventas(con total)
                2. Ventas por fecha especifica(con total)
                3. Ventas por rango de fecha (con total)
                4. Volver al menú principal
                                
''')

                op=int(input("Ingrese una opcion 1-4: "))
                match op:
                    case 1: #listar como el de productos
                        obtener_fecha(1)
                        os.system("pause")
                    case 2: #ventas : ventas [1]
                        obtener_fecha(3)
                        os.system("pause")
                    case 3: #validar rango de fechas ingresadas por el usuario
                        obtener_fecha(2)
                        os.system("pause")
                    case 4: #volver al menu
                        break

        elif opcion == 3:
            while True:
                os.system('cls')
                print('''
                            MANTENEDOR
        ------------------------------------------------------
                    1. Agregar Productos
                    2. Quitar Productos
                    3. Listar Productos
                    4. Volver al menú principal
                    
\n''')
                try:
                    opc_adm = int(input('Ingrese una opción: '))
                    if opc_adm == 1:
                        agregar_producto()

                    elif opc_adm == 2:
                        os.system('cls')
                        id_ingresada = int(input("Ingresa el ID del producto a eliminar: "))
                        mostrar_producto(buscar_producto_por_id(id_ingresada))
                        opc_eliminar = input('\n¿Estás seguro que deseas eliminar el producto [S]/[N]: ')
                        # AGREGAR OPCION PARA ELIMINAR CANTIDAD ESPECIFICA
                        if opc_eliminar.lower() == 's':
                            eliminar_producto(id_ingresada)
                        else:
                            print('Cancelando...')
                        os.system("pause")

                    elif opc_adm == 3:
                        os.system("cls")
                        print('\nOpción 3: Listar Productos')
                        mostrar_tabla_productos()
                        os.system("pause")

                    elif opc_adm ==4:
                        break

                    else:
                        print("Opción no válida")
                        os.system("pause")

                except ValueError:
                    print("Error, rango no válido")
                    os.system("pause")

        elif opcion == 4:
            while True:
                os.system('cls')
                print('''
                            MENU ADMINISTRACION
        ------------------------------------------------------
                    1. Cargar Datos
                    2. Respaldar Datos (Grabar / Actualizar)
                    3. Salir
                    
\n''')
                try:
                    opc_adm = int(input('Ingrese una opción: '))
                    if opc_adm == 1:
                        cargar_datos(1)

                    elif opc_adm ==2:
                        cargar_datos(2)

                    else:
                        break

                except ValueError:
                    print("Error, rango no válido")
                    os.system("pause")

        elif opcion == 5:
            print("Saliendo...")
    except ValueError:
        print("Error, rango no válido")
        os.system("pause")

print("Adiós")




