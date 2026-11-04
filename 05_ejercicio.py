numero_letras = int(input("¿Cuantas letras va a ingresar?: "))

lista_letras = []
for i in range(1, numero_letras + 1):
    letra = input(f"Ingrese letra # {i}: ").lower()
    if letra.isalpha():
        lista_letras.append(letra)


vocales = ("a", "e", "i", "o", "u")
for vocal in vocales:
    print(f"Cantidad de {vocal} = {lista_letras.count(vocal)}")
