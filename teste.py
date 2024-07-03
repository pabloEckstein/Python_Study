nota_1 = float(input("Digite a primeira nota: "))
while nota_1 < 0 or nota_1 > 10:
    nota_1 = float(input("Valores inválidos. Digite Novamente: "))

nota_2 = float(input("Digite a segunda nota: "))
while nota_1 < 0 or nota_1 > 10:
    nota_2 = float(input("Valores inválidos. Digite Novamente: "))

media = (nota_1 + nota_2) / 2

if media < 6:
    print(f"Aluno reprovado com a média {media:.2f}")
else:
    print(f"Aluno aprovado com a média {media:.2f}")