# Dado um nó de referência em um grafo não direcionado e conectado, retorne uma cópia profunda (deep copy) do grafo.
# Cada nó tem um valor inteiro e uma lista de vizinhos (neighbors).
#BFS
# from collections import deque

# def cloneGraph(node):
#     if not node:
#         return None

#     visitado = {node: Node(node.val)}
#     fila = deque([node])

#     while fila:
#         no = fila.popleft()
#         for vizinho in no.neighbors:
#             if vizinho not in visitado:
#                 visitado[vizinho] = Node(vizinho.val)
#                 fila.append(vizinho)
#             visitado[no].neighbors.append(visitado[vizinho])

#     return visitado[node]


#DFS
# def cloneGraph(node):
#     if not node:
#         return None

#     visitado = {}

#     def dfs(no):
#         if no in visitado:
#             return visitado[no]

#         copia = Node(no.val)
#         visitado[no] = copia

#         for vizinho in no.neighbors:
#             copia.neighbors.append(dfs(vizinho))

#         return copia

#     return dfs(node)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None

    visitado = {}

    def dfs(no):
        if no in visitado:
            return visitado[no]

        copia = Node(no.val)
        visitado[no] = copia

        for vizinho in no.neighbors:
            copia.neighbors.append(dfs(vizinho))

        return copia

    return dfs(node)

# Função auxiliar para imprimir o grafo (em largura)
from collections import deque

def imprimir_grafo(node):
    visitados = set()
    fila = deque([node])
    while fila:
        atual = fila.popleft()
        if atual in visitados:
            continue
        visitados.add(atual)
        print(f"Nó {atual.val} -> {[vizinho.val for vizinho in atual.neighbors]}")
        for vizinho in atual.neighbors:
            if vizinho not in visitados:
                fila.append(vizinho)

# 🔧 Construindo o grafo de exemplo:
# Grafo:
# 1 -- 2
# |    |
# 4 -- 3

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

# ✅ Clonando o grafo
copia = cloneGraph(n1)

print("🔍 Grafo Original:")
imprimir_grafo(n1)

print("\n🧬 Grafo Clonado:")
imprimir_grafo(copia)

# 🧪 Verificando se são nós diferentes (endereços diferentes)
print("\n📎 Verificação de identidade dos nós (não devem ser iguais):")
print(f"n1 is copia? {n1 is copia}")                    # Esperado: False
print(f"n1.val == copia.val? {n1.val == copia.val}")    # Esperado: True
print(f"n1.neighbors[0] is copia.neighbors[0]? {n1.neighbors[0] is copia.neighbors[0]}")  # Esperado: False
