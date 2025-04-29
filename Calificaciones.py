#Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
#ingresa calificaciones en una lista por medio de comas
while True:
    try:
        calificacion = float(input("Ingresa una calificacion para validar entradas: "))
        valor_comparar = float(input("Ingresa un valor a comparar: "))
        break
    except ValueError:
        print("Ingresa valores numericos como 4.0,3.8....")

calificaciones_str = str(input("Ingresa tus notas seguido de comas, asi 4.0,3.8,...:  "))
[float(cal) for cal in calificaciones_str.split(",")]
if valor_comparar > calificaciones_str:
    print("Aprobaste.")
else:
    print("Reprobaste")


