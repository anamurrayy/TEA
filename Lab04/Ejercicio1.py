contador = 0
suma = 0 
while True:
  try:
    numero= input("Ingrese un numero: ")
    if (numero == "salir"):
      break
    else:
      contador = contador + 1 
      suma = suma + int(numero)
      promedio = suma / contador 
  except:
    print("Error, debe ingresar un valor numerico")
    contador = contador - 1 
    continue 
print("contador:", contador)
print("sumatoria:", suma)
print("promedio:", promedio)