class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # Facilita a visualização da lista encadeada
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


def find_middle(head):
    slow = head
    fast = head
    # Corrigido para que fast avance dois passos
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(list1, list2):
    head = Node(0)  # nó dummy
    tail = head

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next  # fora do if/else

    tail.next = list1 or list2  # anexa o resto da lista
    return head.next  # ignora o nó dummy


# Criação da lista ligada: 5 -> 9 -> 3 -> 1 -> 7
node_7 = Node(7)
node_1 = Node(1, next=node_7)
node_3 = Node(3, next=node_1)
node_9 = Node(9, next=node_3)
node_5 = Node(5, next=node_9)

# Teste da função find_middle
middle = find_middle(node_5)
print(f"Middle node: {middle.val}")  # Esperado: 3
