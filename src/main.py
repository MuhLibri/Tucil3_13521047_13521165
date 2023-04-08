from Utils import *

adjacencyMatrix, valid = Utils.readFile()
while (not valid):
    print("Silahkan Masukkan file yang valid")
    adjacencyMatrix, valid = Utils.readFile()

inputManual = input("Apakah ingin menamai simpul? (y/n)\n")
while (inputManual not in ["y","Y","n","N"]):
    print("Masukan salah")
    inputManual = input("Apakah ingin menamai simpul? (y/n)\n")

if (inputManual == "y" or inputManual == "Y"):
    nodeDict,nameList = Utils.nameNode(True, 8)
else:
    nodeDict,nameList = Utils.nameNode(False, 8)


a = Utils.matrixToMap(adjacencyMatrix, nameList)
print(a)
Utils.drawGraph(adjacencyMatrix, nameList)