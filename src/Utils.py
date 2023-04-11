import tkinter as tk
from tkinter import filedialog
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Utils:
    def checkValid(adjecencyMatrix: list[list[str]]) -> str:
        if (len(adjecencyMatrix)-1 < 8 or len(adjecencyMatrix[0]) < 8):
            return "too_small"
        elif (len(adjecencyMatrix)-1 != len(adjecencyMatrix[0])):
            return "size_diff"
        for i in range (len(adjecencyMatrix)-1):
            for j in range (len(adjecencyMatrix[0])):
                if (not adjecencyMatrix[i][j].isdigit()):
                    return "not_number"
        return "valid"

    def readFile() -> list[list[int]] and list[str] and bool:
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfile()
        adjacencyMatrix = [[num.strip() for num in line.split(',')] for line in file]
        nameList = adjacencyMatrix[len(adjacencyMatrix)-1]
        file.close()
        status = Utils.checkValid(adjacencyMatrix)
        valid : bool

        if (status == "valid"):
            adjacencyMatrix = adjacencyMatrix[0:len(adjacencyMatrix)-1]
            adjacencyMatrix = [list(map(int, x)) for x in adjacencyMatrix]
            print("File valid")
            valid = True
        elif (status == "too_small"):
            print("Ukuran matrix minimal 8 x 8")
            valid = False
        elif (status == "size_diff"):
            print("Ukuran baris dan kolom harus sama")
            valid = False
        else:
            print("Matrix hanya dapat berupa angka")
            valid = False

        return adjacencyMatrix, nameList, valid

    def matrixToMap(adjacencyMatrix: list[list[int]], nameList : list[str]) -> dict[(str,list[(str,int)])]:
        graphMap : dict
        graphTuple : list[str,list[(str,int)]] = []
        neighbour : list[(str,int)] = []
        for i in range (len(nameList)):
            for j in range (len(adjacencyMatrix[i])):
                if (adjacencyMatrix[i][j] != 0):
                    neighbour.append((nameList[j],adjacencyMatrix[i][j]))
            graphTuple.append((nameList[i], neighbour.copy()))
            neighbour.clear()

        graphMap = dict(graphTuple)
        return graphMap
                    

    def drawGraph(adjacencyMatrix: list[list[int]], nameList : list[str]):
        G = nx.Graph()
        for i in range (len(nameList)):
            for j in range (len(adjacencyMatrix[i])):
                if (adjacencyMatrix[i][j] != 0):
                    G.add_edge(nameList[i], nameList[j], weight = adjacencyMatrix[i][j])

        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=[len(v) * 3000 for v in G.nodes()])
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=10)
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=20)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def showPath(adjacencyMatrix: list[list[int]], nameList : list[str], path : list[str]):
        G = nx.Graph()
        for i in range (len(nameList)):
            for j in range (len(adjacencyMatrix[i])):
                if (adjacencyMatrix[i][j] != 0):
                    G.add_edge(nameList[i], nameList[j], weight = adjacencyMatrix[i][j])

        ePath = []
        for i in range (len(path)-1):
            ePath.append((path[i], path[i+1]))
        eNotPath = [(u, v) for (u, v, d) in G.edges(data=True) if (u, v) not in ePath]

        pos = nx.spring_layout(G, seed=7)
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