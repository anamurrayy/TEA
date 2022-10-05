file2read = input("Ingese el nombre del archivo: ")
fhandle = open("temperaturas.txt", "r")
for linea in fhandle:
    print(linea.upper)


#print(fhandle.read().upper())



