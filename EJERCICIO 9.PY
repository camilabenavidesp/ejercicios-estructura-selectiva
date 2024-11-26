Edad = int(input("Ingrese la edad de la persona que desea ingresar al parque de diversiones: "))
if Edad >= 1 and Edad <= 4:
    print("La persona puede ingresar gratis")
elif Edad > 4 and Edad <= 8:
    print("\n El tickete para esta persona tiene un costo de: ")
    print("\n 2 Dolares")
    print("8600 en pesos colombianos")
elif Edad > 9 and Edad <= 16:
    print("\n El tickete para esta persona es de: ")
    print("\n 6 Dolares")
    print("26334 pesos colombianos")
elif Edad > 36:
    print("\n El tickete para esta persona es de: ")
    print("\n 10 Dolares")
    print("43956 pesos colombianos")