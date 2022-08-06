# Kruskal's Algo, using disjoint union set to check if potential
# edge connects components not already connected.

# Implementing own MinHeap class

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        parent = [x for x in range(n)]
        
        # Return root and height of path to root
        # Not global rank, but rather local based on 1 path
        def find(x: int) -> (int, int):
            height = 1
            while parent[x] != x:

                # Wire x to point to its grandparent, which may
                # be identical to parent. Then move x up branch
                x, parent[x] = parent[x], parent[parent[x]]
                height += 1
            
            return (x, height)
        
        heap = MinHeap()
        
        # Calculate Manhattan distance from every node to every other
        for outNode in range(n):
            for inNode in range(outNode + 1, n):
                weight = abs(points[outNode][0] - points[inNode][0]) +\
                         abs(points[outNode][1] - points[inNode][1])
                heap.push((weight, outNode, inNode))
                
        
        # We didn't add "edge" of weight 0 from any node to itself
        # to heap, so "starting" node comes free
        # Alternative, set nEdgesAdded = 0...while nEdgesAdded < n -1
        nInMST = 1
        sumCost = 0
        
        while nInMST < n:
            (weight, outNode, inNode) = heap.pop()
            outFind = find(outNode)
            inFind = find(inNode)

            if (outFind[0] != inFind[0]):
                sumCost += weight
                nInMST += 1
                
                # Wire root of shorter height to root of longer
                # (using rank or longest height over any path would 
                # be improved, costlier alternative)
                if (outFind[1] > inFind[1]):
                    parent[inFind[0]] = outFind[0]
                else:
                    parent[outFind[0]] = inFind[0]
                    
        return sumCost

# edge is (weight[0], fromNode[1], toNode[2])
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
    def pop(self) -> (int, int, int):
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
    