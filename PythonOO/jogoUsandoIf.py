
n = int(input("Digite o numero parar começar a brincadeira: "))
print ("\n"*50)
chute = int(input("Digite o numero: "))

while n!=chute:
    
    if(n<chute):
        print("Você errou o numero\nO numero correto é menor que {}".format(chute))
        chute = int(input("Digite o numero: "))
    if(n>chute):
        print("Você errou o numero\nO numero correto é maior que {}".format(chute))
        chute = int(input("Digite o numero: "))
print ("Você acertou o numero")
