class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.buffer  = [-1] * k
        self.ptWrite = 0
        self.ptRead  = 0

        # Flag helps discern full vs empty buffer, thru inference
        # of whether enQueue or deQueue was called prior, which
        # cannot identify from checking only ptWrite == ptRead
        self.flag    = True

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        self.buffer[self.ptWrite] = value
        self.ptWrite = (self.ptWrite + 1) % self.k

        # For ptWrite == ptRead, overwrite() sets flag = false
        # to trigger condition for next full() to return true
        self.flag    = (self.ptRead != self.ptWrite)

        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.ptRead = (self.ptRead + 1) % self.k

        # For ptWrite == ptRead, deQueue() sets flag = true to
        # trigger condition for next empty() to return true 
        self.flag   = (self.ptRead == self.ptWrite)

        return True
        
    def Front(self) -> int:
        if self.isEmpty(): return - 1
        return self.buffer[self.ptRead] # Next value to be read   

    # Return value just written prior. If ptWrite
    # sits at index 0, return highest index (k - 1)
    def Rear(self) -> int:
        if self.isEmpty(): return - 1
        return self.buffer[self.ptWrite - 1]

    # ptWrite == ptRead means buffer is either empty or full
    # and flag == false means prior call was enQueue(), so 
    # buffer can only have been full after prior
    # deQueue() or enQueue()
    def isFull(self) -> bool:
        return (self.ptRead == self.ptWrite) and not self.flag   

    # ptWrite == ptRead means buffer is either empty or full 
    # and flag == true means prio
        // ptWrite == ptRead means buffer is either empty or full
    // and flag == false means prior call was enQueue(), so 
    // buffer can only have been full after prior
    // deQueue() or enQueue()r call was deQueue(), so 
    # buffer can only have been empty after prior 
    # deQueue() or enQueue()
    def isEmpty(self) -> bool:
        return (self.ptRead == self.ptWrite) and self.flag
