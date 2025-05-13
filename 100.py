# Você recebe as raízes de duas árvores binárias, p e q. O objetivo é determinar se elas são idênticas:
# Estrutura idêntica: Ambas as árvores devem ter a mesma estrutura (mesma quantidade de nós em cada nível).
# Valores idênticos: Os valores dos nós correspondentes devem ser iguais.
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
