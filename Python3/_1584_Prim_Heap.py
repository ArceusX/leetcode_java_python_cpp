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
    def __init__(self, arr = []):
        self.heap = []
        for edge in arr:
            self.push(edge)
                
    def push(self, edge) -> None:
        self.heap.append(edge)
        self.heapifyUp(self.heap, len(self.heap) - 1)
        
    # When single elem violates heap property. Modify only its ancestors
    @staticmethod
    def heapifyUp(arr, i) -> None:
        if not (0 <= i < len(arr)): return
        
        child = i
        parent = (child - 1) // 2
        
        # Percolate up, swapping to ensure smaller val is made parent
        while child != 0 and arr[child][0] < arr[parent][0]:
            arr[child], arr[parent] = arr[parent], arr[child]
            child = parent
            parent = (child - 1) // 2
          
    # Array's tail is efficiently removed in O(1). Other indices need
    # O(n) shifts. Swap root val we want to remove with tail's val,
    # remove tail, then heapifyDown along single branch from root
    def pop(self) -> (int, int):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            prevRoot = self.heap.pop()
            self.heapifyDown(self.heap, 0)
            return prevRoot
        
        return None
    
    @staticmethod
    def heapifyDown(arr, i) -> None:
        n = len(arr)

        # n - 1: Nothing below to possibly swap with if last node
        if not (0 <= i < n - 1): return
        
        # If need to swap parent, swap it with lower val child as
        # higher val child expects new parent val to become smaller
        # That leaves subtree of higher val child unperturbed
        
        parent = i
        lValChild = 2 * parent + 1
        
        while lValChild < n:
            if (lValChild < n - 1) and arr[lValChild + 1][0] < arr[lValChild][0]:
                lValChild += 1
                
            if arr[lValChild][0] < arr[parent][0]:
                arr[parent], arr[lValChild] = arr[lValChild], arr[parent]
            else:
                break
                
            parent = lValChild
            lValChild = 2 * parent + 1
        
    #Unused
    def peek(self) -> (int, int):
        if not self.heap:
            return
        return self.heap[0]
    
    #Unused
    def updateKey(self, i, newVal) -> None:
        if not (0 <= i < len(self.heap)):
            return
        
        prevVal = self.heap[i][0]
        self.heap[i][0] = newVal
        
        # If updated with larger val, percolate change+= down to leaves
        if newVal > prevVal:
            MinHeap.heapifyDown(self.heap, i)
            
        # If replaced with smaller val, percolate change-= up to root
        else:
            MinHeap.heapifyUp(self.heap, i) 