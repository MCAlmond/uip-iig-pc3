# para poner y quitar el los comentarios del codigio se usa ctrl + / y para quitarlo utiliza la misma combinacion
# puede guardar cualquiere cosa en la coleccion y condiciones. 
# lista puede contener, booleano, datos, diccionarios
# puede tener una lista dentro una lista, todo elemento comienza con 0,1,2... 
# tiene que poner __name__ cuando incia una lista, sino el programa no lo va a leer

# if __name__ == '__main__':
#     ganadores = ['Petra', 'Juana', 'Calixtra', 'Toribia']
#     listaloca = ['Susana', 12, True, ['S','T','D']] #recuerda que la letras es otra lista, que estan dentro de la lista de Susana
#     #para la localizacion de los elementos dentro de la lista
#     print(ganadores[2])
#     print(listaloca[0])
#     print(listaloca[3][2])
#     print(ganadores)
#     print(len(ganadores)) #te señala la longitud de una lista
#     print(ganadores[1:3]) #slicing: es un elemento para extrae los elementos dentro de una lista eje: 1:3
#     print(listaloca[:3]) #la colocacion de un numero adelante es del inicio hasta la posiciona ultima
#     otralista = listaloca[:1] + ganadores #para agregar un elemento de una lista a otra
#     print(otralista)
#     otra = input('Quien se lo gano: ')
#     ganadores.append(otra) #append es aregar un elemento a final de la lista
#     ganadores. insert(4, otra) #insert agregar el elemento en la posicion que desea en la lista, el numero a lado es la posicion que va dentro de la lista, recuerda que el 0 es el inicial
#     print(ganadores)

#     for g in ganadores: #la g imprime el nombre de la lista
#         print(g)

# abc = [1, 2, 3]
# abc. insert(1,4)
# print(abc)
# abc[1] = 5 #sustituye el numero que esta en esa posicion
# print(abc)
# abc.append(6)
# print(abc)
# del abc[3] #del elimina el numero de la posicion
# print(abc)

# vacia = []
# num = int(input("Cuanto nombres? ")) #para controla el for y puede colocar cuanto numeros de posiciones quiere
# for n in range(num): #el range la lista de numeros enteros, cuando posiciones quiere en la lista, luego coloca el elemento
#     nombre = input("Nombre " +str(n) + ":") #el valor de la posicion de la cadena
#     vacia.append(nombre)
# print(vacia)

# tupla1 = ('Petra', 'tiene', 'plata') #el tupla es un codigo que no puede modificar la lista, ni agregar un elemento
# tupla2 = tupla1[0:2] #los tuplas termina con un coma al final
# print(tupla1)
# print(tupla2)
# del tupla1 #cuando imprimes el tupla despues de borrarlo no sale porque se borro
# print(tulpa1)
# print(tupla2)
# print("WOLOLO")

libreria = {'Arte de la Guerra': 'Sun Tzu'} #el arte de la guerra es la llave y sun tzu es 
libreria['Inferno'] = 'Disco' #la llave son unicas, 
print(libreria['Arte de la Guerra'])

css = {'Dundunsua': ['Ranguliao!', 'Hermanito...']}
css['Dundunsua'].append('No te tire!')
css['Viejto que se rie'] = "Ranguliao se llame ese pelao"
print(css)

if 'Dundunsua' in css: #este se usa para verificar si el elemento existe, si es entonces imprimir Cristo te ama, y si no entonces Tirate pue
    print("Cristo te ama!")
else:
    print("Tirate pue!")