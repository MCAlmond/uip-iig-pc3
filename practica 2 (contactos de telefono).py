
if __name__ == '__main__':
    contactos = 'D:\\Ali\\UNIVERSITY 2016-2019\\2018\\Cuart. 7\\Programación de Computadoras III\\.vscode\\contactos.txt'
    archivo = open(contactos, 'r')
    contactos1 = (archivo.readlines())
    numero_telefonico = input("¿Cual es el numero de telefono que quieres marca?:")
    for contacto in contactos1 :
        if numero_telefonico in contacto:
            print ("Estas llamando a: " + contacto.split (" ")[0])       
    else :
        print ("El numero no esta en la lista de contactos")
        print ("¿Desea agragar el contato?")
        eligio = input("Escriba 1 para si o 2 para no:  ")
        if eligio == "1":
            def telefono():
                nom = input("Porfavor coloque el nombre del contacto: ")
                tele = int(input("Porfavor coloque el numero de telefono del contacto: "))
            telefono()

            archivo = open(contactos, 'a')
            contactos.write(telefono)
            contactos.close()
        elif eligio == "2":
            print("Hasta luego!")


    # archivo = open(ruta, 'r')

    # contactos = archivo.readlines()

    # print("Cual es el numero de telefono que quieres marca?")
    # cell = input("Telefono: ")

    # if cell == '3322111':
    #     print("llamando a...")
    #     print(contactos)
    # else:
    #     print("el numero que usted marco no existe")
