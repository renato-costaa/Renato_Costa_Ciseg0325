numero = 0

# Ciclo que vai pedir um número até este estar entre 1 e 100
while numero < 1 or numero > 100:
    numero = int(input("Introduza um número entre 1 e 100: "))

# Apresentar o número quando este estiver dentro do intervalo
print(f"O número {numero} está dentro do intervalo entre 1 e 100.")
