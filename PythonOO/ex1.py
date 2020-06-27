#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.


def lendo_vetor():
    vetor = []
    for x in range(5):
        vetor.append(int(input("Digite um numero: ")))
    return vetor
        

vetor = lendo_vetor()
print(vetor)
