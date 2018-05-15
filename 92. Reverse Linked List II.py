class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p=dummy
        for i in range(m-1):
            p = p.next
        
        curr  = p.next
        for i in range(n-m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = p.next
            p.next = tmp
        
        return dummy.next
        
 -----相当于把curr后面的节点不断移到p的节点后面，就是相当于
 不妨拿出四本书，摞成一摞（自上而下为 A B C D），要让这四本书的位置完全颠倒过来（即自上而下为 D C B A）：

盯住书A，每次操作把A下面的那本书放到最上面

初始位置：自上而下为 A B C B

第一次操作后：自上而下为 B A C D

第二次操作后：自上而下为 C B A D

第三次操作后：自上而下为 D C B A
时间复杂度为O（n）,空间复杂度为O（1）
相当于不断插入
