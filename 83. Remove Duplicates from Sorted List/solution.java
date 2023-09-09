/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr=head;
        while(curr!=null&&curr.next!=null){
            if(curr.val==curr.next.val){
                ListNode temp=curr.next.next;
                if(temp==null){
                    curr.next=null;
                }
                else{
                    curr.next=temp;                    
                }
            }
            else{
                curr=curr.next;
            } 
        }
        return head;
    }
}