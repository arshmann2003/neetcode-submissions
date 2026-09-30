# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = list1
        head2 = list2
        if not head1:
            return head2
        if not head2:
            return head1

        resHead = None
        curr = None

        if head1.val < head2.val:
            resHead = head1
            curr = head1
            head1 = head1.next
        else:
            resHead = head2
            curr = head2
            head2 = head2.next

        while head1 and head2:
            val1 = head1.val
            val2 = head2.val
            if val1 < val2:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        
        curr.next = head1 if head1 else head2

        return resHead
            



        