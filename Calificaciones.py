#Modificaciones de taller semana 2, viernes 2 de Mayo.

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
            print("Porfavor, corregir las calificaciones no son validas.")
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
    contador2 = 0
    for calificacion in calificaciones:
        while calificacion > comparacion:
            print(f"Que bien tu calificacion {calificacion} es mayor a {comparacion}")
            contador = contador+1
            break
        else:
            print(f"Que mal, tu calificacion {calificacion} fue menor a {comparacion}")
    print(f"{contador} notas fueron mayores a {comparacion}")
    for cal in calificaciones:
        if cal == comparacion:
            contador2 += 1
    if contador2 > 0:
        print(f"Se encontro el numero {comparacion}, {contador2} veces.")
    else:
        print(f"No se encontro {comparacion}")
def promedio_Final(calificaciones):
    suma = 0
    cantidad = 0
    for cal in calificaciones:
        suma = suma + cal
        cantidad += 1
    if cantidad > 0:
        promedio = suma/cantidad
        print(f"Tu promedio fue de {promedio}.")
    else:
        print("No hay calificaciones para promediar")





cal_obtenidas = []
comparacion = None

while True:
    try:
        print("\n------Menu de Opciones------")
        print("Bienvenido.\nSelecciona qué acción quieres realizar:")
        print("1. Para ingresar calificaciones y valor a comparar.")
        print("2. Para comparar valores.")
        print("3. Para sacar tu promedio.")
        print("4. Salir.")
        opciones = input("Ingresa la opción: ")

        if opciones == "1":
            cal_obtenidas = obtener_Calificaciones()
            if cal_obtenidas:
                comparacion = valor_Comparar()
        elif opciones == "2":
            comparacion_Calificaciones(cal_obtenidas, comparacion)
        elif opciones == "3":
            promedio_Final(cal_obtenidas)
        elif opciones == "4":
            print("¡Hasta luego!")
            break # Sale del bucle principal
        else:
            print("Opción no válida. Por favor, ingresa 1, 2, 3 o 4.")

    except ValueError:
        print("Error!. Ingresa una opción válida (1, 2, 3 o 4).")







cal_obtenidas = []
comparacion = None
while True:
    try:
        print("------Menu de Opciones------")
        print("Bienvenido.\nSelecciona que accion quieres realizar:")
        print("1.Para ingresar calificaciones y valor a comparar.\n2.Para comparar valores\n3.Para sacar tu promedio\n4.Sali")
        opcion = input("Ingresa la opción: ")
        if opcion == "1":
            cal_obtenidas = obtener_Calificaciones()
            if cal_obtenidas:
                comparacion = valor_Comparar()
        elif opcion == "2":
            comparacion_Calificaciones(cal_obtenidas, comparacion)
        elif opcion == "3":
            promedio_Final(cal_obtenidas)
        elif opcion == "4":
            break
        else:
            print("Error!. Ingresa la opcion 1, 2 o 3....")
    except ValueError:
        print("Error!. Ingresa la opcion 1, 2 o 3....")

