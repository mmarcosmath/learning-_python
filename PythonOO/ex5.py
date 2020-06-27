# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#  Armazene os números pares no vetor PAR e os números
# IMPARES no vetor impar. Imprima os três vetores


def ler_vetor():
    vetor = []
    for x in range(10):
        vetor.append(int(input("Digite um numero: ")))
    return vetor


def separa(vetor):
    vi, vp = [], []
    for x in range(len(vetor)):
        if vetor[x] % 2 == 0:
            vp.append(vetor[x])
            continue
        vi.append(vetor[x])
    return vp, vi


def main():

    vetor = ler_vetor()
    print(vetor)
    print(separa(vetor))


main()
