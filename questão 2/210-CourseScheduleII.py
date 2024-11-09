from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Inicializa um dicionário de lista para armazenar o grafo dos cursos e suas dependências
        grafo = defaultdict(list)
        
        # Inicializa uma lista para contar os pré-requisitos de cada curso (grau de entrada)
        grauEntrada = [0] * numCourses

        # Constrói o grafo e preenche o grau de entrada para cada curso
        for curso, prereq in prerequisites:
            grafo[prereq].append(curso)  # Adiciona uma aresta de 'prereq' para 'curso'
            grauEntrada[curso] += 1  # Incrementa o grau de entrada do curso
        
        # Inicializa uma fila para armazenar cursos que podem ser realizados (grau de entrada zero)
        fila = deque()
        for i in range(numCourses):
            if grauEntrada[i] == 0:  # Se o curso não tiver pré-requisitos
                fila.append(i)  # Adiciona à fila para processamento
        
        # Lista para armazenar a ordem de conclusão dos cursos
        ordemCursos = []

        # Realiza a BFS enquanto houver cursos na fila
        while fila:
            cursoAtual = fila.popleft()  # Remove o primeiro curso da fila
            ordemCursos.append(cursoAtual)  # Adiciona o curso à ordem de conclusão
            
            # Para cada curso dependente do curso atual
            for cursoDependente in grafo[cursoAtual]:
                grauEntrada[cursoDependente] -= 1  # Reduz o grau de entrada desse curso
                if grauEntrada[cursoDependente] == 0:  # Se não houver pré-requisitos restantes
                    fila.append(cursoDependente)  # Adiciona o curso dependente à fila
        
        # Verifica se todos os cursos foram incluídos na ordem de conclusão
        if len(ordemCursos) == numCourses:
            return ordemCursos  # Retorna a ordem dos cursos se possível completar todos
        else:
            return []  # Retorna lista vazia se houver ciclo (impossível completar todos)
