Bonificacion = float(input("Ingrese el valor de su bonificacion para hallar el producto a compara: "))
if Bonificacion < 50000:
    print("Su producto  recbir es una Camara WEB, felicidades")
elif Bonificacion > 50000 and Bonificacion <= 200000:
    print("El producto que puede comprar es un SubWoofer")
elif Bonificacion > 200000 and Bonificacion <= 500000:
    print("El producto que puede comprar es un Disco duro externo")
elif Bonificacion > 500000 and Bonificacion <= 1000000:
    print("El producto que puede comprar es una Impresora Funcional")
elif Bonificacion > 1000000:
    print("El producto que puede comprar es un proyector")
    