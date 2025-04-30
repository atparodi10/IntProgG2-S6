# Adivinar un numero

import random

def AdivinarNum():
    num = random.randint(1, 10)
    for i in range(100):
       num2 = int(input("Ingresa un numero entre 1 y 10: "))
       if num2 < num:
           print("El numero es mayor. Intenta Otra Vez.")
           
       elif num2 > num:
           print("El numero es menor. Intenta Otra vez.")
        
       else:
           print("Has adivinado.")
           print(f"El numero es {num}") 
           break  




def main():
    AdivinarNum()
    
main()