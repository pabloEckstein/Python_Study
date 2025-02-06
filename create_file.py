import os

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
email = input("Informe o seu e-mail: ")
bio = input("Informe algo adicional sobre você: ")
info = (f"O meu nome é {nome}, tenho {idade} anos. Meu email é {email}. Mais informação sobre mim: \n\n{bio}")
nome_arquivo = (f"{nome}_info.txt")
f = open(nome_arquivo, "x")
f.write(info)
f.close()
x = input("Quer apagar o arquivo? (s para SIM, n para NÃO)")
if x == "s":
    os.remove(nome_arquivo)
else:
    f = open(nome_arquivo)
