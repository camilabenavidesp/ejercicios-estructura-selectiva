A = float(input("Ingrese el valor del lado A: "))
B = float(input("Ingrese el valor del lado B: "))
C = float(input("Ingrese el valor del lado C: "))
Suma1 = 0
Suma2 = 0
Suma3 = 0
if A + B > C:
    Suma1 = B + C
else:
    print("Los datos ingresados no pertenecen a los de un triangulo")
    if B + C > A:
        Suma2 = A + C
    else:
        print("Los datos ingresados no pertenecen a los de un triangulo")
        if A + C > B:
            print("Los datos ingresados no pertenecen a los de un triangulo")
        else:
            print("Los datos ingresados no pertenecen a los de un triangulo")
            print("\n Con los datos ingresados no podemos calcular el tipo de triangulo")
            if A == B and == C:
                print("Las medidas pertenecen a un triangulo equilatero")
            elif A != B and B != C:
                print("Las medidas ingresadas pertenece a las de un triangulo isoceles")

