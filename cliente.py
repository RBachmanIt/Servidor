#!/usr/bin/python
# -*- coding: utf-8 -*-
# Programa Cliente

import socket
import sys

if len(sys.argv) != 3:
    print ("Agregar la IP del servidor y el puerto donde se ofrece el servicio.")
    sys.exit(0)

IP = sys.argv[1]
PUERTO = int(sys.argv[2])

print ("\nConectandose al servidor ", IP, " en el puerto ", PUERTO, " ...")

try:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((IP, PUERTO))
except:
    print ("No se puede conectar con el servidor.")
    sys.exit(0)
print("\n*********************************************************************")
print ("Conectado, escriba finalizar() para terminar la conección.")
print ("Bienvenido al conversor de temperatura")
print ("Donde se define K = Kelvin, C = Celsius, F = Fahrenheit")
print ("Para el ingreso de numeros con decimales, debe ir un 'punto' entre ellos")
print ("Ingrese los datos de la forma '180 C K'")
print ("O de la forma '180.000 C K'")
print ("Donde se transformara desde 180 grados celsius a kelvin")
print("***********************************************************************")

try:
    while True:
        mensaje = str(raw_input("Yo >> "))
        #Por si se ingresa solo enter, se enviara un espacio en blanco
        if mensaje == "":
            mensaje= " "
        socket_cliente.send(mensaje.encode("utf-8"))
        if mensaje == "finalizar()":
            break
        recibido = socket_cliente.recv(1024)
        print ("Servidor >> " + recibido)

except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrunpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.")
