import funciones

sectores_hoja_ruta = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]
datos_cliente = []

flag = True

while flag:

    opcion = funciones.menu()

    if opcion == 1: #registrar pedido
        funciones.registrar_pedido(datos_cliente)

    elif opcion == 2: # listar pedido
        funciones.listar_pedido(datos_cliente)

    elif opcion == 3: # imprimir hoja de ruta
        sector = input("comuna: ")
        funciones.hoja_ruta(datos_cliente,sector)

    elif opcion == 4: # buscar pedido por id
        funciones.buscar_id(datos_cliente)

    elif opcion == 5: # salir del programa
        flag = False