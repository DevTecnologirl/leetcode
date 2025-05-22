# Dado um array de inteiros nums e um inteiro k, retorne os k elementos mais frequentes.
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Contar a frequência de cada número
        count = Counter(nums)
        
        # Usar uma min heap para manter os k maiores frequentes
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extrair apenas os números (desprezando as frequências)
        return [num for freq, num in heap]
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))  # Saída: [1, 2]
print(sol.topKFrequent([1], 1))           # Saída: [1]
