lista_calificaiones = [] 
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

while True: 
    try:
        calificacion = str(input("Ingresa tus calificaciones: "))
        if 0 <= float(calificacion) <= 100: 
            lista_calificaiones.append(float(calificacion))
            if calificacion >= 60: 
                    print(f"Felicidades aprobaste con {calificacion}")
            elif calificacion <60:
                    print(f"Que lastima reprobaste con tu calificaion de {calificacion}")
    except ValueError:
        print("Ingresa numeros entre 0 y 100")
