// 002: Add Two Numbers (Digits Being Nodes in Linked List)

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;

        // falseHead: Base holding result digits, but to
        //            be excluded from result
        var falseHead = new ListNode(-1);
        var current = falseHead;
        
        while ((l1 != null) || (l2 != null)) {
            int n1 = (l1 != null) ? l1.val : 0;
            int n2 = (l2 != null) ? l2.val : 0;
            
            int sum = carry + n1 + n2;
            carry = sum / 10;
            
            // Add latest result digit (exclude carry)
            current.next = new ListNode(sum % 10);
            current = current.next;
            
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        
        if (carry != 0) {
            current.next = new ListNode(carry);
        }
        
       return falseHead.next;
    }
}