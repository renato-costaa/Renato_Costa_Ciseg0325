num_mes = int(input("Digita um número de 1 a 12 para saber o mês correspondente: "))

# Verificando o mês
if num_mes == 1:
    mes = "Janeiro"
elif num_mes == 2:
    mes = "Fevereiro"
elif num_mes == 3:
    mes = "Março"
elif num_mes == 4:
    mes = "Abril"
elif num_mes == 5:
    mes = "Maio"
elif num_mes == 6:
    mes = "Junho"
elif num_mes == 7:
    mes = "Julho"
elif num_mes == 8:
    mes = "Agosto"
elif num_mes == 9:
    mes = "Setembro"
elif num_mes == 10:
    mes = "Outubro"
elif num_mes == 11:
    mes = "Novembro"
elif num_mes == 12:
    mes = "Dezembro"
else:
    mes = None

# Mostrando o resultado
if mes:
    print(f"O mês correspondente ao número {num_mes} é {mes}.")
else:
    print("Número de mês inválido! O número deve estar entre 1 e 12.")