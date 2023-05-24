import tkinter as tk
from tkinter import filedialog
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math


class Utils:
    graph_position = {}
    def checkValid(adjecencyMatrix: list[list[str]]) -> str:
        if (len(adjecencyMatrix)-2 < 8 or len(adjecencyMatrix[0]) < 8):
            return "too_small"
        elif (len(adjecencyMatrix)-2 != len(adjecencyMatrix[0])):
            return "size_diff"
        elif (len(adjecencyMatrix[len(adjecencyMatrix)-2]) != len(adjecencyMatrix[0])):
            return "name_not_enough"
        elif (len(adjecencyMatrix[len(adjecencyMatrix)-1]) != len(adjecencyMatrix[0])):
            return "coordinate_not_enough"
        for i in range (len(adjecencyMatrix)-2):
            for j in range (len(adjecencyMatrix[0])):
                if (not adjecencyMatrix[i][j].replace('.', '').isdigit()):
                    return "not_number"
        return "valid"

    def readFile() -> list[list[float]] and list[str] and list[(float,float)] and bool:
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfile()
        adjacencyMatrix = [[num.strip() for num in line.split(' ')] for line in file]
        nameList = adjacencyMatrix[len(adjacencyMatrix)-2]
        coordinateList = [eval(elmt) for elmt in adjacencyMatrix[len(adjacencyMatrix)-1]]
        file.close()
        status = Utils.checkValid(adjacencyMatrix)
        valid : bool

        if (status == "valid"):
            valid = True
            adjacencyMatrix = adjacencyMatrix[0:len(adjacencyMatrix)-2]
            adjacencyMatrix = [list(map(float, x)) for x in adjacencyMatrix]
            print("File valid")
        else:
            valid = False
            if (status == "too_small"):
                print("Ukuran matrix minimal 8 x 8")
            elif (status == "size_diff"):
                print("Ukuran baris dan kolom harus sama")
            elif (status == "name_not_enough"):
                print("Jumlah nama tidak sesuai dengan jumlah simpul")
            elif (status == "coordinate_not_enough"):
                print("Jumlah koordinat tidak sesuai dengan jumlah simpul")
            else:
                print("Matrix hanya dapat berupa angka")

        return adjacencyMatrix, nameList, coordinateList, valid

    def matrixToMap(adjacencyMatrix: list[list[float]], nameList : list[str]) -> dict[(str,list[(str,float)])]:
        graphMap : dict
        graphTuple : list[str,list[(str,float)]] = []
        neighbour : list[(str,float)] = []
        for i in range (len(nameList)):
            for j in range (len(adjacencyMatrix[i])):
                if (adjacencyMatrix[i][j] != 0):
                    neighbour.append((nameList[j],adjacencyMatrix[i][j]))
            graphTuple.append((nameList[i], neighbour.copy()))
            neighbour.clear()

        graphMap = dict(graphTuple)
        return graphMap                   

    def drawGraph(adjacencyMatrix: list[list[float]], nameList : list[str], coordinateList : list[(float,float)]):
        G = nx.Graph()
        i = 0
        for name in nameList:
            G.add_node(name, position=(coordinateList[i][0], coordinateList[i][1]))
            i += 1
 
        for i in range (len(nameList)):
            for j in range (len(adjacencyMatrix[i])):
                if (adjacencyMatrix[i][j] != 0):
                    G.add_edge(nameList[i], nameList[j], weight = adjacencyMatrix[i][j])

        pos = nx.get_node_attributes(G, 'position')
        Utils.graph_position = pos
        print(pos)
        nx.draw_networkx_nodes(G, pos, node_size=[len(v) * 3000 for v in G.nodes()])
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=10)
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=20)
        # nx.draw(G, pos, with_labels=True)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def showPath(adjacencyMatrix: list[list[float]], nameList : list[str], coordinateList : list[(float,float)], path : list[str]):
        G = nx.Graph()
        i = 0
        for name in nameList:
            G.add_node(name, position=(coordinateList[i][0], coordinateList[i][1]))
            i += 1

        for i in range (len(nameList)):
            for j in range (len(adjacencyMatrix[i])):
                if (adjacencyMatrix[i][j] != 0):
                    G.add_edge(nameList[i], nameList[j], weight = adjacencyMatrix[i][j])

        ePath = []
        for i in range (len(path)-1):
            ePath.append((path[i], path[i+1]))
        eNotPath = [(u, v) for (u, v, d) in G.edges(data=True) if (u, v) not in ePath]

        pos = nx.get_node_attributes(G, 'position')
        nx.draw_networkx_nodes(G, pos, node_size=[len(v) * 3000 for v in G.nodes()])

        nx.draw_networkx_edges(G, pos, edgelist=eNotPath, width=10)
        nx.draw_networkx_edges(G, pos, edgelist=ePath, width=10, edge_color="violet")

        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=20)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def euclideanDistance(a: tuple[float,float], b: tuple[float,float]) -> float:
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    
    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        # convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        # 6371 km is the radius of the Earth
        km = 6371 * c
        return km