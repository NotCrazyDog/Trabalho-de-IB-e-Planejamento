nome = input("Digite o nome completo do cidadão: ")
idade = int(input("Digite a idade do cidadão: "))
if idade > 15:
    print(nome + " " + "pode emitir seu título de eleitor")
else:
    print(nome + " " + "não pode emitir seu título de eleitor")