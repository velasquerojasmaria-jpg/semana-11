suma =0
for i in range(1,6):
    nota =float(input("ingrese la nota"+str(i)+":"))
    suma += nota
promedio = suma / 5
print("promedio:", promedio)