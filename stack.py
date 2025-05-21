class Stack: 
    def __init__(self):
        self.items = [0]*max_leght #inicializa a pilha com 0
        self.max_lenght = max_leght
        self.pointer = 0 #inicializa o ponteiro com 0


    def push(self, item): #recebe um item e adiciona na pilha
        self.items(self.pointer) = item #adiciona o item na pilha
        self.pointer += 1

    def pop(self): #remove o último item da pilha
        if not len(self.items): #verifica se a pilha não está vazia
            raise IndexError("pop from empty list")
        return self.items.pop()
    
    def peek(self): #remove o último item da pilha
        if not len(self.items): #verifica se a pilha não está vazia
            raise IndexError("peek from empty list")
        return self.items[-1]
    
    def size(self):
        return self.pointer