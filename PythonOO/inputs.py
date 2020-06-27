nome = input("Digite seu nome: ")
print(nome)
print(nome.upper())
print(nome.capitalize())

print("O nome digitado foi "+nome)
print("O nome digitado foi {}".format(nome))
print("{} foi o nome digitado".format(nome))

sobre = input("Digite seu sobrenome: ")
print("{} {} é o nome completo".format(nome,sobre))
