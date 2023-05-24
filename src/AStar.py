from PriorityQueue import PriorityQueue
from Utils import Utils

class AStar:
    def __init__(self, _graph: dict, map: bool = False) -> None:
        self.graph: dict = _graph
        # self.nameList: list[str] = _nameList
        self.q: PriorityQueue = PriorityQueue()
        self.goal: str = ""
        self.current: tuple[str, float, list[str], float] = tuple() # (CurrentNode, fn, Path, costSoFar)
        self._map = map

    def solve(self, origin: str, destination: str) -> tuple[float, list[str]]:
        self.goal = destination
        self.q = PriorityQueue()
        # print(AStar.sld(origin,destination))
        self.current = (origin, AStar.sld(origin, destination, map=self._map), [origin], 0)
        self.q.enqueue(self.current)

        count = 0

        while(not(self.q.getLowestPriorityKey() >= self.current[1] and self.current[0]==self.goal)):
            count+=1
            
            print(self.current[0] == self.goal)
            # print(self.q.getLowestPriorityKey())
            # print(self.current[1])
            # print('=============')

            # print(self.current)

            self.current = self.q.dequeue()
            currentNode, fn, path, costSoFar = self.current
            for neighbor in self.graph[currentNode]:
                tempPath = path.copy()
                tempPath.append(neighbor[0])
                self.q.enqueue((neighbor[0], self.heuristic_fn(neighbor[0], neighbor[1]), tempPath, costSoFar+neighbor[1]))
            # print(self.q)
            # print('=============')
        
        print('count: ', count)
        return self.current[3], self.current[2]




    def heuristic_fn(self, origin: str, weight: float) -> float:
        cost_so_far = self.current[3] + weight
        estimated_cost_to_goal = AStar.sld(origin, self.goal, map=self._map)
        # print(f'{cost_so_far} : {estimated_cost_to_goal}')
        # print(cost_so_far+estimated_cost_to_goal)
        return cost_so_far + estimated_cost_to_goal


    @staticmethod
    def sld(origin: str, destination: str, map: bool = False) -> float:
        # print(Utils.graph_position[origin])
        # print(Utils.graph_position[destination])
        # print('======================')
        if(map):
            og = Utils.graph_position[origin]
            dg = Utils.graph_position[destination]
            dist = Utils.haversine(og[0], og[1], dg[0], dg[1])*1000
        else:
            dist = Utils.euclideanDistance(Utils.graph_position[origin], Utils.graph_position[destination])
        # print(dist)
        return dist
