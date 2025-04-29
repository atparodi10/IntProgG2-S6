def mostrarLetra(numero):
    for i in range(numero):
        print(f"a"*numero)
    
    
def main():
    num = int(input("Ingresa un numero: "))
    mostrarLetra(num)
    
main() 