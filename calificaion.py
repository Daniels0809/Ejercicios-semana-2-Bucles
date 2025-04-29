lista_calificaiones = [] #Inicializamos una lista vacia para guardar las calificaciones.
def calcularPromedio():
    sumaCal = 0
    for i in range(len(lista_calificaiones)):
        sumaCal += lista_calificaiones[i]
    promedio = sumaCal/len(lista_calificaiones)
    if promedio >= 60:
        print(f"Felicidades tu promedio fue de: {promedio}")
    else:
        print(f"Tu lastima tu promdeio fue de: {promedio}")
        
def calificacionMayor():
    while calificacion > 60:
        conteo += 1
        print(f"{conteo} calificaciones fueron mayores al valor especificado.")
        break
    
while True: #Bucle para validacion de datos.
    try:
        salir = str(input("Bienvenido deseas seguir si/no: ")) #Opcion para seguir o salir del programa.
        if salir == "no":
            print("Hasta la proxima.")
            break
        elif salir == "si":
            calificacion = float(input("Ingresa tu calificación: "))#Ingresamos las calificaciones.
            if 0 <= calificacion <= 100: #Revisamos que el dato este entre 0 y 100.
                lista_calificaiones.append(calificacion) #Usamos metodo append(calificacion) para gregar los datos a la lista.
                if calificacion >= 60: 
                    print(f"Felicidades aprobaste con {calificacion}")
                elif calificacion <60:
                    print(f"Que lastima reprobaste con tu calificaion de {calificacion}")
        else:
            while True:
                salir = str(input("Ingresaste la opcion invalida, es si o no: "))
                if salir == "si" or salir == "no":
                    break
    except ValueError:
        print("Ingresa numeros entre 0 y 100")
        
calcularPromedio()
calificacionMayor()

