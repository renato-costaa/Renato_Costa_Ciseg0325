contador_primos = 0
numero = 2  # Começar pelo primeiro número primo

# Apresentar os 10 primeiros números primos
while contador_primos < 10:
    # Verificar se o número é primo
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    
    # Se o número tiver exatamente 2 divisores, é primo
    if divisores == 2:
        print(numero)
        contador_primos += 1
    
    numero += 1
