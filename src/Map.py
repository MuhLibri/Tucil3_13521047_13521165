import osmnx as ox
import networkx as nx
from shapely.geometry import Point, LineString
import folium
import math
from AStar import AStar
from UCS import UCS
from Utils import Utils

class Map:
    def __init__(self, origin, destination, mode):
        ox.settings.use_cache = True

        self.origin = origin
        self.destination = destination

        y1, x1 = origin
        y2, x2 = destination
        distance = Utils.haversine(y1, x1, y2, x2)*1000
        # distance = 1000
        print(distance)

        g1 = ox.graph_from_point(origin, dist=distance, network_type='drive')
        g1 = ox.distance.add_edge_lengths(g1)
        g1 = Map.snap_node(origin, g1, id=1)
        # g1 = ox.distance.add_edge_lengths(g1, edges = new_edges)

        g2 = ox.graph_from_point(destination, dist=distance, network_type='drive')
        g2 = ox.distance.add_edge_lengths(g2)
        g2 = Map.snap_node(destination, g2, id=2)
        # g2 = ox.distance.add_edge_lengths(g2, edges=new_edges)

        self.graph = nx.compose(g1, g2)
        # self.graph = ox.distance.add_edge_lengths(G)
        # print(self.graph.edges[2,1857160454,0]['length'])
        # print(self.graph.edges[1,32524043,0]['length'])

        # graph = {node: [((x,y), weight)]}
        
        print(self.graph)
        self.distance = 0
        if(mode=='astar' or mode=='ucs'):
            pos = {}
            
            newGraph = {}
            for node in self.graph.nodes:
                # listName = [e for e in self.graph.edges()[0] if node in e]
                # print(self.graph.nodes[node])
                pos.update({str(node): (self.graph.nodes[node]['y'], self.graph.nodes[node]['x'])})


                listName = [e for e in self.graph.edges() if e[0] == node]
                neighbours = []
                for neighbour in listName:
                    # print(node)
                    # print(neighbour)
                    if neighbour[0]==node:
                        neighbour = neighbour[1]
                    else:
                        neighbour = neighbour[0]
                    # print(self.graph.edges[node,neighbour,0]['length'])
                    neighbours.append((str(neighbour), self.graph.edges[node,neighbour,0]['length']))
                newGraph.update({str(node): neighbours})
            Utils.graph_position = pos
        if(mode=='astar'):
            astar = AStar(newGraph, map=True)
            self.distance, paths = astar.solve('1', '2')
            newPaths = []
            for path in paths:
                newPaths.append(int(path))
        elif(mode=='ucs'):
            nameList = newGraph.keys()
            self.distance, paths = UCS.findUCS('1', '2', newGraph, nameList)
            newPaths = []
            for path in paths:
                newPaths.append(int(path))
        elif(mode=='default'):
            newPaths = ox.shortest_path(self.graph, 1, 2)
        
        self.route = newPaths

    
    @staticmethod
    def snap_node(point, G, id):
        (u, v, key), dist = ox.distance.nearest_edges(G, point[1], point[0], return_dist=True)
        edge = G.edges[(u,v,key)]['geometry']
        pt = Point(point[1], point[0])
        closest_point = edge.interpolate(edge.project(pt))
        new_node = {
            'y': closest_point.coords[0][1],
            'x': closest_point.coords[0][0],
            'street_count': 1
        }
        G.add_node(id, **new_node)

        ug = G.nodes[u]
        vg = G.nodes[v]
        # print(G.nodes[id])
        # print(ug)
        # print(vg)
        # print('=======')

        G.add_edge(id, u, key=0, length=1000*Utils.haversine(new_node['y'], new_node['x'], ug['y'], ug['x']))
        G.add_edge(u, id, key=0, length=1000*Utils.haversine(ug['y'], ug['x'],new_node['y'], new_node['x']))
        G.add_edge(id, v, key=0, length=1000*Utils.haversine(new_node['y'], new_node['x'], vg['y'], vg['x']))
        G.add_edge(v, id, key=0, length=1000*Utils.haversine(vg['y'], vg['x'],new_node['y'], new_node['x']))
        return G


    def plot(self):
        m = folium.Map(location=self.origin, zoom_start=12)
        ox.plot_route_folium(self.graph, self.route, route_map=m)
        m.show_in_browser()

    


# map = Map((-6.89323,107.61037), (-6.89150,107.61329))
# map.plot()