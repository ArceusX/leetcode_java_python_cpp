/* 206: Reverse linked list
 * Track 3 pointers: back: nearest to head; lead: back.next 
 * before swap; nextLead: lead.next before swap. Rewire 
 * lead.next = back; shift back, lead up for next iter */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* back = head;
        ListNode* lead = back->next;

        // If lead, guarantees back is non-None
        while (lead) {
            // Record before rewiring would overwrite this data
            ListNode* nextBack = lead->next;

            lead->next = back;

            back = lead; // lead takes role of next back
            lead = nextBack; 
        }

        head->next = nullptr;

        // "while lead" exited on back that is tail of original
        // list (ie next == null). Put it as head of reversed list
        return back;
    }
};