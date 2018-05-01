

def factorial (n):
    fact = 1
    x = 1
    while x <=n:
        fact *= x
        x += 1
    return fact

if __name__ == "__main__":
    x = int(input("Numero: "))
    print(factorial(x)) 
    #print(factorial(x))

#esto se usa para probar si corre el programa