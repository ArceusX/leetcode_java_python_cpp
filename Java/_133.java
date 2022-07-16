//Breadth first: with queue
class Solution {
  public Node cloneGraph(Node node) {
    if (node == null)
      return null;

    //queue tracks original nodes we still need to traverse.
    Queue<Node> queue = new ArrayDeque<>(Arrays.asList(node));

    //map references new copies with old node as key
    Map<Node, Node> map = new HashMap<>();
    map.put(node, new Node(node.val));

    while (!queue.isEmpty()) {
      Node x = queue.poll();
      for (Node neighbor : x.neighbors) {

        // If True: Create copy, store it and old node in map,
        // assign it to be traversed in queue
        if (!map.containsKey(neighbor)) {
          map.put(neighbor, new Node(neighbor.val));
          queue.add(neighbor);
        }

        //Log neighbor into neighbors of new copy
        map.get(x).neighbors.add(map.get(neighbor));
      }
    }

    return map.get(node);
  }
}