// Disjoint union set: Return # of connected components
// See _547.java for algo

class Solution {
public:
int* parent;
int findCircleNum(vector<vector<int>>& conn) {
	int n = conn.size();
	parent = new int[n];
	generate_n(parent, n, [count = 0]() mutable { return count++;});

	for (int row = 0; row < n; row++) {
		for (int col = 0; col < row; col++) {
			if (conn[row][col] == 1) {
				parent[find(col)] = row;
			}
		}
	}

	int nGroups = 0;
	for (int i = 0; i < n; i++) {
        if (i == parent[i]) nGroups ++;
	}

	return nGroups;
}

int find(int x) {
    
	while (parent[x] != x) {
		int temp = parent[x];
		parent[x] = parent[temp];
		x = temp;
	}
	return x;
}
};