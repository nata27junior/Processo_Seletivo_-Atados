# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:51:29 2019

@author: Natanael
"""

""" Problema

Um isograma é uma palavra que não tem letras repetidas, consecutivas ou não consecutivas.
Implemente uma função que determine se uma string que contém apenas letras é um isograma e retorne um booleano,
 indicando True para um isograma e False para não-isogramas.
Suponha que a string vazia seja um isograma. Ignore o caso de letra (case insensitive).

### Exemplos:
```
is_isogram("Dermatoglyphics" ) ==> True
is_isogram("aba" )             ==> False
is_isogram("mo0se" )           ==> False # existe um número
"""


def is_isogram(text):
    """
    -> Função que testa uma string se é um isograma e retorna um boleano
    :param text: string a ser testada
    :return: retorna boleano se é ou não uma string isograma
    """
    text = text.lower()
    if text.isalpha():
        if len(set(text)) == len(text):
            # o set(text) faz uma lista com todas as letras da palavra
            # é comparado o tamanho da lista e o tamanho da palavra
            return True
        else:
            return False
    else:
        return False


# Programa Principal

print("Pernambuco ",is_isogram("Pernambuco"))
print("ADVISOR ",is_isogram("ADVISOR"))
print("Dermatoglyphics ",is_isogram("Dermatoglyphics"))
print("aba ",is_isogram("aba"))
print("mo0se ",is_isogram("mo0se"))
print("Ar@r@ ",is_isogram("Ar@r@"))
print("ArArA ",is_isogram("ArArA"))
print("INVADER ",is_isogram("INVADER"))
print("Invasor ",is_isogram("Ivasor"))
print("!nv@s0r ",is_isogram("!v@s0r"))

