from typing import List

def diferem_por_um_caractere(palavra1, palavra2):
    """
    Verifica se duas palavras diferem por exatamente um caractere.
    Retorna True se diferem por um caractere, caso contrário, retorna False.
    """
    diferencas = 0
    for i in range(len(palavra1)):
        if palavra1[i] != palavra2[i]:
            diferencas += 1
            # Se já houve mais de uma diferença, retorna False imediatamente
            if diferencas > 1:
                return False
    return diferencas == 1


def construir_grafo(palavras):
    """
    Constrói o grafo em forma de lista de adjacências.
    Cada palavra é um nó, e há uma aresta entre duas palavras se diferirem por um caractere.
    """
    grafo = [[] for _ in range(len(palavras))]  # Lista de adjacência

    # Conecta palavras que diferem por um caractere
    for i in range(len(palavras)):
        for j in range(i + 1, len(palavras)):
            if diferem_por_um_caractere(palavras[i], palavras[j]):
                grafo[i].append(j)
                grafo[j].append(i)

    return grafo


def busca_bfs(grafo, inicio):
    """
    Realiza uma busca em largura (BFS) no grafo a partir do nó 'inicio'.
    Retorna um dicionário de pais que indica o caminho mais curto de cada nó a partir do 'inicio'.
    """
    distancia = {inicio: 0}  # Mapeia cada nó à distância mínima a partir de 'inicio'
    pais = {inicio: None}  # Mapeia cada nó aos nós pais no caminho mais curto
    fila = [inicio]  # Fila para a BFS

    while fila:
        no_atual = fila.pop(0)  # Remove o primeiro elemento da fila

        # Para cada vizinho do nó atual
        for vizinho in grafo[no_atual]:
            # Se o vizinho ainda não foi visitado
            if vizinho not in distancia:
                distancia[vizinho] = distancia[no_atual] + 1
                pais[vizinho] = [no_atual]  # Registra o nó atual como pai do vizinho
                fila.append(vizinho)  # Adiciona o vizinho à fila para visita futura
            elif distancia[vizinho] == distancia[no_atual] + 1:
                # Se encontramos outro caminho curto para o vizinho
                pais[vizinho].append(no_atual)

    return pais


def encontrar_caminhos(caminhos, caminho_atual, no_atual, pais, lista_palavras):
    """
    Função recursiva para traçar todos os caminhos mais curtos do nó 'no_atual' ao nó inicial usando o dicionário 'pais'.
    Adiciona cada caminho encontrado em 'caminhos'.
    """
    # Verifica se o nó atual tem um caminho para o início
    if no_atual not in pais:
        return  # Sai se não há pais definidos para este nó (ou seja, ele não é alcançável)

    # Se chegamos ao nó inicial
    if pais[no_atual] is None:
        caminho_atual.reverse()  # Inverte o caminho para a ordem correta
        caminhos.append(caminho_atual)  # Adiciona o caminho aos caminhos encontrados
        return

    # Para cada pai do nó atual, continua a construção do caminho
    for pai in pais[no_atual]:
        encontrar_caminhos(caminhos, caminho_atual + [lista_palavras[pai]], pai, pais, lista_palavras)


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Encontra todos os caminhos mais curtos de 'beginWord' para 'endWord' em 'wordList'.
        Retorna uma lista de listas, onde cada sublista representa um caminho.
        """
        # Se a palavra inicial não está na lista de palavras, adiciona
        if beginWord not in wordList:
            wordList.append(beginWord)

        # Se a palavra final não está na lista de palavras, não há solução
        if endWord not in wordList:
            return []

        # Índices das palavras inicial e final na lista de palavras
        indice_end = wordList.index(endWord)
        indice_begin = wordList.index(beginWord)

        # Constrói o grafo de palavras e executa a BFS para encontrar os pais de cada nó
        grafo = construir_grafo(wordList)
        pais = busca_bfs(grafo, indice_begin)

        # Verifica se o endWord foi alcançado pela BFS
        if indice_end not in pais:
            return []  # Se o endWord não foi alcançado, retorna uma lista vazia

        # Usa backtracking para encontrar todos os caminhos do 'endWord' ao 'beginWord'
        caminhos = []
        encontrar_caminhos(caminhos, [endWord], indice_end, pais, wordList)

        return caminhos
