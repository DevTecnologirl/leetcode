# Leetcode 200 – Number of Islands
# Dado um mapa 2D (matriz) representado por '1' (terra) e '0' (água), conte quantas "ilhas" existem.
# Uma ilha é um grupo de '1's conectados horizontal ou verticalmente (não diagonalmente), cercado por água ou pelas bordas da matriz.
# A matriz é do tipo: List[List[str]].

#  Solução: DFS (ou BFS)
# A ideia é:
# Fazer um DFS ou BFS para explorar cada '1' conectado.
# Após visitar uma célula '1', marcá-la como visitada (por exemplo, alterando para '0').
# Toda vez que acharmos um '1' novo, significa que uma nova ilha começou, então aumentamos o contador.
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Verificações de limites e se é água ou já visitado
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # Marca como visitado
            # Explora vizinhos
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1  # Nova ilha
                    dfs(r, c)     # Marca toda a ilha

        return islands
