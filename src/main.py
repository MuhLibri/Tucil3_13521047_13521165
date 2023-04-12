from Utils import *
from UCS import *

adjacencyMatrix, nameList, coordinateList, valid = Utils.readFile()
while (not valid):
    print("Silahkan Masukkan file yang valid")
    adjacencyMatrix, nameList, coordinateList, valid = Utils.readFile()


Utils.drawGraph(adjacencyMatrix, nameList, coordinateList)
map = Utils.matrixToMap(adjacencyMatrix, nameList)

origin = input("Masukkan simpul asal: ")
destination = input("Masukkan simpul tujuan: ")
distance, path = UCS.findUCS(origin, destination, map, nameList)
print("Jarak dari simpul", origin, "ke simpul", destination, "adalah", distance)

Utils.showPath(adjacencyMatrix, nameList, coordinateList, path)