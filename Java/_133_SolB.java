//Recursive

class Solution {
    
    Map<Node, Node> map = new HashMap<>();
    
    public Node cloneGraph(Node node) {
        return clone(node);
    }
    
    Node clone(Node node) {
        //If node doesn't exist or is already accounted for
        if (node == null || map.containsKey(node)) {
            return map.get(node);
        }
        
        Node copy = new Node(node.val);
        map.put(node, copy);
        
        for (Node neighbor: node.neighbors) {
            copy.neighbors.add(clone(neighbor));
        }
        return copy;
    }
}