# -*- coding: utf-8 -*-
"""


@author: Natanael
"""

""" Problema


Neste desafio queremos que vocês descubram a quantidade de buracos que existe nas letras que formam uma palavra.

Casos de teste de exemplo:

>>> num_buracos("Banana")
5
>>> num_buracos("olho")
2
>>> num_buracos("çzt")
0

Façam um script Python que tenha essa função e disponibilize ele via GitHub para podermos avaliar seu código.

Coisas extras (como TDD, BDD, linting e pep-8) são pontos extras muito bem vistos.
"""
import unittest

class Buracos():
    
    def num_buracos(palavra):
        """
        -> Função que testa uma string e retorna o numero de buracos
        :param palavra: string a ser testada
        :param buracos: quantidade de buracos
        :return: retorna buracos
        """
        buracos =0
        
        vogal={'a':1,'A':1, 'b':1,'B':2, 'e':1,"D":1,'d':1,"O":1,'o':1,"P":1,'p':1,"R":1,'g':1,'q':1,'Q':1}  
        for letra in palavra:
            if letra in vogal:
                buracos = buracos + vogal[letra]
        return buracos
    
class MyBuracosTest(unittest.TestCase):    
    def test_buracos(self):
        resultado = Buracos.num_buracos("Banana")
        self.assertEqual(5, resultado)
    
    
    def test_buracos2(self):         
        resultado = Buracos.num_buracos('banana')
        self.assertEqual(4, resultado)
    
    def test_buracos3(self):         
        resultado = Buracos.num_buracos('olho')
        self.assertEqual(2, resultado)
    
    def test_buracos4(self):         
        resultado = Buracos.num_buracos('çzt')
        self.assertEqual(0, resultado)

# Programa Principal
if __name__=='__main__':
    unittest.main()
    


