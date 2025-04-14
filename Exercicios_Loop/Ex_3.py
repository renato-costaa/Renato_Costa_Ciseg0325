soma_notas = 0
contador = 0

# Leitura das notas dos 10 alunos
while contador < 10:
    nota = float(input(f"Introduza a nota do aluno {contador + 1}: "))
    
    # Verificar se a nota está entre 0 e 20 (considerando notas válidas de 0 a 20)
    if nota < 0 or nota > 20:
        print("Nota inválida! A nota deve estar entre 0 e 20.")
        continue  # Volta à leitura da nota do mesmo aluno
    
    soma_notas += nota  # Somar a nota ao total
    contador += 1  # Incrementar o contador para ler a próxima nota

# Calcular a média
media = soma_notas / 10

# Apresentar a média
print(f"\nA média das notas dos 10 alunos é: {media:.2f}")
