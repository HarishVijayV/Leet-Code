# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        while (l1!=None):
            list1.append(str(l1.val))
            l1=l1.next
        while (l2!=None):
            list2.append(str(l2.val))
            l2=l2.next
        a = "".join(list1[::-1]) 
        b = "".join(list2[::-1]) 
        c= int(a)+int(b)
        c=str(c)
        c=c[::-1]
        result_list=list(c)
        l3=ListNode(0)
        current=l3
        for i in result_list:
            current.next=ListNode(i)
            current=current.next
        return l3.next