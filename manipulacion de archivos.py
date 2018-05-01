

if __name__ == '__main__':
    ruta = 'D:\\Ali\\UNIVERSITY 2016-2019\\2018\\Cuart. 7\\Programación de Computadoras III\\.vscode\\wololo.txt' #ruta absoluta
    archivo = open(ruta, 'r')
    # print( archivo.read() )
    # each letter has a different significance
    # r = lectura, para leer
    # w = escritura, escribir 
    # a = agregar, una linea
    # print( archivo.readline() + " es antes que " + archivo.readline () )
    # print( archivo.readline() ) #readline es un for que muestra la linea actual, no se puede imprimir la posicion directa.

    #readlines lo convierte en una lista
    dias_de_la_semana = archivo.readlines()
    fin_de_semana = ["Sabado", "Domingo"] #si lo escribe en minuscula y el nombre en si es mayuscula tiene que usar d.lower() y d.upper() por ejemplo
    for dia in dias_de_la_semana:
        if any(d in dia for d in fin_de_semana): #usa esto para evitar a hacer varios for para imprimir el codigo
            print(dia)
# ^^^^^^^usa la siguiente codigo para imprimir un dia especifico^^^^^^^^
#el any es un codigo que se existe lo programa

#abriendo un archivo nuevo sin crea un .txt
    ruta2 = '.vscode\\pereza.txt' #ruta relativa, tiene que poner la ruta de donde esta el codigo y no el principal que es Programacion III
    archivo_pereza = open(ruta2, 'w')
    archivo_pereza.write("Tengo pereza\n")
    archivo_pereza.write("Espero que el prof termine temprano")

    archivo.close()
    archivo_pereza.close()