numero = int(input("Ingrese un número: "))
suma = 0
while numero > 0:
    digito = numero % 10
    suma += digito
    numero = numero // 10
print("Suma de dígitos:", suma)