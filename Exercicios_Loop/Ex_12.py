numero = int(input("Introduza um número: "))

# Inicializar o contador de operações
contador_operacoes = 0

# Realizar as operações para todos os números menores que o número informado
for i in range(1, numero):
    # Soma
    soma = numero + i
    print(f"{numero} + {i} = {soma}")
    contador_operacoes += 1
    
    # Subtração
    subtracao = numero - i
    print(f"{numero} - {i} = {subtracao}")
    contador_operacoes += 1
    
    # Multiplicação
    multiplicacao = numero * i
    print(f"{numero} * {i} = {multiplicacao}")
    contador_operacoes += 1
    
    # Divisão
    if i != 0:  # Verificar se i não é zero antes de dividir
        divisao = numero / i
        print(f"{numero} / {i} = {divisao:.2f}")
        contador_operacoes += 1

# Apresentar o total de operações realizadas
print(f"\nTotal de operações realizadas: {contador_operacoes}")
