def exibir_ascii():
    for i in range(0, 256, 20):
        # Imprimir os valores de ASCII e os caracteres correspondentes
        print(f"Códigos ASCII de {i} a {i+19}:")
        for j in range(i, min(i + 20, 256)):  # Para garantir que não ultrapasse 255
            try:
                print(f"{j:3} -> {chr(j)}", end="    ")
            except:
                print(f"{j:3} -> (não imprimível)", end="    ")
        print("\n")
        
        # Perguntar se o utilizador deseja continuar ou sair
        opcao = input("Pressione 'c' para continuar ou qualquer outra tecla para sair: ")
        if opcao.lower() != 'c':
            print("A sair do programa...")
            break

# Chamada para a função exibir_ascii
exibir_ascii()
