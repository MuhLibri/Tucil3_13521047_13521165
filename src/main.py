from Utils import *
from UCS import *
from AStar import *
from Map import *

graphMode = input('Masukkan mode yang diinginkan (peta/file)')
if(graphMode=='file'):
    adjacencyMatrix, nameList, coordinateList, valid = Utils.readFile()
    while (not valid):
        print("Silahkan masukkan file yang valid")
        adjacencyMatrix, nameList, coordinateList, valid = Utils.readFile()


    Utils.drawGraph(adjacencyMatrix, nameList, coordinateList)
    map = Utils.matrixToMap(adjacencyMatrix, nameList)

    origin = input("Masukkan simpul asal: ")
    destination = input("Masukkan simpul tujuan: ")

    searchMode = input('Masukkan mode searching(ucs/astar): ')
    if(searchMode=='ucs'):
        distance, path = UCS.findUCS(origin, destination, map, nameList)
    elif(searchMode=='astar'):
        astar = AStar(map)
        distance, path = astar.solve(origin, destination)


    print("Jarak dari simpul", origin, "ke simpul", destination, "adalah", distance)
    Utils.showPath(adjacencyMatrix, nameList, coordinateList, path)
elif(graphMode == 'peta'):
    ay, ax = map(float, input('Masukkan (latitude,longtude) awal: ').split(','))
    by, bx = map(float, input('Masukkan (latitude,longtude) tujuan: ').split(','))

    origin = (ay,ax)
    destination = (by,bx)

    searchMode = input('Masukkan mode(ucs/astar/default): ')

    mappeta = Map(origin, destination, searchMode)

    print("Jarak dari ", origin, "ke ", destination, "adalah", mappeta.distance)

    mappeta.plot()



# astar = AStar(map)
# distance, path = astar.solve(origin, destination)
# print(path)

# distance, path = UCS.findUCS(origin, destination, map, nameList)
