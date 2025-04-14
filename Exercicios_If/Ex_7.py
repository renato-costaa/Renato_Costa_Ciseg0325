nota1 = float(input("Digita a nota da primeira prova (0 a 10): "))
# Verificar se a 1ª nota está entre 0 e 10
if nota1 < 0 or nota1 > 10:
    print("Nota inválida! A nota deve estar entre 0 e 10.")
    nota1 = float(input("Digita a nota da primeira prova (0 a 10): "))

nota2 = float(input("Digita a nota da segunda prova (0 a 10): "))
# Verificar se a 2ª nota está entre 0 e 10
if nota2 < 0 or nota2 > 10:
    print("Nota inválida! A nota deve estar entre 0 e 10.")
    nota2 = float(input("Digita a nota da segunda prova (0 a 10): "))

nota3 = float(input("Digita a nota da terceira prova (0 a 10): "))
# Verificar se a 3ª nota está entre 0 e 10
if nota3 < 0 or nota3 > 10:
    print("Nota inválida! A nota deve estar entre 0 e 10.")
    nota3 = float(input("Digita a nota da terceira prova (0 a 10): "))

# Cálculo da média
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

# Verificar se o aluno foi aprovado ou reprovado
if media >= 6:
    print(f"Média final: {media:.2f} - APROVADO")
else:
    print(f"Média final: {media:.2f} - REPROVADO")