Matematicas = float(input("Ingrese el puntaje obtenido en el area de Matematicas: "))
Lenguaje = float(input("Ingrese el puntaje obtenido en el area de lenguaje: "))
if Matematicas > Lenguaje:
    print(f"\n Usted obtuvo un puntaje mayor en matematicas con:{Matematicas} y menor en lenguaje con:{Lenguaje}")
elif Matematicas < Lenguaje:
    print(f"\n Usted obtuvo un puntaje mayor en lenguaje con: {Lenguaje} y menor en matematicas con: {Matematicas}")