Nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
if 4.6<= 5.0:
    resultado = "Excelente"
elif 3.6 <= 4.6: 
    resultado = "Buena"
elif 3.0 <= 3.6:
    resultado = "Aceptable"
elif 2.0 <= 3.0:
    resultado = "Insuficiente"
elif 0.0 <= 2.0:
    resultado = "Deficiente"
else:
        resultado = "Nota fuera de rango"
print("La calificacion cuantitativa es:", resultado)