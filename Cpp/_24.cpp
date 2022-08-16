class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* pred = new ListNode(-1, head);
        ListNode* dummy = pred;

        while (pred->next && pred->next->next) {

        	ListNode* first = pred->next;
        	ListNode* second = first->next;

        	pred->next = second;
        	first->next = second->next;
        	second->next = first;

        	pred = pred->next->next;
        }

        return dummy->next;
    }
};