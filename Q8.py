print("Uma calculadora programada em Python")
numberOne = float(input("Digite o primeiro número: "))
numberTwo = float(input("Digite o segundo número: "))
choice = input("Escolha uma operação básica: ")
print()
if choice == "+":
    print(f'O valor é {numberOne + numberTwo}')
elif choice == "-":
    print(f'O valor é {numberOne - numberTwo}')
elif choice == "*":
    print(f'O valor é {numberOne * numberTwo}')
else:
    print(f'O valor é {numberOne / numberTwo}')