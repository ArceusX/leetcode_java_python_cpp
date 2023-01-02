# Prim's Algo
# Prim's builds from 1 central component that adds lightest
# remaining edge (calculated as weight from node already
# added to one not added) each iter

# Implementing own MinHeap class: See Prim 1 of _1584_Prim
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        isAdded = [False] * n
        
        sumCost = 0
        nInMST = 0

        # Store (weight, node) being pointed to/newly added
        heap = MinHeap([(0, 0)])
        
        while nInMST < n:
            weight, toNode = heap.pop()
            
            # Only add nodes not already added. If added, skip
            if isAdded[toNode]:
                continue
            
            isAdded[toNode] = True
            nInMST += 1
            sumCost += weight
            
            for nbor in range(n):

                # Consider only edges carrying node not already added
                if not isAdded[nbor]:
                    addCost = abs(points[toNode][0] - points[nbor][0]) +\
                                  abs(points[toNode][1] - points[nbor][1])
                    
                    heap.push((addCost, nbor))
                    
        return sumCost

# edge is (weight[0], toNode[1]). Weight from added node to nbor toNode
class MinHeap:

    # If passed [] or nothing for arr, no push 
    def __init__(self, arr = []):

        # Heapify in-place all at once
        self.heap = arr
        self.heapifyDown(self.heap)

        # Push, then heapify one-by-one
        # self.heap = []
        # for edge in arr:
        #     self.push(edge)
                
    def push(self, edge) -> None:
        self.heap.append(edge)
        self.heapifyUp(self.heap, len(self.heap) - 1)
        
    # heapifyUp swaps only if child < parent and other child 
    # doesn't mind if parent is swap to have smaller val (need
    # to check and modify only 1 branch when percolating)
    @staticmethod
    def heapifyUp(arr, i) -> None:
        if not (0 <= i < len(arr)): return
        
        child = i
        parent = (child - 1) // 2
        
        # Percolate up, swapping to ensure smaller between child
        # and parent is made new parent for MinHeap
        while child != 0 and arr[child][0] < arr[parent][0]:
            arr[child], arr[parent] = arr[parent], arr[child]
            child = parent
            parent = (child - 1) // 2
          
    # Array's tail is efficiently removed in O(1). Other indices need
    # O(n) shifts. Swap root val we want to remove with tail val,
    # remove tail, then heapifyDown from root
    def pop(self) -> (int, int):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            prevRoot = self.heap.pop()
            self.heapifyDown(self.heap)
            return prevRoot
        
        return

    # Assume "default" i = 0 because pop attempts to erase arr[0]
    # For updateKey, i is variable because any node is targetable
    @staticmethod
    def heapifyDown(arr, i = 0) -> None:
        n = len(arr)

        # arr[-1]: No child to swap with if is leaf, which final node is
        if not (0 <= i < n - 1): return
        
        # When swapping parent, swap it with lower-val child so
        # parent now with smaller child's val will still be less than
        # larger child. Subtree of larger child left unaffected
        
        parent = i
        child = 2 * parent + 1 # leftChild
        
        while child < n:

            # Set child to lower-val child. Check rightChild exist first
            if (child < n - 1) and arr[child + 1][0] < arr[child][0]:
                child += 1
                
            if arr[child][0] < arr[parent][0]:
                arr[parent], arr[child] = arr[child], arr[parent]

            # If swap is unneeded, no longer need to heapifyDown subtree
            else:
                break
                
            parent = child
            child = 2 * parent + 1
        
    # Get highest-priority elem: max | min elem for (Max | Min) Heap
    def peek(self) -> (int, int):
        if not self.heap:
            return
        return self.heap[0]
    
    # Unused
    def updateKey(self, i, newVal) -> None:
        if not (0 <= i < len(self.heap)):
            return
        
        prevVal = self.heap[i][0]
        self.heap[i][0] = newVal
        
        # If updated with larger val, percolate change+ down to leaves
        if newVal > prevVal:
            MinHeap.heapifyDown(self.heap, i)
            
        # If updated with smaller val, percolate change- up to root
        else:
            MinHeap.heapifyUp(self.heap, i) 