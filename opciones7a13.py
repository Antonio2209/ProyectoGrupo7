elif opcion == "7":
        nombre_cliente = input("Nombre del cliente para eliminar la reserva: ").strip().lower()
        destino = input("Destino de la reserva a eliminar: ").strip()
        eliminar_reserva(clientes, nombre_cliente, destino)

    elif opcion == "8":
        nombre_paquete = input("Nombre del paquete a actualizar: ").strip().lower()
        descripcion = input("Nueva descripción (dejar vacío si no se actualiza): ").strip()
        precio = input("Nuevo precio (dejar vacío si no se actualiza): ").strip()
        actualizar_paquete(paquetes, nombre_paquete, descripcion, precio)

    elif opcion == "9":
        mostrar_paquetes(paquetes)

    elif opcion == "10":
        nombre_paquete = input("Nombre del paquete a eliminar: ").strip()
        eliminar_paquete(paquetes, nombre_paquete)

    elif opcion == "11":
        nombre_cliente = input("Nombre del cliente a actualizar: ").strip()
        nuevo_correo = input("Nuevo correo del cliente: ").strip()
        actualizar_cliente(clientes, nombre_cliente, nuevo_correo)

    elif opcion == "12":
        nombre_cliente = input("Nombre del cliente a eliminar: ").strip().lower()
        eliminar_cliente(clientes, nombre_cliente)

    elif opcion == "13":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Por favor, elige una opción correcta.")
