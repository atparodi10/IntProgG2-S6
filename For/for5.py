# Contar números pares hasta un límite

def ContarNum(num):
    for i in range(num+1):
        if i % 2 == 0:
            print(i)


def main():
    num = int(input("Ingresa el número hasta donde quiere que llegue su contador: "))
    while True:
        if num > 0:
            ContarNum(num)
            break
        else:
            print("Ingresa un numero positivo.")

main()