# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        m=len(nums)//2
        if len(nums)==0: return None
        if len(nums)==1: return TreeNode(nums[0])
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])
        return root
  
  ## 直接使用递归就行
  ## 注意特殊条件
  ## 时间复杂度为一次树遍历O(N)
  ## 栈空间O(logn)加上结果的空间O(n)，额外空间是O(logn)，总体是O(n)
  
  #也可以用二分查找来做一个有序数组转换成一颗二分查找树。
  #其实从本质来看，如果把一个数组看成一棵树（也就是以中点为根，左右为左右子树，依次下去）数组就等价于一个二分查找树。
  #所以如果要构造这棵树，那就是把中间元素转化为根，然后递归构造左右子树。所以我们还是用二叉树递归的方法来实现，以根作为返回值，每层递归函数取中间元素，
  #作为当前根和赋上结点值，然后左右结点接上左右区间的递归函数返回值。
  但是python的好处是可以取切片，就可以直接调用，不需要二分查找确定左右节点了
