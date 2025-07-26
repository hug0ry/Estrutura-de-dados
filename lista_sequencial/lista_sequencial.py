class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade  # cria uma lista "vazia" com tamanho fixo
        self.tamanho = 0  # contador de quantos elementos realmente estão na lista

def esta_vazia(self):
    return self.tamanho == 0

def esta_cheia(self):
    return self.tamanho == self.capacidade

def obter_tamanho(self):
    return self.tamanho

def obter_elemento(self, posicao):
    if posicao < 1 or posicao > self.tamanho:
        raise IndexError("Posição inválida")
    return self.dados[posicao - 1]

def modificar_elemento(self, posicao, valor):
    if posicao < 1 or posicao > self.tamanho:
        raise IndexError("Posição inválida")
    self.dados[posicao - 1] = valor

def inserir(self, posicao, valor):
    if self.esta_cheia():
        raise OverflowError("Lista cheia")
    if posicao < 1 or posicao > self.tamanho + 1:
        raise IndexError("Posição inválida")

    # Move os elementos para a direita
    for i in range(self.tamanho, posicao - 1, -1):
        self.dados[i] = self.dados[i - 1]

    self.dados[posicao - 1] = valor
    self.tamanho += 1

def remover(self, posicao):
    if self.esta_vazia():
        raise IndexError("Lista vazia")
    if posicao < 1 or posicao > self.tamanho:
        raise IndexError("Posição inválida")

    valor_removido = self.dados[posicao - 1]

    # Move os elementos para a esquerda
    for i in range(posicao - 1, self.tamanho - 1):
        self.dados[i] = self.dados[i + 1]

    self.dados[self.tamanho - 1] = None
    self.tamanho -= 1

    return valor_removido

from lista_sequencial import ListaSequencial

def testar_lista():
    print("=== Testando Lista Sequencial ===")

    lista = ListaSequencial(5)
    
    print("Inserindo 10 na posição 1")
    lista.inserir(1, 10)
    assert lista.obter_elemento(1) == 10

    print("Inserindo 20 na posição 2")
    lista.inserir(2, 20)
    assert lista.obter_elemento(2) == 20

    print("Inserindo 15 na posição 2")
    lista.inserir(2, 15)
    assert lista.obter_elemento(2) == 15
    assert lista.obter_elemento(3) == 20

    print("Modificando valor da posição 1 para 5")
    lista.modificar_elemento(1, 5)
    assert lista.obter_elemento(1) == 5

    print("Removendo elemento da posição 2")
    removido = lista.remover(2)
    assert removido == 15
    assert lista.obter_elemento(2) == 20

    print("Verificando tamanho da lista")
    assert lista.obter_tamanho() == 2

    print("Verificando se a lista está vazia")
    assert not lista.esta_vazia()

    print("Preenchendo lista")
    lista.inserir(3, 30)
    lista.inserir(4, 40)
    lista.inserir(5, 50)
    assert lista.esta_cheia()

    print("Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    testar_lista()
