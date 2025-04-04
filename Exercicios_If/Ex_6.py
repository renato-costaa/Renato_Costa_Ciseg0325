
nome_cli = input("Digite o nome do cliente: ")
val_compra = float(input("Digite o valor da compra: "))

# Calculo do desconto e do valor total
if val_compra <= 200:
    desc_perc = 10
elif val_compra > 200 and val_compra <= 500:
    desc_perc = 15
else:
    desc_perc = 20

val_desc = (desc_perc / 100) * val_compra
val_total = val_compra - val_desc

print(f"Nome do cliente: {nome_cli}")
print(f"Valor da compra: {val_compra:.2f}€")
print(f"Percentual de desconto: {desc_perc}%")
print(f"Valor do desconto: {val_desc:.2f}€")
print(f"Valor total a pagar: {val_total:.2f}€")
