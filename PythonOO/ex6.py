# Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
import functools as ft

def lendo_notas():
    vetor = []
    for x in range(2):
        vetor.append([])
        for y in range(4):
            vetor[x].append(float(input("Digite a {}ª nota aluno {}:" .format(y+1,x+1))))
    print(vetor)
    return vetor

def verifica_media(vetor):
    control = 0
    for x in range(2):
        if((ft.reduce(lambda x,y:x+y,vetor[x])/4)>=7):
            control+=1
    print(control," alunos obtiveram media maior ou igual a 7")
    return control


    



def main():
    print("Oi")
    vetor = lendo_notas()
    c = verifica_media(vetor)
    



main()