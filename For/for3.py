# Leer dos numeros y leer los numeros entre ellos

def mostrarNum(inicio=0, fin=0):
    if inicio > fin:
        print("Rango invalido.")
        
    else:
        for i in range(inicio, fin+1):
            print(i, end=" ")
        

def main():
    inicio = int(input("Ingresa el primer numero: "))
    fin = int(input("Ingresa el segundo numero: "))
    mostrarNum(inicio, fin)

main()