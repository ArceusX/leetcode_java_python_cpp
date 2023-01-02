class Solution {
public:
    ListNode* detectCycle(ListNode *head) {
    	if (!head) return nullptr;
        ListNode* slow = head, *fast = head;

        bool hasCycle = false;
        while (slow->next && fast->next) {
        	slow = slow->next;
        	fast = fast->next;
        	if (fast->next) {
        		fast = fast->next;

        		if (slow == fast) {
        			hasCycle = true;
                    break;
        		}
        	}
        }
        
        if (hasCycle) {
            slow = head;
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            
            return fast;
        }
        return nullptr;
    }
};