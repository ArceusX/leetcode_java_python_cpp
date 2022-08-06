/*
1. Initialize each node in disjoint union set array []parent to
   its index (set each node as root of its own group)

2. Node's val in []parent being changed marks node is absorbed. 
   Overwrite its old val with node/root that absorbed it

3. Care to overwrite only nodes in parent that are roots of their 
   sets because roots are only nodes not yet absorbed.

4. If node1 connects to node2, node1 connects its root to node2;
   let node2 absorb root and its group by parent[find(n1)] = n2;

5. Return # of entries in parent == to their index (original val)
   unchanged, being # of unabsorbed groups
*/

class Solution {
    
    int[] parent;
    public int findCircleNum(int[][] mat) {
        parent = new int[mat.length + 1];
        Arrays.setAll(parent, i -> i);
        
        //For each row-node, check only with preceding nodes
        //because graph is undirected
        for (int row = 0; row < mat.length; row++) {
            for (int col = 0; col < row; col++) {

                //Kill group lead by root connected to col-node
                if (mat[row][col] == 1) {
                    parent[find(col)] = row;

                    //Path compression: probably unnecessary
                    //parent[col] = row
                }
            }
        }

        int nGroups = 0;
        for (int row = 0; row < mat.length; row++) {
            if (parent[row] == row) {
                nGroups++;
            }
        }

        return nGroups;
    }

    int find(int x) {
        //Iterate until get to root. Along way, compress path
        while (parent[x] != x) {
            //Wire x to point to its grandparent, which may
            //be identical to parent. Then move x up group
            int temp = parent[x];
            parent[x] = parent[temp];
            x = temp;
        }

        return x;
    }
}