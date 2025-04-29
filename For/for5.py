# Contar números pares hasta un límite

def ContarNum(num):
    for i in range(num+1):
        if i % 2 == 0:
            print(i)


def main():
    num = -1
    
    while num <= 0:
        num = int(input("Ingresa el número hasta donde quiere que llegue su contador: "))
        if num <= 0:
            print("Ingresa un numero positivo.")
    ContarNum(num)
main()