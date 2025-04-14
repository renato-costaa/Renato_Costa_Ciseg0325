numero = int(input("Introduza um número inteiro: "))

# Verificar se o número é menor ou igual a 1 (não é primo)
if numero <= 1:
    print(f"O número {numero} não é primo.")
else:
    # Inicializar a variável para verificar a divisibilidade
    divisor = 2
    while divisor < numero:
        # Verificar se o número é divisível por qualquer número menor que ele
        if numero % divisor == 0:
            print(f"O número {numero} não é primo.")
            break  # Sair do ciclo se encontrar um divisor
        divisor += 1
    else:
        # Se não encontrou nenhum divisor, o número é primo
        print(f"O número {numero} é primo.")
