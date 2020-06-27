# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:31:50 2020

@author: mmarc
"""

# Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.

import functools as ft


def ler_vetor():
    vetor = []
    for x in range(10):
        vetor.insert(0, input("Digite um caractere: "))
    print(vetor)
    return vetor


def verifica_consoantes(c):
    if c.lower() == 'a':
        return 0
    if c.lower() == 'e':
        return 0
    if c.lower() == 'i':
        return 0
    if c.lower() == 'o':
        return 0
    if c.lower() == 'u':
        return 0
    return 1


def main():
    vetor = ler_vetor()
    print(ft.reduce(lambda x, y: x+y, list(map(verifica_consoantes, vetor))))
    print(vetor)



main()
