# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next=head
        pre,curr = dummy,head
        while curr and curr.next:
            pre.next = curr.next
            curr.next = pre.next.next 
            pre.next.next = curr
            pre,curr = curr , curr.next
        return dummy.next
        
        这道题中用了一个辅助指针作为表头，这是链表中比较常用的小技巧，因为这样可以避免处理head的边界情况，一般来说要求的结果表头会有变化的会经常用这个技巧，大家以后会经常遇到。
因为这是一遍过的算法，时间复杂度明显是O(n)，空间复杂度是O(1)。

这道题考察了基本的链表操作，注意当改变指针连接时，要用一个临时指针指向原来的next值，否则链表丢链，无法找到下一个值。 

本题的解题方法是：

需要运用fakehead来指向原指针头，防止丢链，用两个指针，ptr1始终指向需要交换的pair的前面一个node，ptr2始终指向需要交换的pair的第一个node。

 然后就是进行链表交换。

需要用一个临时指针nextstart， 指向下一个需要交换的pair的第一个node，保证下一次交换的正确进行。

然后就进行正常的链表交换，和指针挪动就好。 

 当链表长度为奇数时，ptr2.next可能为null；

 当链表长度为偶数时，ptr2可能为null。

所以把这两个情况作为终止条件，在while判断就好，最后返回fakehead.next。

画图画图画图
pre指的是应该交换的pair的前一个节点，curr是应该交换的第一个节点，理清楚交换的顺序
