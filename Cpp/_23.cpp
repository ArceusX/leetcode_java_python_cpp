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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        if (lists.empty()) {
            return nullptr;
        }
        
        return mergeLists(lists, 0, lists.size() - 1);
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
        
        while (left) {
            tail->next = left;
            left = left->next;
            tail = tail->next; 
        }

        while (right) {
            tail->next = right;
            right = right->next;
            tail = tail->next;
        }

        return head->next;
    }
};