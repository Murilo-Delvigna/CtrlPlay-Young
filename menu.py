import calculadora

def menu():
    while True :
        print("Menu")
        print("[1] Somar")
        print("[2] subtrair")
        print("[3]  multiplicar")
        print("[4] dividir")
        print("[5] sair")
        opt = int(input("Opçao desejada"))
        if opt == 1:
            num1 = int(input("digite numero 1"))
            num2 = int(input("digite numero 2"))
            print(calculadora.soma(num1, num2))
            pause = input("")

        elif opt == 2:
            num1 = int(input("digite numero"))
            num2 = int(input("digite numero "))
            print(calculadora.subtrair(num1, num2))
            pause = input("")

        elif opt == 3:
             num1 = int(input("digite numero"))
             num2 = int(input("digite numero "))
             print(calculadora.multiplica(num1, num2))
             pause = input("")
            
        elif opt == 4:
             num1 = int(input("digite numero"))
             num2 = int(input("digite numero "))
             print(calculadora.dividir(num1, num2))
             pause = input("")

        elif opt == 5:
            break
        else : 
            menu()
