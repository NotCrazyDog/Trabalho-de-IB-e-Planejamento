print("Uma calculadora programada em Python")
numberOne = int(input("Digite o primeiro número: "))
numberTwo = int(input("Digite o segundo número: "))
choice = input("Escolha uma operação básica: ")
print()
if choice == "+":
    print(f'O valor é {numberOne + numberTwo}')
elif choice == "-":
    print(f'O valor é {numberOne - numberTwo}')
elif choice == "*":
    print(f'O valor é {numberOne * numberTwo}')
else:
    if numberTwo == 0:
        print('Não é possível divisão por 0!!!')
    else:
        print(f'O valor é {numberOne / numberTwo}')
