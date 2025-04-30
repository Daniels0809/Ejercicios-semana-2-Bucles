def obtener_Calificaciones ():

    while True:

        calificaciones_str = str(input("Ingresa tus calificaciones. Ejemplo: 80,60,55.5...: "))
        lista_cal = calificaciones_str.split(",")
        cal_float = []
        errores = False

        for calificacion_str in lista_cal:
            try:
                calificacion = float(calificacion_str.strip())
                if 0 <= calificacion <= 100:
                    cal_float.append(calificacion)
                    if calificacion >= 60:
                        print(f"Excelente {calificacion},aprobaste.")
                    else:
                        print(f"Que mal {calificacion},reprobaste.") 
                else:
                    print(f" {calificacion} esta fuera del rango permitido.")
                    errores = True
            except ValueError:
                print(f"La calificacion {calificacion_str.strip()} no es valida.")
                errores = True

        if not errores and cal_float: #Verificamos que no hayan errores y retornamos la lista con las calificaciones.
            return cal_float
        elif errores:
            print("Porfavor, corregir las calificaiones no validas.")
        else:
            print("No hubo ingreso de calificaciones.")

def valor_Comparar():
    while True:
        valorComparar_str = str(input("Ingresa el valor a comparar: "))
        try:
            comp = float(valorComparar_str)
            return comp
        except ValueError:
            print(f"{valorComparar_str} no es valido.")
def comparacion_Calificaciones(calificaciones, comparacion):
    print(f"Ahora comparando tus calificaciones con {comparacion}")
    contador = 0
    for calificacion in calificaciones:
        while calificacion > comparacion:
            print(f"Que bien tu calificacion {calificacion} es mayor a {comparacion}")
            contador = contador+1
            break
        else:
            print(f"Que mal, tu calificacion {calificacion} fue menor a {comparacion}")

        print(f"{contador} notas fueron mayores a {comparacion}")





cal_obtenidas = obtener_Calificaciones()
if cal_obtenidas:
    comparacion = valor_Comparar()
    comparacion_Calificaciones(cal_obtenidas, comparacion)
