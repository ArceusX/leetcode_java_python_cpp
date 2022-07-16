
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;
        ListNode temp = head;
        
        int len = 1;

        // Get old tail (final)
        while (temp.next != null) {
            temp = temp.next;
            len++;
        }
        
        k = k % len;

        //Any full cycle leaves unchanged
        if (k == 0) return head;
        
        ListNode current = head;

        // Get node that would be new tail
        // Each rotate moves tail down 1, by displacing tail
        // So need precedessor to final displaced node
        for (int i = 0; i < (len - k - 1); i++) {
            current = current.next;
        }

        //newHead will be last displaced tail node
        ListNode newHead = current.next;

        //First displaced tail is wired to point to old head
        temp.next = head;

        // Now new tail has its previous next cleared 
        current.next = null;
        return newHead;
    }
}