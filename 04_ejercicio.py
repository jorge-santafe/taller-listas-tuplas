numeros = []

while True:
    numero = int(input("Digite un número o 99999 para terminar: "))
    if numero != 99999:
        numeros.append(numero)
    else:
        break

pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Pares: {pares} total: {len(pares)}")
print(f"Impares: {impares} total: {len(impares)}")
