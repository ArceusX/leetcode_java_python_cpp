// 225: Implement Stack with 2 Queues
// Need only 1 queue. 2 queues use same time complexity

// For push: push x, then repush those that were
// pushed before x. O(n) push and O(1) peek 
class MyStack {
    Queue<Integer> queue;

    public MyStack() {
        queue = new ArrayDeque<>();
    }
    
    public void push(int x) {
        queue.add(x);
        for (int i = 1, n = queue.size(); i < n; i++) {
            queue.add(queue.remove());
        }
    }
    
    public int pop() {
        return queue.remove();
    }
    
    public int top() {
        return queue.peek();
    }
    
    public boolean empty() {
        return queue.isEmpty();
    }
}