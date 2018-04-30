# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    def recursive_inordertraversal(self,root,res):
        if root:
            self.recursive_inordertraversal(root.left,res)
            res.append(root.val)
            self.recursive_inordertraversal(root.right,res)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[] 
        self.recursive_inordertraversal(root,res)
        return res
    
    递归版本 时间复杂度O（n），空间复杂度则是递归栈的大小O(logn）
    --------------------------------------------------------------
class Solution:
    
    def iterative_inordertraversal(self,root,res):
        stack=[]
        while stack or root:
            if root :
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res
                
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[] 
        self.iterative_inordertraversal(root,res)
        return res
  
  迭代版本 其实是用一个栈来模拟递归的过程，所以时间复杂度也是O(N),空间复杂度为栈的大小O(logn),过程中维护一个node表示当前走到的结点 
  维护了一个栈非递归的实现思路如下：

   对于任一节点P，

1）若P的左孩子不为空，则将P入栈并将P的左孩子置为当前节点，然后再对当前节点进行相同的处理；

2）若P的左孩子为空，则输出P节点，出栈，而后将P的右孩子置为当前节点，看其是否为空；

3）若不为空，则重复1）和2）的操作；

4）若为空，则执行出栈操作，输出栈顶节点，并将出栈的节点的右孩子置为当前节点，看起是否为空，重复3）和4）的操作；

5）直到当前节点P为NULL或者栈为空，则遍历结束。
                                  
简而言之，判定root是否为空，为空出栈，不为空则入栈，结果是出栈的顺序
 
                                  
      --------------------------------------------------------------------------------------------
                                  用常量空间进行中序遍历，这种方法叫做morris traversal，Morris遍历方法用了线索二叉树，这个方法不需要为每个节点额外分配指针指向其前驱和后继结点，
                                  而是利用叶子节点中的右空指针指向中序遍历下的后继节点就可以了。
算法具体分情况如下：
1. 如果当前结点的左孩子为空，则输出当前结点并将其当前节点赋值为右孩子。
2. 如果当前节点的左孩子不为空，则寻找当前节点在中序遍历下的前驱节点（也就是当前结点左子树的最右孩子）。
                                  接下来分两种情况：
 a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点（做线索使得稍后可以重新返回父结点）。然后将当前节点更新为当前节点的左孩子。
 b) 如果前驱节点的右孩子为当前节点，表明左子树已经访问完，可以访问当前节点。将它的右孩子重新设为空（恢复树的结构）。输出当前节点。当前节点更新为当前节点的右孩子。 

接下来我们来分析一下时间复杂度。咋一看可能会觉得时间复杂度是O(nlogn)，因为每次找前驱是需要logn，总共n个结点。但是如果仔细分析会发现整个过程中每条边最多只走2次，
一次是为了定位到某个节点，另一次是为了寻找上面某个节点的前驱节点，而n个结点的二叉树中有n-1条边，所以时间复杂度是O(2*n)=O(n)，仍然是一个线性算法。空间复杂度的话我们分析过了，只是两个辅助指针，所以是O(1)。
