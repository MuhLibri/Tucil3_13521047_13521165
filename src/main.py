from Utils import *
from UCS import *

adjacencyMatrix, nameList, valid = Utils.readFile()
while (not valid):
    print("Silahkan Masukkan file yang valid")
    adjacencyMatrix, nameList, valid = Utils.readFile()

#                   1      2      3      4      5      6      7      8
coordinateList = [(0,0),(0,-11),(2,0),(13,13),(0,10),(3,13),(0,20),(0,13)]
Utils.drawGraph(adjacencyMatrix, nameList, coordinateList)
map = Utils.matrixToMap(adjacencyMatrix, nameList)

origin = input("Masukkan simpul asal: ")
destination = input("Masukkan simpul tujuan: ")
distance, path = UCS.findUCS(origin, destination, map, nameList)
print("Jarak dari simpul", origin, "ke simpul", destination, "adalah", distance)

Utils.showPath(adjacencyMatrix, nameList, path)