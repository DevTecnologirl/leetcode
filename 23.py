# heapq exige que os elementos sejam comparáveis. Como ListNode não tem comparação padrão, 
# usamos tupla (valor, índice, nó) para garantir ordenação estável.
# dummy é um nó inicial fictício que facilita o retorno do resultado.

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Para imprimir a lista ligada de forma amigável (opcional)
    def __str__(self):
        result = []
        while self:
            result.append(str(self.val))
            self = self.next
        return "->".join(result)

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        heap = []

        # Inserimos o primeiro nó de cada lista na heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
# Construindo listas [1->4->5], [1->3->4], [2->6]
a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))

lists = [a, b, c]

sol = Solution()
merged = sol.mergeKLists(lists)
print(merged)  # Saída: 1->1->2->3->4->4->5->6
