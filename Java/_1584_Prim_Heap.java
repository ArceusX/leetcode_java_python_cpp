
// With own MinHeap implementation
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] isAdded = new boolean[n];

        int sumCost = 0;
        int nInMST = 0;

        MinHeap heap = new MinHeap(new Integer[][] {{0, 0}});

        while (nInMST < n) {
            Integer[] edge = heap.pop();

            if (isAdded[edge[1]]) continue;

            Integer weight = edge[0];
            Integer toNode = edge[1];
            isAdded[toNode] = true;
            nInMST += 1;
            sumCost += weight;

            for (int nbor = 0; nbor < n; nbor++) {
                Integer addCost = Math.abs(points[toNode][0] - points[nbor][0]) + Math.abs(points[toNode][1] - points[nbor][1]);

                heap.push(new Integer[] {addCost, nbor});
            }
        }

        return sumCost;
    }
}

//edge is (weight[0], toNode[1]). Weight from added node to nbor toNode
class MinHeap {

    public List<Integer[]> heap = new ArrayList<>();
    public MinHeap(Integer[][] list) {
        for (Integer[] edge : list) push(edge);
    }

    public void push(Integer[] edge) {
        heap.add(edge);
        heapifyUp(heap, heap.size() - 1);
    }

    // When single elem violates heap property. Modify only its ancestors
    public static void heapifyUp(List<Integer[]> heap, int i) {
        if (i < 0 || (i >= heap.size())) return;
        int child = i;
        int parent = (child - 1) / 2;

        // Percolate up, swapping to ensure smaller val is made parent
        while (child != 0 && (heap.get(child)[0] < heap.get(parent)[0])) {
            Collections.swap(heap, child, parent);
            child = parent;
            parent = (child - 1) / 2;
        }
    }

    // Array's tail is efficiently removed in O(1). Other indices need
    // O(n) shifts. Swap root val we want to remove with tail's val,
    // remove tail, then heapifyDown along single branch from root
    public Integer[] pop() {
        if (!heap.isEmpty()) {
            Collections.swap(heap, 0, heap.size() - 1);
            Integer[] root = heap.remove(heap.size() - 1);
            heapifyDown(heap, 0);
            return root;
        }
        return null;
    }

    public static void heapifyDown(List<Integer[]> heap, int i) {
        int len = heap.size();
        if (i < 0 || (i >= len)) return;

        // If need to swap parent, swap it with lower val child as
        // higher val child expects new parent val to become smaller
        // That leaves subtree of higher val child unperturbed

        int parent = i;
        int lValChild = 2 * parent + 1;

        while (lValChild < len) {
            if ((lValChild < len - 1) && heap.get(lValChild + 1)[0] <
                    heap.get(lValChild)[0])
                lValChild++;

            if (heap.get(lValChild)[0] < heap.get(parent)[0]) {
                Collections.swap(heap, lValChild, parent);
            }
            else break;

            parent = lValChild;
            lValChild = 2 * parent + 1;
        }
    }
}