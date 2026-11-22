# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverseList(head: ListNode) -> ListNode:
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        i = 1
        newHead = reverseList(head)
        curr = newHead
        prev = None
        while curr and i!=n:
            prev = curr
            curr = curr.next
            i += 1

        if prev and curr:
            prev.next = curr.next
        elif not prev and curr:
            curr = curr.next
            newHead = curr
        
        return reverseList(newHead)


            

        