contador = 0

# Leitura dos 10 números
while contador < 10:
    numero = int(input(f"Introduza o {contador + 1}.º número: "))
    
    # Verificar se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")
    
    contador += 1