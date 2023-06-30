// 225: Implement Stack with 2 Queues
// Need only 1 queue. 2 queues use same time complexity

// For push: push x, then repush those that were
// pushed before x. O(n) push and O(1) peek  

class MyStack {
    queue<int> queue;
public:
    MyStack() {}
    
    void push(int x) {
        queue.push(x);
        for (int i = 1, n = queue.size(); i < n; i++) {
            queue.push(pop()); // Move front e to back
        }
    }
    
    int pop() {
        int x = queue.front();
        queue.pop();
        return x;
    }
    
    int top() {
        return queue.front();
    }
    
    bool empty() {
        return queue.empty();
    }
};