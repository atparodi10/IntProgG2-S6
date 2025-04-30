# Serie de Fibonacci hasta un límite

def Fibonacci(limit):
    a = 0
    b = 1
    if limit == 0:
        print(a)
        return
    elif limit == 1:
        print(a, b)
        return
    for i in range(0, limit):
        print(a)
        c = a + b
        a = b
        b = c

def main():
    while True:
        fin = int(input("ingrese hasta donde quiere: "))
        if fin < 0:
            print("Ingrese un número valido.")
        
        else: 
            break
    Fibonacci(fin)

main()