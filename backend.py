import requests

import constante as CONST
from graph import Graph

def main():

  jsons = {}
  for transp in CONST.TRANSPORTATION:
    URL = CONST + "/processed/v2/{}.json".format(transp)
    r = requests.get(url=URL)
    jsons[transp] = r.json()


  graph = Graph()
  graph.build([json for json in jsons.values()])
  pass

if __name__ == '__main__':
  main()
