import json
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse

import constante as CONST
from graph import Graph

graph = None

class Route(Resource):
    def __init__(self):
        super().__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('start', type=str)
        self.parser.add_argument('dest', type=str)

    def get(self):
        args = self.parser.parse_args()
        start = json.load(args['start'])
        dest = json.load(args['dest'])
        return {'Route': [args['starting_point'], args['destination']]}

def request_graph():
  jsons = {}
  for transp in CONST.TRANSPORTATION:
    URL = CONST + "/processed/v2/{}.json".format(transp)
    r = requests.get(url=URL)
    jsons[transp] = r.json()

  graph = Graph()
  graph.build([json for json in jsons.values()])
  # TODO: do some stuff with the graph
  return graph

def setup_api():
  app = Flask(__name__)
  api = Api(app)
  api.add_resource(Route, '/route')
  return api

if __name__ == '__main__':
  global graph = request_graph()
  api = setup_api()
  app.run(debug=True, host='0.0.0.0')
