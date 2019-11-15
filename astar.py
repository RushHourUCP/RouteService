class NodeAStar:
  """
  args:
    graph_node (Node) : assossiated node in the graph
    parent (dic) : 'node'-parent node, 'path'-path taken to come from the parent node
    g (double) : cost of the path to go to this node
    h (double) : heuritic, estimation to go the goal
    f (double) : final cost value
  """

  def __init__(self, graph_node):
    self.graph_node = graph_node
    self.parent = None
    self.g = 0
    self.h = 0
    self.f = 0

  def __equal__(self, other):
    return (self.graph_node.pos['x'] == other.graph_node.pops['x'] and
            self.graph_node.pos['y'] == other.graph_node.pops['y'])

  def __alternative_equal__(self, other):
    return self.graph_node.id == other.graph_node.id

  def __distance_to_goal(self, goal_node):
    """Compute the heuristique"""
    self.h = math.sqrt((this.graph_node.pos['x'] - goal_node.pos['x'])**2 +
                       (this.graph_node.pos['y'] - goal_node.pos['y'])**2)

  def __compute_g(self):
    """"""
    # TODO: faire la fonction enfaite
    pass

  def compute_cost(self, goal):
    """Compute the cost of a node
    agrs:
      goal (Node) : target node for A*
    """
    self.__distance_to_goal(goal)
    self.__compute_g()
    self.f = self.g + self.h

def AStar(graph, start, end):
  """
  args:
    graph (Graph) :
    start (str) :
    end (str) :
  """

  def extract_best_node(node_list):
    if(not list):
      return None
    best_node = node_list[0]
    best_idx = 0
    for i, node in enumerate(node_list):
      if(node.graph_node.f < best_node.graph_node.f):
        best_node = node
        best_idx = i
    node_list.pop(best_idx)
    return best_node

  openList = []
  closeList = []
  start_node = NodeAStar(graph.nodes[start])
  end_node = NodeAStar(graph.nodes[end])

  curr_node = start_node
  curr_node.compute_cost(graph.nodes[end])
  openList.append(curr_node)

  while(openList):
    curr_node = extract_best_node(openList)
    closeList.append(curr_node)

    if curr_node == end_node:
      n = curr_node
      final_path = []
      while curr_node.parent :
        final_path.append(curr_node)
        curr_node = curr_node.parent['node']
      return final_path.reverse()

    childrens = [{'node':Astar(edge.end), 'path':edge}
                 for edge in curr_node.graph_node.edges]

    for child in childrens:

      if child['node'] in closeList:
        continue

      # child['node']
      # TODO: can't add the node to closeList because don't have the edge information
