puntos = float (input ("Ingrese puntuacion: "))

if puntos < 0.0 or puntos > 1.0:
    print("fuera de rango!!..Debe ser entre 0.0 y 1.0")
else:
    if puntos > 0.9:
        print("sobresaliente")
    elif puntos >= 0.8 and puntos < 0.9:
        print("notable")
    elif puntos >= 0.7 and puntos < 0.8:
        print("bien")
    elif puntos >= 0.6 and puntos < 0.7:
        print("suficient")
    else:
        print("Insuficient")
