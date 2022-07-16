class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
      return None

    queue = deque([node])
    map = {node: Node(node.val)}

    while queue:
      u = queue.popleft()
      for neighbor in u.neighbors:
        if neighbor not in map:
          map[neighbor] = Node(neighbor.val)
          queue.append(neighbor)
        map[u].neighbors.append(map[neighbor])

    return map[node]