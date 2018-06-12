# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None : return None
        dummy = ListNode(0)
        dummy.next = head
        
        curr = head
        
        while curr.next:
            
            if curr.next.val < curr.val:
                
                pre = dummy
                
                while pre.next.val < curr.next.val:
                    
                    pre = pre.next
                
                temp = curr.next
                
                curr.next = curr.next.next 
                
                temp.next = pre.next
                
                pre.next = temp
                
            else:
                
                curr = curr.next
        
        return dummy.next
                
                
            
    ## 插入排序，首先找到要插进去的结点，然后找到要插的地方，所以需要两个节点
    ## 找到要插的结点是通过结点的是否升序判定的，找到要插的地方是判断前一个值和后一个值和已经找到的该节点的比较
    ## 最坏时间复杂度是O(N^2)，最好时间复杂度是O(n)相当于遍历一遍，所以平均时间复杂度是O(N^2)
        
