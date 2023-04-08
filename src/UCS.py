from PriorityQueue import *

class UCS:
    def findUCS(origin : str, destination : str, map : dict, nameList : list[str]) -> int and list[str]:
        nodeStatus = [False for i in range(len(map))]
        nodeIsPassed = dict(zip(nameList, nodeStatus))
        ucsQueue = PriorityQueue()
        currentNode = origin
        currentNodeWeight = 0
        ucsQueue.enqueue((currentNode, currentNodeWeight, [currentNode]))

        while (currentNode != destination):
            currentNode, currentNodeWeight, currentNodePath = ucsQueue.dequeue()
            nodeIsPassed[currentNode] = True
            for neighbor in (map[currentNode]):
                if(not nodeIsPassed[neighbor[0]]):
                    nodePath = currentNodePath.copy()
                    nodePath.append(neighbor[0])
                    ucsQueue.enqueue((neighbor[0], neighbor[1] + currentNodeWeight, nodePath))
            if (currentNode != destination):
                currentNodePath.clear()

        return currentNodeWeight, currentNodePath