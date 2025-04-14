seg = int(input("Digita o número de segundos: "))

# Cálculo de horas, minutos e segundos
if seg >= 3600:
    hor = seg // 3600
    seg = seg % 3600
else:
    hor = 0

if seg >= 60:
    min = seg // 60
    seg = seg % 60
else:
    min = 0

print(f"{hor} horas, {min} minutos e {seg} segundos")
