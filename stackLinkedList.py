class Node: #valor da linkedi list que ira apontar para o proximo
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack: 
    def __init__(self):
        self.top = None
        self._size = 0 

    def push(self, item): #recebe um item e adiciona na pilha
        new_node = Node(item)
        new_node.next = self.top #aponta o novo nó para o topo
        self.top = new_node #atualiza o topo para o novo nó que esta no topo
        self._size += 1
    def pop(self): #remove o último item da pilha
        if self.top is None:
            raise IndexError("pop from empty list")
        
        popped_node = self.top
        self.top = popped_node.next #atualiza o topo para o próximo nó
        self._size -= 1 
        return popped_node.value
    
    def peek(self): #remove o último item da pilha
       if self.top is None:
            raise IndexError("pop from empty list")
       return self.top.value
    
    def size(self):
        return self._size
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) # 3
print(stack.peek()) # 2
print(stack.size()) # 2
print(stack.pop()) # 2
print(stack.pop()) # 1

