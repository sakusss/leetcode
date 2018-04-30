# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
-----------------------------递归-----------------------------------

class Solution:
    def recursive_pre(self,root,res):
        if root:
            res.append(root.val)
            self.recursive_pre(root.left,res)
            self.recursive_pre(root.right,res)
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.recursive_pre(root,res)
        return res
  时间复杂度 O(N),空间复杂度O（logn），递归栈的大小
    ----------------------------迭代------------------------------------------
    算法时间复杂度也是O(n)，空间复杂度是栈的大小O(logn)。
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res =[]
        self.recursive_preorder(root,res)
        return res
    def iterative_preorder(self,root,res):
        stack=[]
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            else:
                root = stack.pop()
                root=root.right
        return res
          
  根据先序遍历的顺序，先访问根节点，再访问左子树，后访问右子树，而对于每个子树来说，又按照同样的访问顺序进行遍历，上图的先序遍历顺序为：ABDECF。非递归的实现思路如下：

对于任一节点P，

1）输出节点P，然后将其入栈，再看P的左孩子是否为空；

2）若P的左孩子不为空，则置P的左孩子为当前节点，重复1）的操作；

3）若P的左孩子为空，则将栈顶节点出栈，但不输出，并将出栈节点的右孩子置为当前节点，看其是否为空；

4）若不为空，则循环至1）操作；

5）如果为空，则继续出栈，但不输出，同时将出栈节点的右孩子置为当前节点，看其是否为空，重复4）和5）操作；

6）直到当前节点P为NULL并且栈空，遍历结束。
先序遍历：先沿最左侧通道自顶而下访问沿途节点，再自下而上依次遍历这些节点的右子树
简而言之，依次访问root结点，如果不是空，入栈，转到左子树，如果是空，则出栈，顺便遍历右子树。


--------------------morris traversal----------------------------------------------------------------------
最后使用Morris遍历方法，这个方法不需要为每个节点额外分配指针指向其前驱和后继结点，而是利用叶子节点中的右空指针指向中序遍历下的后继节点就可以了。具体的分析可以参见Binary Tree Inorder Traversal，中序和先序方法上是完全一样的，只是访问结点的时机不同而已。这种方法的缺陷在于会暂时性的改变结点的内容，从编程健壮性和封装性来说不是特别好（比如说传进来的树结点很可能是const的变量，不希望对它做任何改变）。时间复杂度和空间复杂度如同Binary Tree Inorder Traversal中分析的，分别是O(n)和O(1)。
