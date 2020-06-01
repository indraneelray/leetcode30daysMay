# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            rn = TreeNode(root.val)
        else:
            return None
        if root.right:
            rn.left = self.invertTree(root.right)
        if root.left:
            rn.right = self.invertTree(root.left)
        return rn
        
