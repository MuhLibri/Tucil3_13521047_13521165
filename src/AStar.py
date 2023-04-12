from PriorityQueue import PriorityQueue
from Utils import Utils

class AStar:
    def __init__(self, _graph: dict) -> None:
        self.graph: dict = _graph
        # self.nameList: list[str] = _nameList
        self.q: PriorityQueue = PriorityQueue()
        self.goal: str = ""
        self.current: tuple[str, float, list[str], float] = tuple() # (CurrentNode, fn, Path, costSoFar)

    def solve(self, origin: str, destination: str) -> tuple[float, list[str]]:
        self.goal = destination
        self.q = PriorityQueue()
        self.current = (origin, AStar.sld(origin, destination), [origin], 0)
        self.q.enqueue(self.current)

        while(not(self.q.getLowestPriorityKey() > self.current[1] and self.current[0]==self.goal)):
            self.current = self.q.dequeue()
            currentNode, fn, path, costSoFar = self.current
            # print(self.current)
            for neighbor in self.graph[currentNode]:
                tempPath = path.copy()
                tempPath.append(neighbor[0])
                self.q.enqueue((neighbor[0], self.heuristic_fn(neighbor[0], neighbor[1]), tempPath, costSoFar+neighbor[1]))
            # print(self.q)
            # print('=============')
        
        return self.current[3], self.current[2]




    def heuristic_fn(self, origin: str, weight: float) -> float:
        cost_so_far = self.current[3] + weight
        estimated_cost_to_goal = AStar.sld(origin, self.goal)
        return cost_so_far + estimated_cost_to_goal


    @staticmethod
    def sld(origin: str, destination: str) -> float:
        return Utils.euclideanDistance(Utils.graph_position[origin], Utils.graph_position[destination])
