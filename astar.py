class NodeAStare:
  """"""

  def __init__(self, graph_node):
    self.graph_node = graph_node
    self.parent = None

  def __equal__(self, other):
    return (self.graph_node.pos['x'] == other.graph_node.pops['x'] and
            self.graph_node.pos['y'] == other.graph_node.pops['y'])

  def __alternative_equal__(self, other):
    return self.graph_node.id == other.graph_node.id


def AStar(graph, start, end):
  """
  args:
    graph (Graph) :
    start (str) :
    end (str) :
  """

  openList = []
  closeList = []

  curr_node = NodeAStare(graph.nodes(start))
  openList.append(curr_node)

  
