# Funciones para gestionar los paquetes turísticos
def crear_paquete(paquetes, nombre, descripcion, precio):
    paquete = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio
    }
    paquetes.append(paquete)
    print(f"Paquete '{nombre}' creado exitosamente.")

def buscar_paquete(paquetes, nombre):
    for paquete in paquetes:
        if paquete["nombre"] == nombre:
            return paquete
    return None

# Funciones para gestionar los clientes
def registrar_cliente(clientes, nombre, correo):
    cliente = {
        "nombre": nombre,
        "correo": correo,
        "reservas": []
    }
    clientes.append(cliente)
    print(f"Cliente '{nombre}' registrado.")

def buscar_cliente(clientes, nombre):
    for cliente in clientes:
        if cliente["nombre"] == nombre:
            return cliente
    return None



# Funciones para gestionar las reservas
def hacer_reserva(clientes, tipo, destino, fecha, nombre_cliente):
    cliente = buscar_cliente(clientes, nombre_cliente)
    if cliente:
        reserva = {
            "tipo": tipo,  # 'vuelo' o 'hotel'
            "destino": destino,
            "fecha": fecha,
        }
        cliente["reservas"].append(reserva)
        print(f"Reserva de {tipo} a {destino} creada para {cliente['nombre']}.")
    else:
        print(f"Cliente {nombre_cliente} no encontrado.")

# Menú interactivo
def mostrar_menu():
    print("\n--- Agencia de Viajes ---")
    print("1. Crear paquete turístico")
    print("2. Registrar cliente")
    print("3. Hacer reserva")
    print("4. Buscar cliente y mostrar reservas")
    print("5. Buscar paquete turístico")
    print("6. Salir")

#if __name__ == "__main__":
paquetes = []
clientes = []
    
while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paquete: ").strip()
            descripcion = input("Descripción del paquete: ").strip()
            precio = float(input("Precio del paquete: "))
            crear_paquete(paquetes, nombre, descripcion, precio)

        elif opcion == "2":
            nombre = input("Nombre del cliente: ").strip()
            correo = input("Correo del cliente: ")
            registrar_cliente(clientes, nombre, correo)

        elif opcion == "3":
            nombre_cliente = input("Nombre del cliente para la reserva: ").strip()
            tipo_reserva = input("Tipo de reserva (vuelo/hotel): ").strip()
            destino = input("Destino: ").strip()
            fecha = input("Fecha (YYYY-MM-DD): ").strip()
            hacer_reserva(clientes, tipo_reserva, destino, fecha, nombre_cliente)

        elif opcion == "4":
            nombre_cliente = input("Nombre del cliente: ").strip()
            cliente = buscar_cliente(clientes, nombre_cliente)
            if cliente:
                print(f"Cliente: {cliente['nombre']}, Correo: {cliente['correo']}")
                for reserva in cliente["reservas"]:
                    print(f"Reserva {reserva['tipo']} a {reserva['destino']} el {reserva['fecha']}")
            else:
                print("Cliente no encontrado.")

        elif opcion == "5":
            nombre_paquete = input("Nombre del paquete turístico: ")
            paquete = buscar_paquete(paquetes, nombre_paquete)
            if paquete:
                print(f"Paquete: {paquete['nombre']}, Descripción: {paquete['descripcion']}, Precio: {paquete['precio']}")
            else:
                print("Paquete no encontrado.")

        elif opcion == "6":
            print("Gracias por utilizar la Agencia de Viajes.")
            break

        else:
            print("Opción no válida, intenta nuevamente.")
   