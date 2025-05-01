# Suma de números impares

def SumaImpares():
    contador = 0
    suma = 0
    for i in range(100+1):
        if i % 2 == 1:
            print(i)
            suma += i
            contador += 1
        
    print(f"El resutado de la suma de los numeros impares es de: {suma}")
    print(f"Total de iteraciones de ciclo: {contador}")

def main():
    SumaImpares()
    

main()