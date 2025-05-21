import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph} # inicializa todas as distâncias como infinito
    distances[start] = 0  # distância do nó inicial para ele mesmo é 0

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items(): #acessando vizinhos de A
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
                0
    return distances
    

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
{"A": 0, "B": 1, "C": 3, "D": 4}