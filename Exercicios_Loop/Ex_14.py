for numero in range(1, 101):  # Vai de 1 até 100
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):  # Vai de 1 até 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print()  # Saltar uma linha entre as tabuadas
