def resolver_labirinto(labirinto, inicio, tesouro):
    visitados = set()
    pilha = [inicio]
    caminho = []
    
    while pilha:
        linha, coluna = pilha.pop()
        
        if (linha, coluna) == tesouro:
            caminho.append((linha, coluna))
            return True, caminho
        
        if (linha, coluna) not in visitados:
            visitados.add((linha, coluna))
            caminho.append((linha, coluna))
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = linha + di, coluna + dj
                if (0 <= ni < len(labirinto) and 0 <= nj < len(labirinto[0]) and 
                    labirinto[ni][nj] != '#' and (ni, nj) not in visitados):
                    pilha.append((ni, nj))
    
    return False, caminho

def main():
    # Definindo o labirinto
    labirinto = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', 'J', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '.', 'T', '#'],
        ['#', '#', '#', '#', '#', '#', '#']
    ]
    
    # Encontrando posições
    inicio = None
    tesouro = None
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 'J':
                inicio = (i, j)
            elif labirinto[i][j] == 'T':
                tesouro = (i, j)
    
    if not inicio or not tesouro:
        print("Posição inicial ou tesouro não encontrado!")
        return
    
    # Resolvendo o labirinto
    sucesso, caminho = resolver_labirinto(labirinto, inicio, tesouro)
    
    # Exibindo resultados
    if sucesso:
        print("Tesouro encontrado! Caminho percorrido:")
        for passo in caminho:
            print(f"({passo[0]}, {passo[1]})", end=" -> ")
        print("FIM")
    else:
        print("Não foi possível encontrar o tesouro!")

if __name__ == "__main__":
    main()