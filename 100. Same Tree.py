# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p== None and q == None : 
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
        
      ## 这道题是树的题目，属于最基本的树遍历的问题。问题要求就是判断两个树是不是一样，基于先序，中序或者后序遍历都可以做完成，
   ## 因为对遍历顺序没有要求。
    ##这里我们主要考虑一下结束条件，1.如果两个结点都是null，也就是到头了，那么返回true。
    2.如果其中一个是null，说明在一棵树上结点到头，另一棵树结点还没结束，即树不相同，
    3.或者两个结点都非空，并且结点值不相同，返回false。
    4.最后递归处理两个结点的左右子树，返回左右子树递归的与结果即可。
     ##   这里使用的是先序遍历，算法的复杂度跟遍历是一致的，如果使用递归，时间复杂度是O(n)，空间复杂度是O(logn)。
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p== None and q == None : return True
        if p== None or q==None: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
