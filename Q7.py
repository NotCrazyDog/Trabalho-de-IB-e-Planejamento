nome = input("Digite o nome do aluno(a): ")
disciplina = input("Digite a disciplina: ")
nota1 = float(input("Digite a nota parcial: "))
nota2 = float(input("Digite a nota bimestral: "))
media = (nota1 + nota2)/2
print()
print(f'A média de {nome} é {media} na disciplina {disciplina}')
if media >= 6:
    print(nome + " está aprovado na disciplina " + disciplina)
else:
    print(nome + " está reprovado na disciplina " + disciplina)