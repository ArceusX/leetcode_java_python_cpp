class Solution {
public:
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {

	ListNode *curr1 = l1, *curr2 = l2;

	// Create 2 ptrs: tail onto which nodes merge, 
	// falseHead that points to eventual head of merged
	ListNode* tail      = new ListNode(-1);
	ListNode* falseHead = tail;

    while (curr1 && curr2) {
	    if (curr1->val < curr2->val) {
	    	tail->next = curr1;
	    	curr1 = curr1->next;
	    }
	    else {
	    	tail->next = curr2;
	    	curr2 = curr2->next;
	    }
	    tail = tail->next;
    }

    // After either list depleted: end comparison, 
    // if other remains, merge its current tracked 
    if (curr1) tail->next = curr1;
    if (curr2) tail->next = curr2;

    return falseHead->next;
}
};