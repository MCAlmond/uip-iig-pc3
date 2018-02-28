
import re

patron = '[0-7]'
palabras = ['1', '15', '7']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '\\\[a-z]sa'
palabras = ['casa', 'cesa', 'cosa', 'tasa', '\\asa']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

patron = '[A-Za-z][6-9a-z].\.exe'
palabras = ['A7a.exe', 'tns.exe', 'X1..exe']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

#cuando es \d es cualquier caracter que sea un digito
#\D es un caracter que NO sea un digito
#\w es un caracter alfanumerico
#\W caracter NO alfanumerico
#\s espacio blanco
#\S espacio never o caracter de no espacio
patron = '\d\w\w\w\d\.exe'
palabras = ['1aaa1.exe', '10aa1.exe', '11111.exe', '1,,,1.exe']

for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")

#repeticion, utiliza un signo de + el caracter de lado izqueirda aparazca una o varios veces, 
# * que aparece de lado izquierdo se repite el 0
#? aparece cero o una vez, o no aparece o aparece una vez
# {} coloca un numero adentro y se repita la cantidad colocada {1,2 se repite 1 a 2 veces} {7, } se repite 7 a 0 veces
# | es un "o" 
patron = '[A-Z][a-z]+\s[A-Z](\.|[a-z]+)'
palabras = ['Abdel M.', 'Abdel M', 'Abdel Martinez', 'Abdulah Ramadahzunzo.di']

#search busca la palabra dentro de cualquier punto
#match lo busca desde la primera palabra
for palabra in palabras:
    if re.match(patron, palabra):
        print("La palabra " + palabra + " cumple.")
    else:
        print("La palabra " + palabra + " no cumple.")