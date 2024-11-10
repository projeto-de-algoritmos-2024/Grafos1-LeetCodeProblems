class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        # a func recebe um array edges que representa o grafo direcionado.
        n=len(edges)
        # n é o número total de nós no grafo, que corresponde ao comprimento do array edges.
        ind=[0]*n
        # ind é um array de tamanho n, onde cada posição ind[i] armazenará a "edge score" do nó i. Inicialmente, todos os valores são 0.
        for x in range(n):
            ind[edges[x]]+=x
        #Este loop percorre todos os nós no grafo. Para cada nó x, ele incrementa o valor ind[edges[x]] adicionando x. 
        m=0 
        i=0
        for x in range(n):
            if ind[x]>m:
                m=ind[x]
                i=x
        #O loop percorre todos os nós, verificando se a edge score de ind[x] é maior do que m. 
        #Se for, ele atualiza m e define i como o índice atual x. Isso garante que, se houver empate na edge score, o índice menor seja retornado.
        
        return i