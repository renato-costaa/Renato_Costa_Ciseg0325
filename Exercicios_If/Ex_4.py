
sal_ini = float(input("Digite o saldo inicial do cliente: "))
cheque = float(input("Digite o valor do cheque: "))

# Descontar o Cheque
if cheque <= sal_ini:
    sal_ini -= cheque
    print(f"Cheque descontado! Saldo restante: {sal_ini:.2f}€")
else:
    print("Cheque não pode ser descontado, saldo insuficiente.")