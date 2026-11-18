# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        nodes = {}
        n = 0
        curr = head
        while curr:
            nodes[n] = curr
            n+=1
            curr = curr.next

        
        curr = head
        j = n - 1
        i = 1
        for k in range(n-1):
            if k%2==0:
                curr.next = nodes[j]
                j-=1
            else:
                curr.next = nodes[i]
                i += 1

            curr = curr.next
        curr.next = None



        ### {0:NODE, 1:NODE}
        ## One index goes from 0 -> n-1 (even ++2), another goes from n-1 -> 0 (odd ++2)



