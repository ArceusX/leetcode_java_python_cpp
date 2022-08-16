class Solution {
public:
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {

	// Create 2 pointers: 1 we merge elems into and 
	// another that tracks eventual head of merged list
	ListNode* mDummy = new ListNode(-1);
	ListNode* mPt = mDummy;

    while (l1 && l2) {
	    if (l1->val < l2->val) {
	    	mPt->next = l1;
	    	l1 = l1->next;
	    }
	    else {
	    	mPt->next = l2;
	    	l2 = l2->next;
	    }
	    mPt = mPt->next;
    }

    // No more merge involving elems from different
    // list, so quickly add elems of remaining list
    if (l1) mPt->next = l1;
    if (l2) mPt->next = l2;

    return mDummy->next;
}
};