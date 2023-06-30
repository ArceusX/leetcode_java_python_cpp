# 225: Implement Stack with 2 Queues
# Need only 1 queue. 2 queues use same time complexity

# For push: push x, then repush those that were
# pushed before x. O(n) push and O(1) peek  
class MyStack:
    def __init__(self):
        # As queue is 1-ended, choose only 1 pair:
        # (append + popleft) or (appendleft + pop) 
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(1, len(self.queue)):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popright()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not bool(self.queue)
        