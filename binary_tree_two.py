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
        
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node: # se tiver node ele vai adicionar o nó na lista result
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)


    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node: # se tiver node ele vai adicionar o nó na lista result
            self._inorder_recursive(node.left, result)
            result.append(node.data) #MUDANÇA NO INORDER 
            self._inorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node: # se tiver node ele vai adicionar o nó na lista result
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data) #MUDANÇA NO POSTORDER 

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(7)
#print("Search 4:", tree.search(4))  # False
#print("Search 7:", tree.search(7))  # True
print("Preorder Traversal:", tree.preorder_traversal())  # [10, 5, 3, 7, 15, 12, 18]
print("Inorder Traversal:", tree.inorder_traversal())  # [3, 5, 7, 10, 12, 15, 18]
print("Postorder Traversal:", tree.postorder_traversal())  # [3, 7, 5, 12, 18, 15, 10]