// 002: Add Two Numbers (Digits Being Nodes in Linked List)

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;

        // falseHead: Base holding result digits, but to
        //            be excluded from result
        auto falseHead = new ListNode(-1);
        auto current = falseHead;
        
        while (l1 || l2) {
            
            int sum = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            int sum_digit = sum % 10;
            carry = sum / 10;
            
            // Add latest result digit (exclude carry)
            current->next = new ListNode(sum_digit);
            current = current->next;
            
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        
        if (carry != 0) {
            current->next = new ListNode(carry);
        }
        
        return falseHead->next;
    }
};