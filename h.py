def obtenerCalificaciones ():
    while True:
        calificaciones_str = str(input("Ingresa tus calificaciones. Ejemplo: 80,60,55.5...: "))
        lista_cal = calificaciones_str.split(",")
        cal_float = []
        for calificacion_str in lista_cal:
            try:
                calificacion = float(calificacion_str.strip())
                if 0 <= calificacion <= 100:
                    cal_float.append(calificacion)
                    return cal_float
                else:
                    print(f" {calificacion} esta fuera del rango permitido.")
            except ValueError:
                print(f"La calificacion {calificacion_str.strip()} no es valida.")
                break
def valorComparar():
    while True:
        valorComparar_str = str(input("Ingresa el valor a comparar: "))
        try:
            comp = float(valorComparar_str)
            return comp
        except ValueError:
            print(f"{valorComparar_str} no es valido.")
def Comparacion(calificacion, comparacion):
    print(f"Ahora comparando tus calificaciones con {comparacion}")
    if calificacion > comparacion:
        print(f"Que bien tu calificacion {calificacion} es mayor a {comparacion}")
    else:
        print(f"Que mal, tu calificacion {calificacion} fue menor a {comparacion}")
        