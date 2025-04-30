# Número de dígitos

def CantDig(numero):
    numeroBase = numero
    
    if numero == 0:
        print(f"{numeroBase} tiene 1 dígito.")
        return
    
    numero = abs(numero)
    digitos = 0
    
    for _ in range(100):
        if numero == 0:
            break
        
        numero //= 10
        digitos += 1
    
    print(f"{numeroBase} tiene {digitos} dígitos.")





def main():
    numero = int(input("Ingresa un número: "))
    CantDig(numero)


main()