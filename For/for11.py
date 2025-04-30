#  Menú interactivo

from datetime import datetime

def MostrarMenu():
    print("-----SELECCIONA UNA OPCIÓN-----")
    print("1. Saludar")
    print("2. Fecha")
    print("3. Salir")

def Saludar():
    print("Hola, un gusto Saludarte")

def Fecha():
    fecha_actual = datetime.today()
    print(f"La fecha actual es {fecha_actual}")


def main():
    MostrarMenu()
    
    for _ in range(1000):
        opcion = input("Ingresa una opción: ")
        if opcion == "1":
            Saludar()
        
        elif opcion == "2":
            Fecha()
            
        elif opcion == "3":
            print("Hasta Luego.")
            break
        
        else: 
            print("Selecciona una opcion valida.")

main()