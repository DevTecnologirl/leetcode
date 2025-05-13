#inorder = [9.3.15.20.7]
#postorder = [9,15,7,20,3]
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        inorder_index = inorder.index(root.val) # = 1

        root.right = self.buildTree(inorder[inorder_index + 1:], postorder) # = [20]
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        return root