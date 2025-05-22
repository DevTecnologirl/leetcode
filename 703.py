import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        # Mantém apenas os k maiores elementos
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # retorna 4
print(kthLargest.add(5))  # retorna 5
print(kthLargest.add(10)) # retorna 5
print(kthLargest.add(9))  # retorna 8
print(kthLargest.add(4))  # retorna 8
