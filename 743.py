import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Criar grafo como dicionário de adjacência
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = {}
            graph[u][v] = w
        
        # Dicionário para armazenar menor tempo até cada nó
        distances = {}
        min_heap = [(0, k)]  # (tempo atual, nó)

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in distances:
                continue  # já visitado

            distances[node] = time

            for neighbor in graph.get(node, {}):
                if neighbor not in distances:
                    new_time = time + graph[node][neighbor]
                    heapq.heappush(min_heap, (new_time, neighbor))

        # Se nem todos os nós foram alcançados
        if len(distances) != n:
            return -1

        # O tempo máximo necessário para alcançar todos os nós
        return max(distances.values())
