from Utils import *

adjacencyMatrix, valid = Utils.readFile()
while (not valid):
    print("Silahkan Masukkan file yang valid")
    adjacencyMatrix, valid = Utils.readFile()


nodeDict,nameList = Utils.nameNode(False, 8)
Utils.drawGraph(adjacencyMatrix, nameList)