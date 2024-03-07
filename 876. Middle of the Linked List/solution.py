# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        c=0
        headd=head
        while headd.next!=None:
            c+=1
            headd=headd.next
        return c
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=self.length(head)
        dup=head
        for i in range(n//2):
            dup=dup.next
        if n%2==0:
            return dup
        return dup.next

