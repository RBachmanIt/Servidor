#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa Servidor

import socket
import sys

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio.")
    sys.exit(0)

IP = ""
PUERTO = int(sys.argv[1])

print ("\nServicio se va a configurar en el puerto: ", PUERTO, " ...")

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket con la IP y el puerto
socket_servidor.bind((IP, PUERTO))

# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
socket_servidor.listen(1)

print ("Servicio configurado.\n")

try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto socket_cliente para recibir datos,
        # direccion_cliente recibe la tupla de conexion: IP y puerto
        socket_cliente, direccion_cliente = socket_servidor.accept()
        print ("Cliente conectado desde: ", direccion_cliente)

        while True:
            try:
                #falta que con coma tire un mensaje de error
                recibido = socket_cliente.recv(1024)
                print (str(direccion_cliente[0]) + " >> ", recibido)
                variables = recibido.split()
                resultado = " "
                resultado2 = " "
                resultado3 = " "
                error = False

                #for para capturar error cuando se ingresa espacios en blanco
                j = [" "]
                i=0
                for i in range(512):
                    if recibido == "" or recibido == j[i]:
                        variables.append("errores")
                        variables.append("errores")
                    j.append(j[i]+" ")
                    i=i+1
                #try para verificar que la variable sea de tipo float
                try:
                    float(variables[0])
                except ValueError:
                    variables.append("errores")
                    variables.append("errores")
                    variables[1]="error"
                    error = True
                #si la cadena ingresada no se puede separar por espacios en blancos
                if len(variables)==1:
                    variables.append("errores")
                #finalizar la coneccion
                if recibido == "finalizar()":
                    print ("Cliente finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    socket_cliente.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                #Para cuando se quiere transformar desde grados Celsius
                elif variables[1] == "C" or variables[1] == "c":
                    if variables[2] == "K" or variables[2] == "k":
                        resultado = float(variables[0]) + 273.15
                        resultado3 = "Kelvin"
                    elif variables[2] == "F" or variables[2] == "f":
                        resultado = float(variables[0])*9/5 + 32
                        resultado3 = "Fahrenheit"
                    elif variables[2] == "C" or variables[2] == "c":
                        resultado = float(variables[0])
                        resultado3 = "Celsius"
                    else:
                        if error == True:
                            resultado = "Ha ingresado el valor de forma incorrecta, pruebe de la forma 10 o 100.0"
                        elif variables[2] != "K" and variables[2] != "k" and variables[2] != "F" and variables[2] != "f" and variables[2] != "C" and variables[2] != "c":
                            resultado3 = "Ha ingresado el tipo de temperatura de forma incorrecta, pruebe K o F"
                #Para cuando se quiere transformar desde grados Kelvin
                elif variables[1] == "K" or variables[1] == "k":
                    if variables[2] == "C" or variables[2] == "c":
                        resultado = float(variables[0]) - 273.15
                        resultado3 = "Celsius"
                    if variables[2] == "F" or variables[2] == "f":
                        resultado = (float(variables[0])-273.15) * 9/5 + 32
                        resultado3 = "Fahrenheit"
                    if variables[2] == "K" or variables[2] == "k":
                        resultado = float(variables[0])
                        resultado3 = "Kelvin"
                    else:
                        if error == True:
                            resultado = "Ha ingresado el valor de forma incorrecta, pruebe de la forma 10 o 100.0"
                        elif variables[2] != "C" and variables[2] != "c" and variables[2] != "F" and variables[2] != "f" and variables[2] != "K" and variables[2] != "k":
                            resultado3 = "Ha ingresado el tipo de temperatura de forma incorrecta, pruebe C o F"
                #Para cuando se quiere transformar desde grados Fahrenheit
                elif variables[1] == "F" or variables[1] == "f":
                    if variables[2] == "C" or variables[2] == "c":
                        resultado = (float(variables[0]) - 32)*5/9
                        resultado3 = "Celsius"
                    if variables[2] == "K" or variables[2] == "k":
                        resultado = (float(variables[0]) - 32)* 5/9 + 273.15
                        resultado3 = "Kelvin"
                    if variables[2] == "F" or variables[2] == "f":
                        resultado = float(variables[0])
                        resultado3 = "Fahrenheit"
                    else:
                        if error == True:
                            resultado = "Ha ingresado el valor de forma incorrecta, pruebe de la forma 10 o 100.0"
                        elif variables[2] != "K" and variables[2] != "k" and variables[2] != "C" and variables[2] != "c" and variables[2] != "F" and variables[2] != "f":
                            resultado3 = "Ha ingresado el tipo de temperatura de forma incorrecta, pruebe K o C"
                elif variables[1] != "C" and variables[1] != "c" and variables[1] != "K" and variables[1] != "k" and variables[1] != "F" and variables[1] != "f":
                    resultado2 = "Debe ingresar finalizar() o por ejemplo 180.0 C K"
                respuesta_servidor = str(direccion_cliente[0]) + " resultado: " + str(resultado) + str(resultado2) + str(resultado3)
                socket_cliente.send(respuesta_servidor.encode("utf-8"))
            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\n∫Se interrunpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    #socket_cliente.close()
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")
