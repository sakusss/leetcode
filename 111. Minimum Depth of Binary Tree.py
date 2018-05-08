# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:return 0
        if root.left == None and root.right!=None: return self.minDepth(root.right)+1
        if root.right == None and root.left!= None : return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
        
   ## 这道题是判断最小深度，所以必须增加一个叶子的判断（因为如果有一个节点
   如果只有左子树或者右子树，我们就不能取它左右子树中最小的作为深度，因为
   那样结果是0，我们只有在叶子节点才能判断深度，而在求最大深度的时候，因为
   一定会取大的那个，所以不会有问题），递归比max多一个左右子树的判断。
  ##非递归解法同样采用层序遍历(相当于图的BFS），只是在检测到第一个叶子的时候就可以返回了，代码如下： 
