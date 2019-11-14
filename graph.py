import math

class Node:
  """
  args:
    id (str)
    pos (dic) : position of the Node in the MEAOO City
    edges (list) : outgoing edges for this Node
  """

  def __init__(self, id, pos, edges):
    self.id = id
    self.pos = pos
    self.edges = edges

class Edge:
  """
  args:
    id (str)
    start (Node) :
    end (Node)
    factor (int) : circultation factor in case of pertubation
    dist (double) : length of the Edge
  """

  def __init__(self, id, start, end):
    self.id = id
    self.start = start
    self.end  = end
    self.factor = 1
    self.dist = self.get_dist()

  def get_dist(self):
    """Compute the length fo the Edge using Euclidean distance"""
    return math.sqrt((this.start.pos['x'] - this.end.pos['x'])**2 +
                     (this.start.pos['y'] - this.end.pos['y'])**2)

class Graph:
  """
  args :
    nodes (dic) : list of nodes in the Graph accessible by id
    edges (dic) : list of edges in the Graph accessible by id
  """

  def __init__(self):
    self.nodes = {}
    self.edges = {}

  def build(self, jsons):
    """Read the Json files and fill the nodes and edges
    args :
      jsons : list of jsons files containing the graphs informations
    """
    # TODO: maybe use the api to get the jsons and not files
    pass

  def update_circulation(self, json):
    """Update the graph information using the json string gived by MEAOO Api
    args :
      json : json string containing the ciculation information
    """
    # TODO: don't forget to reset the previous changes
    # Option 1 : go throw all edges to reset value : + memory - speed
    # Option 2 : use stored copy of initial graph : + speed - memory
    pass
