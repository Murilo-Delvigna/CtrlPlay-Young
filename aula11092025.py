
try:
    num1 = input("Digite um numero")
    num2 = input("Digite outro numero")

    resultado = int(num1) / int(num2)
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero")
except ValueError:
    print("Você precisa digitar apenas números ")
else:

    if int(num1) < 0 or int(num2) < 0:

        print("Numero negativo nao sao permitidos")
    else:
        print(f'o resultado é : {resultado}')