// 1584 Min Cost to Connect All Points (Prim's Algo)

class Solution {
public:
	using Edge = pair<int, int>;
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<bool> isAdded(n, false);
        int sumCost = 0;
        int nInMST = 0;

        // <entry type, container, comparison class>
        // greater<> gives min heap. less<> gives max heap
        priority_queue<Edge, vector<Edge>, greater<Edge>> heap;
        heap.emplace(0, 0);
        while (nInMST < n) {
        	auto [weight, toNode] = heap.top();
        	heap.pop();

        	if (isAdded[toNode]) continue;

        	isAdded[toNode] = true;
        	nInMST += 1;
        	sumCost += weight;

        	for (int nbor = 0; nbor < n; nbor++) {
            	// Consider only edges carrying node not already added
                if (!isAdded[nbor]) {
                    int addCost = abs(points[toNode][0] - points[nbor][0]) +\
                                  abs(points[toNode][1] - points[nbor][1]);
                    
                    heap.emplace(addCost, nbor);
                }
        	}

        }
        return sumCost;
    }
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        int sumCost = 0;
        vector<bool> isAdded(n, false);
        vector<int> minCost(n, INT_MAX);
        minCost[0] = 0;

        for (int nInMST = 0; nInMST < n; nInMST++) {
            int toAdd = -1;
            int currMinCost = INT_MAX;

            for (int prospect = 0; prospect < n; prospect++) {
                if (!isAdded[prospect] && minCost[prospect] < currMinCost) {
                    currMinCost = minCost[prospect];
                    toAdd = prospect;
                }
            }

            sumCost += currMinCost;
            isAdded[toAdd] = true;

            for (int nbor = 0; nbor < n; nbor++) {
                if (!isAdded[nbor]) {
                    minCost[nbor] = min(minCost[nbor], abs(points[toAdd][0] - points[nbor][0]) +
                        abs(points[toAdd][1] - points[nbor][1]));
                }
            }
        }

        return sumCost;
    }
};