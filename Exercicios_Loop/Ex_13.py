numero = int(input("Introduza um número para ver a sua tabuada: "))

# Apresentar a tabuada do número
print(f"Tabuada de {numero}:")
for i in range(1, 11):  # Vai de 1 até 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
