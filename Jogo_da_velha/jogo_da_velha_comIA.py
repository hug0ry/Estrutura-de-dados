 # -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
      
        M = self.matriz
        meu = self.tipo
        oponente = Tabuleiro.JOGADOR_X if meu == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

        def linhas():
            for i in range(3):
                yield [(i, 0), (i, 1), (i, 2)]  
                yield [(0, i), (1, i), (2, i)]  
            yield [(0, 0), (1, 1), (2, 2)] 
            yield [(0, 2), (1, 1), (2, 0)]  

        # R1: Completar ou bloquear
        for tripla in linhas():
            vals = [M[l][c] for l, c in tripla]
            if vals.count(meu) == 2 and vals.count(Tabuleiro.DESCONHECIDO) == 1:
                return tripla[vals.index(Tabuleiro.DESCONHECIDO)]
            if vals.count(oponente) == 2 and vals.count(Tabuleiro.DESCONHECIDO) == 1:
                return tripla[vals.index(Tabuleiro.DESCONHECIDO)]

        # R2: Criar duas ameaças
        jogadas_possiveis = [(l, c) for l in range(3) for c in range(3) if M[l][c] == Tabuleiro.DESCONHECIDO]
        for l, c in jogadas_possiveis:
            M[l][c] = meu
            duplas = 0
            for tripla in linhas():
                vals = [M[i][j] for i, j in tripla]
                if vals.count(meu) == 2 and vals.count(Tabuleiro.DESCONHECIDO) == 1:
                    duplas += 1
            M[l][c] = Tabuleiro.DESCONHECIDO
            if duplas >= 2:
                return (l, c)

        # R3: Centro
        if M[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Canto oposto
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        opostos = {(0, 0): (2, 2), (0, 2): (2, 0), (2, 0): (0, 2), (2, 2): (0, 0)}
        for c in cantos:
            if M[c[0]][c[1]] == oponente:
                op = opostos[c]
                if M[op[0]][op[1]] == Tabuleiro.DESCONHECIDO:
                    return op

        # R5: Canto livre
        for c in cantos:
            if M[c[0]][c[1]] == Tabuleiro.DESCONHECIDO:
                return c

        # R6: Arbitrária
        if jogadas_possiveis:
            return jogadas_possiveis[0]
        return None
