def pergunta_Numero():
    numero = 1
    while True:
        try:
                val = int(input("Entre um inteiro:"))
        except:
            print("Parece que você nao digitou um inteiro")
            continue

        finally:
           print("tentativa numero:", numero)
           numero = numero + 1
        print(val)
pergunta_Numero()
               