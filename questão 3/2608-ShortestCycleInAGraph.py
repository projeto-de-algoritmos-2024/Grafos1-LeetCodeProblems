from collections import defaultdict
from collections import deque
#O código começa construindo o grafo usando o defaultdict da biblioteca collections. Cada vértice é uma chave, 
#e os valores associados a essa chave são listas dos vértices adjacentes (vértices conectados por uma aresta).
#A lista de arestas edges é processada, e para cada aresta [v, w], os vértices v e w são adicionados como vizinhos um do outro no grafo G.

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for v, w in edges:
            G[v].append(w)
            G[w].append(v)
        self.res = float('inf')
        #A função bfs faz uma busca em largura a partir de um vértice inicial v, que representa um ponto de partida para detectar ciclos no grafo.
        def bfs(v):
            level = defaultdict(int)
            #level: armazena o nível de profundidade de cada vértice a partir do vértice inicial. Esse nível ajuda a verificar a distância percorrida até cada vértice.
            visited = set()
            #visited: um conjunto que armazena os vértices já visitados para evitar visitas duplicadas.
            que = deque([(v,0)])
            #que: uma fila deque usada para processar os vértices camada por camada na BFS.
            while que:
                v, d = que.popleft()
                if v in visited: continue
                visited.add(v)
                level[v] = d
                parents = set()
                for w in G[v]:
                    if w in visited:
                        if level[w] == d-1:
                            parents.add(w)
                            if len(parents) == 2:
                                self.res = min(self.res, 2*d)
                                return
                        if level[w] == d:
                            self.res = min(self.res, 2*d + 1)
                    else:
                        que.append((w,d+1))
        for v in range(n):
            bfs(v)
        return self.res if self.res != float('inf') else -1