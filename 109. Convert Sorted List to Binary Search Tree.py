class Solution:
    def sortedListToBST(self,head):
        array=[]
        p=head
        while p:
            array.append(p.val)
            p=p.next
        return self.sortedArrayToBST(array)
    
    def sortedArrayToBST(self, array):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if len(array)==0: return None
        if len(array)==1: return TreeNode(array[0])
        m=len(array)//2
        root = TreeNode(array[m])
        root.left=self.sortedArrayToBST(array[:m])
        root.right=self.sortedArrayToBST(array[m+1:])
        return root
        
        ###两个思路：一，可以使用快慢指针来找到中间的那个节点，然后将这个节点作为树根，并分别递归这个节点左右两边的链表产生左右子树，这样的好处是不需要使用额外的空间，坏处是代码不够整洁。二，将排序好的链表的每个节点的值存入一个数组中，这样就和http://www.cnblogs.com/zuoyuan/p/3722103.html这道题一样了，代码也比较整洁。
        #-------------------------------中序遍历---------------------------------
        我们需要取中点作为当前函数的根。这里的问题是对于一个链表我们是不能常量时间访问它的中间元素的。这时候就要利用到树的中序遍历了，按照递归中序遍历的顺序对链表结点一个个进行访问，而我们要构造的二分查找树正是按照链表的顺序来的。思路就是先对左子树进行递归，然后将当前结点作为根，迭代到下一个链表结点，最后在递归求出右子树即可。整体过程就是一次中序遍历，时间复杂度是O(n)，空间复杂度是栈空间O(logn)。
        
