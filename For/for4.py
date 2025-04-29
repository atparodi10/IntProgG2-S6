# imprimir tabla de multuplicar de cualquier numero

def TablaMul(num):
    for i in range(1, 13):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")
    

def main():
    numero = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))
    TablaMul(numero)
    
main()