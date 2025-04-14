notas=0
acima_da_media=0

for i in range(10):
    nota = int(input("Nota do Aluno:"))
    if 0 <= nota <= 20:
        notas += nota
    else:
        print("Nota inválida! A nota deve estar entre 0 e 20.")

media = notas / 10

for i in range(10):
    if nota >= media:
        acima_da_media += 1

print(f"Média das Notas: {media}")
print(f"Alunos com nota igual ou acima da média: {acima_da_media}")