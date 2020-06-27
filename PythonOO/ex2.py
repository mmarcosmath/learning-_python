#Faça um Programa que leia um vetor de 10 números reais
#e mostre-os na ordem inversa.


def lendo_vetor():
    vetor = []
    for x in range(10):
        vetor.append(int(input("Digite um numero: ")))
    return vetor
        

vetor = lendo_vetor()
#vetor.reverse()#metodo 1
vetor = vetor[::-1]#metodo 2
print(vetor)
