class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    def insert(self, data):
        if self.root is None:
            self.root =Node(data) #terá um novo Node 
        else:
            self._insert_recursive(data, self.root) #chama a função recursiva verificando se é maior ou menor que o nó atual
        # Se o nó atual for None, cria um novo nó com o dado fornecido e o retorna

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)

        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root) #chama a função recursiva verificando se é maior ou menor que o nó atual
    
    def _search_recursive(self, data, node):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)
        
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)
print("Search 4:", tree.search(4))  # False
print("Search 7:", tree.search(7))  # True