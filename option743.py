import heapq
from typing import List

class Solution:
    def timeToNode(self, times: List[List[int]], n: int, k: int, target: int = 4) -> int:
        # Construir grafo como um dicionário de adjacência
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = {}
            graph[u][v] = w
        
        # Inicializar heap e distâncias
        min_heap = [(0, k)]  # (distância, nó)
        distances = {k: 0}

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if node == target:
                return dist  # Chegou ao destino

            if node in graph:
                for neighbor, weight in graph[node].items():
                    new_dist = dist + weight
                    if new_dist < distances.get(neighbor, float('inf')):
                        distances[neighbor] = new_dist
                        heapq.heappush(min_heap, (new_dist, neighbor))

        # Se não alcançou o destino
        return -1
