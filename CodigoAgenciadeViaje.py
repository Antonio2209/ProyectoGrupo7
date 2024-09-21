import re  #patron definido como la fecha
from datetime import datetime

#Diccionarios predefinidos
paquetes = {
    "aventura en la selva": {
        "nombre": "aventura en la selva",
        "descripcion": "Un paquete turístico que incluye senderismo y campamentos en la selva.",
        "precio": "500"
    },
    "escapada a la playa": {
        "nombre": "escapada a la playa",
        "descripcion": "Vacaciones relajantes en una playa paradisiaca con actividades acuáticas.",
        "precio": "800"
    },
    "tour histórico por europa": {
        "nombre": "Tour histórico por europa",
        "descripcion": "Un recorrido por las ciudades históricas más importantes de Europa.",
        "precio": "1500"
    }
}

clientes = {
    "juan perez": {
        "nombre": "juan perez",
        "correo": "juanperez@example.com",
        "reservas": [
            {
                "tipo": "vuelo",
                "destino": "cancun",
                "fecha": "2024-09-20"
            }
        ]
    },
    "maria gonzales": {
        "nombre": "maria gonzales",
        "correo": "mariagonalez@example.com",
        "reservas": [
            {
                "tipo": "hotel",
                "destino": "paris",
                "fecha": "2024-10-05"
            },
            {
                "tipo": "vuelo",
                "destino": "nueva york",
                "fecha": "2024-12-12"
            }
        ]
    },
    "carlos lopez": {
        "nombre": "carlos lopez",
        "correo": "carloslopez@example.com",
        "reservas": []
    }
}
#  hoteles predefinidos
hoteles = ["hotel paris", "resort playa", "hostal montaña", "hotel central City", "hotel luxor"]

# Funcion para gestionar los paquetes turísticos
def crear_paquete(paquetes, nombre, descripcion, precio):
    paquete = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio
    }
    if nombre in paquetes:
        print(f"El paquete '{nombre}' ya existe.")
    else:
        paquetes[nombre] = paquete
        print(f"Paquete '{nombre}' creado exitosamente.")

#funcion buscar paquetes
def buscar_paquete(paquetes, nombre):
    return paquetes.get(nombre, None)  #None=ausencia de valor o valor nulo.   .get=para buscar

#funcion actualizar paquetes
def actualizar_paquete(paquetes, nombre, descripcion=None, precio=None):
    if nombre in paquetes:
        if descripcion:
            paquetes[nombre]["descripcion"] = descripcion
        if precio:
            paquetes[nombre]["precio"] = precio
        print(f"Paquete '{nombre}' actualizado.")
    else:
        print(f"El paquete '{nombre}' no existe.")

#funcion eliminar paquetes
def eliminar_paquete(paquetes, nombre):
    if nombre in paquetes:
        del paquetes[nombre]
        print(f"Paquete '{nombre}' eliminado.")
    else:
        print(f"El paquete '{nombre}' no existe.")

#funcion mostrar paquetes
def mostrar_paquetes(paquetes):
    print("\n--- Paquetes Turísticos Disponibles ---")
    for paquete in paquetes.values():
        print(f"Nombre: {paquete['nombre']}, Descripción: {paquete['descripcion']}, Precio: {paquete['precio']}")

# Funciones para gestionar los clientes
def registrar_cliente(clientes, nombre, correo):
    cliente = {
        "nombre": nombre,
        "correo": correo,
        "reservas": []
    }
    if nombre in clientes:
        print(f"El cliente '{nombre}' ya está registrado.")
    else:
        clientes[nombre] = cliente
        print(f"Cliente '{nombre}' registrado.")

#funcion para buscar clientes
def buscar_cliente(clientes, nombre):
    nombre_normalizado = nombre.strip().lower()
    for nombre_cliente, datos_cliente in clientes.items():  #obtener clave,valor del diccionario
        if nombre_cliente.strip().lower() == nombre_normalizado:
            return datos_cliente
    return None

#funcion para actualizar clientes
def actualizar_cliente(clientes, nombre, correo=None):
    if nombre in clientes:
        if correo:
            clientes[nombre]["correo"] = correo
        print(f"Cliente '{nombre}' actualizado.")
    else:
        print(f"El cliente '{nombre}' no existe.")

#funcion para eliminar clientes
def eliminar_cliente(clientes, nombre):
    nombre_normalizado = nombre.strip().lower()  # Normalización del nombre
    cliente_encontrado = None
    for nombre_cliente, datos_cliente in list(clientes.items()):
        if nombre_cliente.strip().lower() == nombre_normalizado:
            cliente_encontrado = nombre_cliente
            break
    
    if cliente_encontrado:
        del clientes[cliente_encontrado]
        print(f"Cliente '{cliente_encontrado}' eliminado.")
    else:
        print(f"El cliente '{nombre}' no fue encontrado.")

# Funciones para gestionar las reservas
def hacer_reserva(clientes, tipo, destino, fecha, nombre_cliente):
    cliente = buscar_cliente(clientes, nombre_cliente)
    if cliente:
        reserva = {
            "tipo": tipo,
            "destino": destino,
            "fecha": fecha,
        }
        cliente["reservas"].append(reserva)
        print(f"Reserva de {tipo} a {destino} creada para {cliente['nombre']}.")
    else:
        print(f"Cliente {nombre_cliente} no encontrado.")

#funcion mostrar reservas
def mostrar_todas_reservas(clientes):
    print("\n--- Todas las reservas ---")
    for nombre_cliente, cliente in clientes.items():
        if cliente["reservas"]:
            print(f"Reservas de {cliente['nombre']}:")
            for reserva in cliente["reservas"]:
                print(f"- {reserva['tipo']} a {reserva['destino']} el {reserva['fecha']}")
        else:
            print(f"{cliente['nombre']} no tiene reservas.")

#funcion eliminar reservas
def eliminar_reserva(clientes, nombre_cliente, destino):
    cliente = buscar_cliente(clientes, nombre_cliente)
    if cliente:
        reservas = cliente["reservas"]
        for reserva in reservas:
            if reserva["destino"] == destino:
                reservas.remove(reserva) #remover o borrar
                print(f"Reserva a {destino} eliminada para {cliente['nombre']}.")
                return
        print(f"No se encontró una reserva a {destino} para {cliente['nombre']}.")
    else:
        print(f"Cliente {nombre_cliente} no encontrado.")

# Mostrar lista de hoteles como menú
def seleccionar_hotel():
    print("\n--- Opciones de Hospedaje ---")
    for i, hotel in enumerate(hoteles, 1):
        print(f"{i}. {hotel}")
    opcion = input("Elige una opción de hotel: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= len(hoteles)):  #opcion.isdigit  verifica si la cadena opcion contiene solo dígitos
        print("Opción inválida, intenta de nuevo.")                        #1 <= int(opcion) <= len(hoteles) comprueba si el número ingresado 
        opcion = input("Elige una opción de hotel: ")                      #está dentro del rango válido, es decir, entre 1 y la longitud de la lista hoteles
    return hoteles[int(opcion) - 1]

# Validar formato de fecha
def validar_fecha(fecha):
    try:
        # Intentamos convertir la cadena de fecha a un objeto datetime
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        # Si ocurre un error, significa que el formato es incorrecto
        return False
    
# Menú interactivo
def mostrar_menu():
    print("\n--- Agencia de Viajes Indiana ---")
    print("1. Crear paquete turístico")
    print("2. Registrar cliente")
    print("3. Hacer reserva")
    print("4. Buscar cliente y mostrar reservas")
    print("5. Buscar paquete turístico")
    print("6. Mostrar todas las reservas")
    print("7. Eliminar reserva")
    print("8. Actualizar paquete turístico")
    print("9. Mostrar paquetes turísticos")
    print("10. Eliminar paquete turístico")
    print("11. Actualizar cliente")
    print("12. Eliminar cliente")
    print("13. Salir")

# Bucle del menú 
while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")
#Creacion del paquete
    if opcion == "1":
        while True:
            nombre = input("Nombre del paquete: ").strip().lower()                         #c.isalpha() verifica si el carácter c es una letra
            if all(c.isalpha() or c.isspace() for c in nombre) and len(nombre) > 0:        #c.isspace() verifica si el carácter c es un espacio en blanco
                break                                                                      #len(nombre) > 0: comprueba que la longitud sea mayor que 0, que no esté vacía. 
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")    
        
        descripcion = input("Descripción del paquete: ").strip()
        precio = input("Precio del paquete: ").strip()
        while not precio.replace('.', '', 1).isdigit():                                    #replace('.', '', 1):elimina el primer punto (.) en la cadena precio. decimal valido
            print("Por favor, ingrese un precio válido.")
            precio = input("Precio del paquete: ").strip()
        crear_paquete(paquetes, nombre, descripcion, precio)

#Registrar Clientes
    elif opcion == "2":
        while True:
            nombre = input("Nombre del cliente: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre) and len(nombre) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        
        while True:
            correo = input("Correo del cliente: ").strip()
            if "@" in correo:
                break
            print("Error: El correo debe contener '@'.")
        
        registrar_cliente(clientes, nombre, correo)

#Hacer Recerva
    elif opcion == "3":
        while True:
            nombre_cliente = input("Nombre del cliente: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_cliente) and len(nombre_cliente) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        while True:
            tipo_reserva = input("Tipo de reserva (vuelo/hotel): ").strip().lower()
            if tipo_reserva not in ["vuelo", "hotel"]:
                    print("Error: El tipo de reserva debe ser 'vuelo' o 'hotel'.")
            else:
                    destino = seleccionar_hotel() if tipo_reserva == "hotel"  else input("Destino: ").strip().lower()
                    break
            
        while True:
            fecha = input("Fecha (YYYY-MM-DD): ").strip()
    
            if validar_fecha(fecha):
                print(f"El formato {fecha} de la fecha es correcto.")
        # Si la fecha es válida, romper el bucle y proceder con la reserva
                break
            else:
                print("Error: El formato de la fecha es incorrecto. Intente de nuevo (formato YYYY-MM-DD).")

# Llamada a la función de reserva (aquí ya estarías fuera del bucle)
        hacer_reserva(clientes, tipo_reserva, destino, fecha, nombre_cliente)

    elif opcion == "4":
        while True:
            nombre_cliente = input("Nombre del cliente para buscar: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_cliente) and len(nombre_cliente) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        cliente = buscar_cliente(clientes, nombre_cliente)
        if cliente:
            print(f"Cliente: {cliente['nombre']}, Correo: {cliente['correo']}")
            for reserva in cliente["reservas"]:
                print(f"Reserva {reserva['tipo']} a {reserva['destino']} en {reserva['fecha']}")
        else:
            print(f"Cliente {nombre_cliente} no encontrado.")


#Buscar Paquete
    elif opcion == "5":
        while True:
            nombre_paquete = input("Nombre del paquete: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_paquete) and len(nombre_paquete) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        paquete = buscar_paquete(paquetes, nombre_paquete)
        if paquete:
            print(f"Nombre: {paquete['nombre']}, Descripción: {paquete['descripcion']}, Precio: {paquete['precio']}")
        else:
            print(f"Paquete {nombre_paquete} no encontrado.")

    elif opcion == "6":
        mostrar_todas_reservas(clientes)

#Eliminar Recerva
    elif opcion == "7":
        while True:
            nombre_cliente = input("Nombre del cliente: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_cliente) and len(nombre_cliente) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        while True:
            destino = input("Nombre del destino a eliminar: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in destino) and len(destino) > 0:
                break
            print("Error: El nombre del destino debe contener solo letras y no puede estar vacío.")
        eliminar_reserva(clientes, nombre_cliente, destino)

#actualizar paquete
    elif opcion == "8":
        while True:
            nombre_paquete = input("Nombre del a paquete a actualizar: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_paquete) and len(nombre_paquete) > 0:
                break
            print("Error: El paquete debe contener solo letras y no puede estar vacío.")
        descripcion = input("Nueva descripción (dejar vacío si no se actualiza): ").strip()
        precio = input("Nuevo precio (dejar vacío si no se actualiza): ").strip()
        while not precio.replace('.', '', 1).isdigit():
            print("Por favor, ingrese un precio válido.")
            precio = input("Precio del paquete: ").strip()
        actualizar_paquete(paquetes, nombre_paquete, descripcion, precio)

    elif opcion == "9":
        mostrar_paquetes(paquetes)

#eliminar paquete
    elif opcion == "10":
        while True:
            nombre_paquete = input("Nombre del paquete a eliminar: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_paquete) and len(nombre_paquete) > 0:
                break
            print("Error: El nombre del paquete debe contener solo letras y no puede estar vacío.")
        eliminar_paquete(paquetes, nombre_paquete)

#Actualizar cliente
    elif opcion == "11":
        while True:
            nombre_cliente = input("Nombre del cliente para actualizar datos: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_cliente) and len(nombre_cliente) > 0:
                break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        while True:
            nuevo_correo = input("Nuevo correo del cliente para actualizar: ").strip()
            if "@" in nuevo_correo:
                break
            print("Error: El correo debe contener '@'.")
        actualizar_cliente(clientes, nombre_cliente, nuevo_correo)

#Eliminar cliente
    elif opcion == "12":
        while True:
            nombre_cliente = input("Nombre del cliente a eliminar: ").strip().lower()
            if all(c.isalpha() or c.isspace() for c in nombre_cliente) and len(nombre_cliente) > 0:
                    break
            print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        eliminar_cliente(clientes, nombre_cliente)

    elif opcion == "13":
        print("Gracias por utilizar nuestra Agencia de Viajes Indiana. Saliento...")
        break

    else:
        print("Opción no válida. Por favor, elige una opción correcta.")
