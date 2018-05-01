
import re

print("Bienvenido a la cedulacion! Porfavor introduzca su cedula.")
cedula = input("Coloca su cedula: ")
patron1 = '[1-13]{1}\-[0-9]{0,3}\-[0-9]{0,4}'
patron2 = '([PE]|[N]|[E]){1}\-[0-9]{0,3}\-[0-9]{0,4}'

if re.search(patron1, cedula):
        print("La cedula " + cedula + " es valida y ha sido guardada en el registro.")
        ruta2 = '.vscode\\Cedula.txt'
        archivo_Cedula = open(ruta2, 'a')
        archivo_Cedula.write("Una Cedula ha sido guardada \n" )
        archivo_Cedula.close()
else:
    if re.search(patron2, cedula):
            print("La cedula " + cedula + " es valida y ha sido guardada en el registro.")
            ruta2 = '.vscode\\Cedula.txt'
            archivo_Cedula = open(ruta2, 'a')
            archivo_Cedula.write("Una Cedula ha sido guardada \n" )
            archivo_Cedula.close()
    else:
        print("la cedula " + cedula + " es invalid, por favor intente denuevo")

print("Ingrese su nombre.")
ruta = '.vscode\\nombres.txt'
nombres = open(ruta, 'r')
nombre =(input("Introduzca el nombre: "))
if  nombre in nombres:
    print (" El nombre esta dentro de la lista prohibida de nombres, por favor intentelo denuevo")
else: 
    print("el nombre: " + nombre + " es valido")
    ruta2 = '.vscode\\Cedula.txt'
    archivo_Cedula = open(ruta2, 'a')
    archivo_Cedula.write("Un nombre ha sido guardada \n" )
    archivo_Cedula.close()