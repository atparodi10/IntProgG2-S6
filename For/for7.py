# Contador regresivo

def ContaReg(num):

    for i in range(num, 0-1, -1):
        print(f"{i}")


def main():
    inicio = 0
    while inicio <= 0:  
        inicio = int(input("Ingresa donde quieres que empieze la cuenta regresiva: "))

        if inicio <= 0:
            print("Ingrese un numero mayor a 0 para iniciar el contador.")
        
    ContaReg(inicio)

main()