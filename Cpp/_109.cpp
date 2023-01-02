/* Increment slow by 1 and fast by 2 until end of list
   to get middle of range. Create TreeNode from middle 
   listNode as subRoot with each half-range as its child 
*/

class Solution {
public:
TreeNode* sortedListToBST(ListNode* head) {
    if (!head) return nullptr;
    if (!head->next) return new TreeNode(head->val);

    ListNode* fast = head, * slow = head, * prev = nullptr;

    while (fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    prev->next = nullptr;
    return new TreeNode(slow->val, sortedListToBST(head), sortedListToBST(slow->next));

}
};