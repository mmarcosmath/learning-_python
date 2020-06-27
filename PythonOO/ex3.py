#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
import functools as ft

def lendo_vetor():
    vetor = []
    for x in range(4):
        vetor.append(float(input("Digite a {}º nota: " .format(x+1))))
    return vetor
        

def main():
    vetor = lendo_vetor()
    print("Notas: ",vetor)
    #media = (vetor[0]+vetor[1]+vetor[2]+vetor[3])/4 #metodo 1
    media = ft.reduce(lambda x,y: x+y,vetor)/4 #metodo 2
    print("Media: ",media)
    


main()
