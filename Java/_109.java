/* Increment slow by 1 and fast by 2 until end of list
   to get middle of range. Create TreeNode from middle 
   listNode as subRoot with each half-range as its child 
*/

class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        if (head.next == null) return new TreeNode(head.val);
        ListNode fast, slow, prev;
        fast = slow = head; prev = null;
        
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev.next = null;
        return new TreeNode(slow.val, sortedListToBST(head),
                            sortedListToBST(slow.next));
        
    }
}