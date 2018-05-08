# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxdepth(self,root):
        if root == None :return 0
        return max(self.maxdepth(root.left),self.maxdepth(root.right))+1
    
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        maxdepth_left = self.maxdepth(root.left)
        maxdepth_right = self.maxdepth(root.right)
        if abs(maxdepth_left-maxdepth_right) <=1 :
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
        
 ## 平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于1.这实际上是AVL树
 的定义。首先写一个计算二叉树高度的函数，也就是计算最大深度的函数，二叉树高度定义：树为空
 时，高度为0，然后递归求解。高度计算函数实现后，递归求解每个节点的左右子树的高度差，如果有大于1的，
 returnFALSE,如果高度差小于等于1，则需要继续递归求解，思路要清楚。
 ## 时间复杂度为一次树的遍历O（n），空间复杂度为栈的高度O（logn）
