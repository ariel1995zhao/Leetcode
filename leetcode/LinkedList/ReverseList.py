# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        temp = None 
        prev = None
        while head:
            temp = head.next ## store the node after head
            head.next = prev  ## 断开以前的链
            prev = head ## prev equal to the old head
            head = temp ## head equals to the second node 
        return prev 
        

    def reverseList_recursion(self.head):
        if head is None or head.next is None: ## the size of the linkedlist is <= 1
            return head  
        new_head = self.reverseList_recursion(head.next) ## assume it's reversed 
        head.next.next = head 
        head.next = None 
        return new_head 

    




    