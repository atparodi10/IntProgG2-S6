# Suma de numeros hasta llegar a un limite

def SumaNum():
    suma = 0
    for i in range(1000):
        num = int(input("Ingresa un número a sumar: "))
        suma += num
        if suma > 100:
            break
        print(f"La suma va en: {suma}")
    print(f"La suma total es de: {suma}")
    
    

def main():
    SumaNum()

main()