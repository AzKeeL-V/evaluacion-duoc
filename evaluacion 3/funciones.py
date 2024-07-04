import config as con
import random
import csv
import os

def menu():
    opcion = 1
    for elemento in con.menu:
        print(f"{opcion}. {elemento}")
        opcion += 1
    flag = True

    while flag:

        try :
            seleccion = int(input("ingresa la opcion deseada: "))
            flag = False
        except:
            print("error escoge una opcion correcta")
    return seleccion   

def registrar_pedido(lista):
    cantidad_cilindro_6litros = 0
    cantidad_cilindro_10litros = 0
    cantidad_cilindro_20litros = 0

    idpedido = random.randint(999,999999)
    while True:
        nombre = input("nombre: ")
        if nombre.isalpha:
            break
        else:
            print("error")
    while True:    
        apellido = input("apellido: ")
        if apellido.isalpha:
            break
        else:
            print("error")
    while True:    
        direccion = input("direccion: ")
        if direccion.isalnum:
            break
        else:
            print("agrega todos los datos solicitados")

    comuna = input("comuna: ")
    while True:
        try:
            tipo_cilindro = int(input("tenemos disponibles cilindros de 6, 10 y 20 litros. cual necesitas?: "))
            if tipo_cilindro == 6 or tipo_cilindro == 10 or tipo_cilindro == 20:
                break
        except:
            print("solo tenemos disponibles cilindros de 6, 10 y 20 litros")

    if tipo_cilindro == 6:
        while True:
            try:
                cantidad_cilindro_6litros = int(input("ingresa la cantidad de cilindros de 6 litros: "))
                if cantidad_cilindro_6litros > 0:
                    break
            except:
                print("ingresa la cantidad")
    elif tipo_cilindro == 10:
        while True:
            try:
                cantidad_cilindro_10litros = int(input("ingresa la cantidad de cilindros de 10 litros: "))
                if cantidad_cilindro_10litros > 0:
                    break
            except:
                print("ingresa la cantidad")

    elif tipo_cilindro == 20:        
        while True:
            try:
                cantidad_cilindro_20litros = int(input("ingresa la cantidad de cilindros de 6 litros: "))
                if cantidad_cilindro_20litros > 0:
                    break
            except:
                print("ingresa la cantidad")
       

    datos_cliente = ([idpedido, nombre, apellido,direccion, comuna, cantidad_cilindro_6litros, cantidad_cilindro_10litros, cantidad_cilindro_20litros])
    print("ID\tCLIENTE   \t  DIRECCION\tSECTOR\tDISP.6LTS\tDISP.10LTS\tDISP.20LTS")
    print(f"{idpedido}  {nombre,apellido}   {direccion}    {comuna}     {cantidad_cilindro_6litros}  {cantidad_cilindro_10litros}  {cantidad_cilindro_20litros}")


    lista.append(datos_cliente)    

def listar_pedido(lista):
    print("ID\tCLIENTE\tDIRECCION\tSECTOR    \tDISP.6LTS DISP.10LTS DISP.20LTS")
    for cliente in lista:
        print(cliente)


def hoja_ruta(lista,sectores):
    with open("hojaruta.csv", "w", newline="")as archivo:
        escritor = csv.writer(archivo)
        if sectores == "concepcion":
            for sectores in lista:
             escritor.writerow(sectores)


def buscar_id(lista):
    id = input("id a buscar: ")
    for codigo in lista:
        for id in codigo:
            if id == codigo:
             print(codigo)

