class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        if (lists.empty()) return nullptr;

        // Merging linearly ([[0 + 1] + 2] + 3)
        // is space-efficient, but time-inefficient

        // Merging divide-and-conqurer ([0 + 1] + [2 + 3])
        // is time-efficient, but space-inefficient

        ListNode* merged = lists[0];
        for (int i = 1; i < lists.size(); i++) {
            merged = merge(merged, lists[i]);
        }
        return merged;
        //return mergeLists(lists, 0, lists.size() - 1);
    }

    ListNode* mergeLists(vector<ListNode*>& lists, int start, int end) {
        
        if (start == end) {
            return lists[start];
        }
        
        int mid = (start + end) / 2;
        
        return merge(mergeLists(lists, start, mid), mergeLists(lists, mid + 1, end));
    }
                     
    ListNode* merge(ListNode* left, ListNode* right) {
        
        ListNode* head = new ListNode(-1);
        ListNode* tail = head;
        
        while (left && right) {
            if (left->val < right->val) {
                tail->next = left;
                left = left->next;
            }
            
            else {
                tail->next = right;
                right = right->next;
            }
            
            tail = tail->next;
        }

        if (left) tail->next = left;
        if (right) tail->next = right;
        
        return head->next;
    }
};