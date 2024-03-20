# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head=list1
        dup=list1
        for i in range(0,a-1):
            dup=dup.next
        dup2=dup
        for i in range(a,b+1):
            dup2=dup2.next
        dup.next=list2
        while dup.next!=None:
            dup=dup.next
        dup.next=dup2.next
        return head
        

        