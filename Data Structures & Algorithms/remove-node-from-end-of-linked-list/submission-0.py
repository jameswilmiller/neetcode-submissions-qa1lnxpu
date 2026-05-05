# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #lets use two pointers
        #we want right pointer to be at the end of the list and that space between pointers is equal to n
        #essentially we want to keep shifting l and r until r is at the end of the list while keeping gap = n
        #we are gonna keep a dummy node at the beginning of the list, and initiliase our left pointer at the dummy node
        #this way we have left pointer at the correct node 
        #to return new linked list, return dummy.next
        dummy = ListNode(0, head)
        left = dummy
        # we need right to be at head + n
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        #delete the node
        left.next = left.next.next
        return dummy.next

     
       
        