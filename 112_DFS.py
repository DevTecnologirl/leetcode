class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left and targetSum == root.val: #resulta em 0
            return True

        return self.hasPathSum(root, left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)