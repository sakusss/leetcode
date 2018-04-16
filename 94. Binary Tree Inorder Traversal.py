# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.iterative_inorder(root,res)
        return res
        
        
    def iterative_inorder(self,root,res):
        stack = []
        while root or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
    
    def recursive_inorder(self,root,res):
        if root:
            self.recursive_inorder(root.left,res)
            res.append(root.val)
            self.recursive_inorder(root.right,res)
            
