// 622: Implement Queue with Circular Buffer
// Track flag variable to discern full vs empty buffer 

class MyCircularQueue {
public:
    int* buffer;
    size_t ptWrite = 0;
    size_t ptRead  = 0;
    size_t k;

    // Flag helps discern full vs empty buffer, thru inference
    // of whether enQueue or deQueue was called prior, which
    // cannot identify from checking only ptWrite == ptRead
    bool   flag    = true;

    MyCircularQueue(int k): k(k), buffer(new int[k]) {}
    
    bool enQueue(int value) {
        if (isFull()) return false;

        buffer[ptWrite] = value;
        ptWrite = (ptWrite + 1) % k;

        // For ptWrite == ptRead, overwrite() sets flag = false
        // to trigger condition for next full() to return true
        flag    = (ptRead != ptWrite);

        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;

        int value = buffer[ptRead];
        ptRead = (ptRead + 1) % k;

        // For ptWrite == ptRead, deQueue() sets flag = true to
        // trigger condition for next empty() to return true 
        flag   = (ptRead == ptWrite);

        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return buffer[ptRead]; // Next value to be read
    }
    
    int Rear() {
        if (isEmpty()) return -1;

        // Return value just written prior. If ptWrite
        // sits at index 0, return highest index (k - 1)
        return buffer[(ptWrite == 0 ? k : ptWrite) - 1];
    }

    bool isFull() {
        return (ptRead == ptWrite) && !flag;
    }
    
    // ptWrite == ptRead means buffer is either empty or full 
    // and flag == true means prior call was deQueue(), so 
    // buffer can only have been empty after prior 
    // deQueue() or enQueue()
    bool isEmpty() {
        return (ptRead == ptWrite) &&  flag;
    }
};