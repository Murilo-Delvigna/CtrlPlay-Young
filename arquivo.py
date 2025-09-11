while True:
    try:
        base = int(input("Digite um número: "))  
        expoente = int(input("Digite o expoente: "))  

        if base < 0 or expoente < 0:
            print("Número negativo não é permitido.")
        else:
            resultado = base ** expoente
        print(f"O resultado é: {resultado}")

    except ValueError:
        print("Você precisa digitar apenas números inteiros.")
        print("Você nao pode digitar letras.")














