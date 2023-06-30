// 232: Implement Queue With 2 Stacks
/* Push: O(1)
 * Peek: O(1) amortized. Move from pushStack into
 * popStack needs O(n), but that move readies n
 * vals for pop, so O(n) / n == O(1) amortized */

class MyQueue {
    Stack<Integer> pushStack, popStack;

    public MyQueue() {
        pushStack = new Stack<>();
        popStack  = new Stack<>();
    }
    
    public void push(int x) {
        pushStack.push(x);
    }
    
    public int pop() {
        int x = this.peek();
        popStack.pop();
        return x;
    }
    
    public int peek() {
        if (popStack.empty()) {
            while (!pushStack.empty()) {
                popStack.push(pushStack.pop());
            }
        }
        return popStack.peek();
    }
    
    public boolean empty() {
        return pushStack.empty() && popStack.empty();
    }
};