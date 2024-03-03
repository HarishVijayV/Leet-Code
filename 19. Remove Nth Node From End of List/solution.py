# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head: Optional[ListNode])->int:
        c=0
        aa=head
        while(aa is not None):
            c+=1
            aa=aa.next
        return c
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cc=dummy
        length = self.length(head)
        for _ in range(length-n):
            dummy=dummy.next
        dd=dummy.next
        dummy.next=dd.next
        return cc.next
        
        