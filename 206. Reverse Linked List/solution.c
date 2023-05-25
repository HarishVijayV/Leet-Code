struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *temp,*prevn,*next;
    prevn=NULL;
    temp=next=head;

while(next!=0)
{
next=next->next;
temp->next=prevn;
prevn=temp;
temp=next;
}
head=prevn;
return head;

}