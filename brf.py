#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:44:31 2017

@author: alef1
"""
import math as m
################################################
####    rede RBF para comparar com a mlp    ####
####    camada oculta u = ||Xi - Ti||       ####
####    camada saida  u = S(Wi*Thei||Xi - Ti||##
####        
####    theta(v) = exp (-(v²/2sigma²))
####
####
################################################
#v = x - u; x vetor de entrada; u centro da função radial; sigma largura da função radial
def funcao_gaussiana(t,x):
    soma = 0
    for i in range(len(t)):
        soma += (x[i] - t[i])**2
    return 2.7182818284**(-soma)


def main():
    pesos = [-0.5,-0.5,0.9]
    ts  = [[0,0],[1,1]]
    mat_entrada = [[0,0],[0,1],[1,0],[1,1]]
    saida = [0,1,1,0]
    #mat_saida   = [[0],[1],[1],[0]]
    q = []
    for j in range(len(mat_entrada)):
        p = []
        print("entradas: ",mat_entrada[j])
        for i in range(len(mat_entrada[j])):
           p.append(funcao_gaussiana(ts[i],mat_entrada[j]))
        q.append(p)
    print("transformada: ",q)
    #adaline
    novos =  treino(pesos,q,saida,mat_entrada)
    teste(novos,q,saida)
        
def treino(pesos,q,saida,mat):
    for epoca in range(100):
        for i in range(len(q)):
            net = somatorio(pesos, q[i])
            y = f(net)
            erro = saida[i] - y
            for j in range(len(pesos)-1):
                pesos[j] += 0.2*erro*q[i][j]
    return pesos
def teste(pesos, testes,saida):
     for i in range(4):
         net = somatorio(pesos, testes[i])
         y = f(net)
         print("Class do teste",i," y = ",y," esperado era = ",saida[i])

def somatorio(pesos, entradas):
    soma = 0;
    for i in range(len(pesos)-1):
        soma += pesos[i]*entradas[i]    
    #theta associado ao neuronio
    soma += pesos[len(pesos)-1]
    return soma

def f(net):
    if(net > 0.5):
        return 1
    return 0
    
    
if __name__ == "__main__":
    main()    
    
'''
    Pseudo -- código
    1. Inicialização do vetor peso
        Para j <-- 1 ate m faça wj <-- 0
    2. Atualização dos pesos
        Para n <-- 1 até Maxciclos faça
            Para i <-- 1 até p faça
                yi(n) <-- Somat wj neurj (Xi)
                Para j=1 até m faça
                    wj <-- wj + n(t – yi(n)) neurj(xi)
                Fim_para
            Fim_para
        Fim_para
'''

