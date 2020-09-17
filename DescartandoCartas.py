# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:44:05 2020

@author: matheus
"""

import numpy as np

class Fila:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.__valores = np.empty(self.tamanho, dtype=int)
        
    def fila_vazia(self):
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_elementos == self.tamanho
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila está cheia')
            return
        
        if self.final == self.tamanho -1:
            self.final = -1
        self.final += 1
        self.__valores[self.final] = valor
        self.numero_elementos += 1
        
    
    def desenfileirar(self):
        if self.fila_vazia():
            print('Fila está vazia')
            return
        
        temp = self.__valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.tamanho:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp
    
    def primeiro(self):
        if self.fila_vazia():
            return -1
        return self.__valores[self.inicio]
    
            
n = int(input('Digite o número de cartas: '))
baralho = []
fila = Fila(n)
descartadas = []

if n >= 2:
    
    for i in range(n):
        cont = i+1
        baralho.append(cont)
    
    for x in baralho:
        carta = x
        fila.enfileirar(carta) 
        x += 1
        
    for y in baralho:
        if fila.numero_elementos > 1:
            
            if not fila.fila_vazia():
                descartadas.append(fila.primeiro())
                fila.desenfileirar()
                
                if not fila.fila_vazia():
                    movida = fila.primeiro()
                    fila.enfileirar(movida)
                    
                if not fila.fila_vazia():
                    fila.desenfileirar()
                    y = y + 1
         
    restante = fila.primeiro() 
                        
    print('Descartadas',descartadas,'\nRestante:',restante)
    

else:
    print('Poucas cartas no baralho!')
    
    
    
    
    
