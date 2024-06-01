hora = int(input("Digite o horário (formato de 24 horas): "))
if hora >= 0 and hora < 12:
    print("Está de manhã")
elif hora >= 12 and hora < 18:
    print("Está de tarde")
else:
    print("Está de noite")