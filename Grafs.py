class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node #primeiro caso: node vazio 
       
        q = deque([node]) #primeiro item na fila de processamento
        clones = {}
        clones[node.val] = Node(node.val, []) #cria o clone do primeiro item
        while q:
            curr = q.popleft() # 1° remoção do primeiro item da fila
            curr_clone = clones[node.val] #pega o clone do item atual
            for n in curr.neighbors: # nao estao na fila, percorrendo os vizinhos 
                if n.val not in clones: #O(1)
                    clones[n.val] = Node(n.val, []) #2° criando os clones 
                    q.append(n)
                curr_clone.neighbors.append(clones[n.val]) # 3° adicionando os vizinhos do clone   
        return clones[node.val]
