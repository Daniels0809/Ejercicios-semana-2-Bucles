import os
os.system("clear")
while True:
    try:
        note = int(input("Ingresa una calificación del 0 al 100: "))
        if 0 <= note <= 100:
            break
        else:
            print("Por favor ingresa un número entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

if note >= 70:
    print("El estudiante ha APROBADO.")
else:
    print("El estudiante ha REPROBADO.")

while True:
    list_input = input("\nIngresa una lista de calificaciones separadas por comas: ")
    try:
        listNote = [int(x.strip()) for x in list_input.split(",")]
        if all(0 <= x <= 100 for x in listNote):
            break
        else:
            print("Todas las calificaciones deben estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar solo números separados por comas.")

average = sum(listNote) / len(listNote)
print(f"El promedio de las calificaciones es: {average:.2f}")

while True:
    try:
        value = int(input("\nIngresa un valor para comparar: "))
        if 0 <= value <= 100:
            break
        else:
            print("Ingresa un valor entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

counter = 0
for score in listNote:
    if score > value:
        counter += 1

print(f"Hay {counter} calificaciones mayores que {value}.")

while True:
    try:
        search = int(input("\nIngresa la calificación que deseas buscar en la lista: "))
        if 0 <= search <= 100:
            break
        else:
            print("Ingresa una calificación entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

contador = 0
for calificacion in listNote:
    if calificacion != search:
        continue
    contador += 1
    if contador >= 10:
        print("La calificación fue encontrada 10 veces, deteniendo la búsqueda.")
        break

if contador > 0:
    print(f"La calificación {search} aparece {contador} veces en la lista.")
else:
    print(f"La calificación {search} no está en la lista.")