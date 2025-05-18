# 1. Básico: imprime todos los números enteros del 0 al 100
for i in range(101):
    print(i)

print("-----")

# 2. Múltiples de 2 entre 2 y 500
for i in range(2, 501, 2):
    print(i)

print("-----")

# 3. Contando Vanilla Ice
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

print("-----")

# 4. Wow. Número gigante a la vista
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("Suma total de pares del 0 al 500000:", suma)

print("-----")

# 5. Regrésame al 3
for i in range(2024, 0, -3):
    print(i)

print("-----")

# 6. Contador dinámico
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
