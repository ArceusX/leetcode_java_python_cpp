/**
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        auto result = new ListNode(0);
        auto pointer = result;
        
        while (l1 || l2) {
            
            int sum = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            int sum_digit = sum % 10;
            carry = sum / 10;
            
            pointer->next = new ListNode(sum_digit);
            pointer = pointer->next;
            
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        
        if (carry != 0) {
            pointer->next = new ListNode(carry);
        }
        
        return result->next;
    }
};