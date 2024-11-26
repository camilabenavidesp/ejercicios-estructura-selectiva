Partido1 = input("Ingrese cantidad de goles en el partido 1: ")
Partido2 = input("Ingrese cantidad de goles en el partido 2: ")
Partido3 = input("Ingrese cantidad de goles enel partido 3: ")
Partido4 = input("Ingrese cantidad de goles en el partido 4: ")
SUMA = Partido1 + Partido2 + Partido3 + Partido4
if SUMA > 10:
    Promedio = SUMA / 4
    print(f"Su promeido es: {promedio}")
else: 
    print("El promedio no se puede calcular")
    