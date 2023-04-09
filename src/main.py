from Utils import *
from UCS import *

adjacencyMatrix, valid = Utils.readFile()
while (not valid):
    print("Silahkan Masukkan file yang valid")
    adjacencyMatrix, valid = Utils.readFile()

inputManual = input("Apakah ingin menamai simpul? (y/n)\n")
while (inputManual not in ["y","Y","n","N"]):
    print("Masukan salah")
    inputManual = input("Apakah ingin menamai simpul? (y/n)\n")

if (inputManual == "y" or inputManual == "Y"):
    nodeDict,nameList = Utils.nameNode(True, len(adjacencyMatrix))
else:
    nodeDict,nameList = Utils.nameNode(False, len(adjacencyMatrix))

Utils.drawGraph(adjacencyMatrix, nameList)
map = Utils.matrixToMap(adjacencyMatrix, nameList)

origin = input("Masukkan simpul asal: ")
destination = input("Masukkan simpul tujuan: ")
distance, path = UCS.findUCS(origin, destination, map, nameList)
print("Jarak dari simpul", origin, "ke simpul", destination, "adalah", distance)

Utils.showPath(adjacencyMatrix, nameList, path)