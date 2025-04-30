# Promedio de calificaciones

def PromedioCal():
    suma = 0
    contador = 0
    for i in range(1000):
        calificaciones = float(input("Ingresa la calificación: "))
        while calificaciones < -1:
            print("Ingrese una calificación valida.")
            calificaciones = float(input("Ingresa la calificación: "))
        
        if calificaciones != -1 and calificaciones > -1:
            contador += 1
            suma += calificaciones
        
        else: 
            break
        
       
    
    if contador > 0:
        promedio = suma / contador
        print(f"Promedio: {promedio: .2f}")
    
    else:
        print("No se ingresaron calificaciones.")
    
            
    
def main():
    print("Para finalizar el programa ingrese -1.")
    PromedioCal()
    

main()