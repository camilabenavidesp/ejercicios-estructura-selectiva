Name = input("Ingrese su Nombre: ")
Edad = int(input("Ingrese su Edad: "))
Sexo = input("Ingrese su sexo: Masculino(M), Femenino (F): ")
Sexo1 = Sexo.upper()
EstadoCivil = input("Ingrese su EstadoCivil: ")
EstadoCivil = EstadoCivil.upper()
if Edad < 18:
    print("Edad no requerida para las votaciones, lo siento no puedes votar")
elif Edad >= 18 and EstadoCivil == "CASADA" and Sexo1 == "F":
    print(f"{Name} votas en la Mesa #1")
elif Edad >= 18 and EstadoCivil == "SOLTERA" and Sexo1 == "F":
    print(f"{Name} Votas en la Mesa #2")
elif Edad >= 18 and EstadoCivil == "SEPARADA" and Sexo1 == "F":
    print(f"{Name} Votas en la Mesa #3")
elif Edad >= 18 and EstadoCivil == "OTRO" and Sexo1 == "F":
    print(f"{Name} Votas en la Mesa #4")
elif Edad >= 18 and EstadoCivil == "CASADO" and Sexo1 == "M":
    print(f"{Name} Votas en la Mesa #5")
elif Edad >= 18 and EstadoCivil == "SOLTERO" and Sexo1 == "M":
    print(f"{Name} Votas en la Mesa #6")
elif Edad >= 18 and EstadoCivil == "SEPARADO" and Sexo1 == "M":
    print(f"{Name} Votas en la Mesa #7")
elif Edad >= 18 and EstadoCivil == "OTRO" and Sexo1 == "M":
    print(f"{Name} Votas en la Mesa #8")