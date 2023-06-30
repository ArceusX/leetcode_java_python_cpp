// 1584 Min Cost to Connect All Points (Prim's Algo)

/* Into initially-empty connected component (CC), Prim adds
 * each node via lighest edge to unadded node from any node 
 * already in CC (that edge's weight as unadded node's cost)
 *
 * Track each edge in heap. Get lighest edge from heap,
 * then check if that edge connects to unadded node
 * Complex.: O(nEdges * ln(nNodes)) */

// Implement own MinHeap
class Solution {
public int minCostConnectPoints(int[][] points) {
    int n = points.length;
    boolean[] isAdded = new boolean[n];

    int sumCost = 0;
    int nInMST  = 0;

    // Store [0: weight] to [1: node]. Heap to sort by [0]
    // Assign points[0] as source node with cost 0
    MinHeap heap = new MinHeap(new Integer[][] {{0, 0}});

    // To iterate over edges gives no guarantee each
    // iteration adds 1 node to connected component
    while (nInMST < n) {
        Integer[] edge = heap.pop();

        // Only add nodes not already added. If added, skip
        if (isAdded[edge[1]]) continue;

        // Lighest newly-scanned edge connects unadded node 
        Integer weight  = edge[0];
        Integer toNode  = edge[1];
        isAdded[toNode] = true;
        nInMST  += 1;
        sumCost += weight;

        // Push edge from newly-added node to each unadded node into heap 
        for (int nbor = 0; nbor < n; nbor++) {
            if (isAdded[nbor]) continue;

            Integer addCost = Math.abs(points[toNode][0] - points[nbor][0]) + 
                              Math.abs(points[toNode][1] - points[nbor][1]);

            heap.push(new Integer[] {addCost, nbor});
        }
    }

    return sumCost;
}
}

// edge: (0: weight, 1: toNode). Weight to toNode from node in CC
class MinHeap {

    public List<Integer[]> heap = new ArrayList<>();
    public MinHeap(Integer[][] list) {
        for (Integer[] edge : list) push(edge);
    }

    public void push(Integer[] edge) { // Keep heapness
        heap.add(edge);
        heapifyUp(heap, heap.size() - 1);
    }

    // Ensure heapness up from lone index i of arr, default
    // being arr's final index for call by push()
    public static void heapifyUp(List<Integer[]> heap, int i) {
        if (i < 0 || (i >= heap.size())) return;
        int child = i;
        int parent = (child - 1) / 2;

        // Resolve up: Swap to set lower-ordered val as parent 
        // Child's sibling accepts parent swapped lower-ordered val
        while (child != 0 && (heap.get(child)[0] < heap.get(parent)[0])) {
            Collections.swap(heap, child, parent);
            child = parent;
            parent = (child - 1) / 2;
        }
    }

    // Steps: Swap vals at [0] and [-1]. In O(1), remove
    //       val now at [-1]. heapifyDown(..) from [0]
    public Integer[] pop() {
        if (!heap.isEmpty()) {
            Collections.swap(heap, 0, heap.size() - 1);
            Integer[] root = heap.remove(heap.size() - 1);
            heapifyDown(heap, 0);
            return root;
        }
        return null;
    }

    // Ensure heapness down from lone index i of arr,
    // default being i = 0 for call by pop(),
    public static void heapifyDown(List<Integer[]> heap, int i) {
        int len = heap.size();

        // arr[len - 1]: As leaf, has no child to swap with
        if (i < 0 || (i >= len - 1)) return;

        int parent = i;
        int child  = 2 * parent + 1; // leftChild

        // Child's sibling accepts parent swapped lower-ordered val
        while (child < len) {

            // Set child to lower-val child between left and right
            if ((child < len - 1) && heap.get(child + 1)[0] <
                    heap.get(child)[0])
                child++;

            if (heap.get(child)[0] < heap.get(parent)[0]) {
                Collections.swap(heap, child, parent);
            }

            // If no swap, no longer need to heapifyDown subtree
            else break;

            parent = child;
            child  = 2 * parent + 1;
        }
    }
}