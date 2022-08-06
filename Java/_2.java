/**
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        var result = new ListNode(-1);
        var pointer = result;
        
        while ((l1 != null) || (l2 != null)) {
            int n1 = (l1 != null) ? l1.val : 0;
            int n2 = (l2 != null) ? l2.val : 0;
            
            int sum = carry + n1 + n2;
            carry = sum / 10;
            
            pointer.next = new ListNode(sum % 10);
            pointer = pointer.next;
            
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        
        if (carry != 0) {
            pointer.next = new ListNode(carry);
        }
        
       return result.next;
    }
}