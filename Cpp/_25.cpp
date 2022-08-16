class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {

    	if (!head || k == 1) return head;

    	ListNode* dummy = new ListNode(-1, head);
    	ListNode* pred = dummy;
    	ListNode* tail = head;
    	int i = 0;

    	while (tail) {
    		i++;

    		if (i % k == 0) {
    			pred = reverse(pred, tail->next);
    			tail = pred->next;
    		}
    		else {
    			tail = tail->next;
    		}
    	}

    	return dummy->next;
    }

    ListNode* reverse(ListNode* pred, ListNode* end) {
    	ListNode* head = pred->next;
    	ListNode* tail = head->next;

    	while (tail != end) {
    		ListNode* after = tail->next;
    		tail->next = pred->next;
    		pred->next = tail;
    		tail = after;
    	}

    	head->next = end;
    	return head;
    }
};