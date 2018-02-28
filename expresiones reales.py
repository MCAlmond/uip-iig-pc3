
import re #re means regular library

if __name__ == '__main__':
    palabra1 = 'xopa'
    palabra2 = 'sopa'
    palabra3 = 'ropa'

    if re.match(palabra1, palabra2):
        print('Opa')
    else: 
        print('Nah!')

    if re.match('...a', palabra1): #the period represents a comodin, as in it does nothing to the code
        print('Opa opa!')
    else:
        print("No sirve")

    if re.match('\.png', '.png'):  #upon using the backslash it will define the dot
        print("Imagen PNG")

    
    extensiones = ['doc', 'xls', 'ppt', 'mp3', 'flv']
    for tipo in extensiones:
        if re.match('doc|xls|ppt', tipo):
            print("Billete para Microsoft")
        elif re.match('mp3', tipo):
            print("Billete para Spotify")
        else:
            print("Habla!")

    palabras = ['rata', 'rampa', 'rasca', 'chino']
    for p in palabras:
        if re.match('r(..|...|....)a', p): #in ths example it prints any word that starts with r and ends with a, which chino wouldn't be valid and the range
           print(p)
