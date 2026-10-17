/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    int count=0;
    ListNode*move = head;
    ListNode*prev = NULL;

    while(move->next!=NULL){
        prev = move;
        move = move->next;
        count ++;
    }

    ListNode*move1 = head;
    ListNode*prev1 = NULL;

    if(head == NULL){
        return NULL;
    }

    if(n == count+1){
        ListNode*temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    if(n == 1){
        prev->next = NULL;
        delete move;
        return(head);
    }

    int i=0;
    while(i < count-(n-1)){
        prev1 = move1;
        move1 = move1->next;
        i++;
    }

    cout<<move1->val<<endl;
    cout<<prev1->val<<endl;

    
    prev1->next = move1->next;
    delete move1;
    return(head);
    }
};