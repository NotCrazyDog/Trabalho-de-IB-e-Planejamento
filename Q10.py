print("Tabuada dalgo")
number = int(input("Digite um número: "))
choice = input("Escolha uma operação básica: ")
print()
if choice == "+":
    for tab in range(1,11):
        print(f'+{tab} = {number + tab}')
elif choice == "-":
    for tab in range(1,11):
        print(f'-{tab} = {number - tab}')
elif choice == "*":
    for tab in range(1,11):
        print(f'*{tab} = {number * tab}')
else:
    for tab in range(1,11):
        print(f'/{tab} = {number / tab}')