numero = int(input("Introduza um número inteiro: "))

# Inicializar a variável para contar os divisores
contador_divisores = 0

# Verificar quantos divisores o número tem
for i in range(1, numero + 1):
    if numero % i == 0:
        contador_divisores += 1

# Apresentar a quantidade de divisores
print(f"O número {numero} tem {contador_divisores} divisores.")
