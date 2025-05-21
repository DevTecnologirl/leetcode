#min stack - possibilitar encontrar o menor elemento O(1)
class MinStack:
    def __init__(self):
        self.stack = [] # algo pra armazenar = array (pegar o minimo, precisamos saber a posição)
        self.minStack = []

    def push(self, val: int) -> None: #Adicionar elementos 
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1], val)
        self.minStack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]
