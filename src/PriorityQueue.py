from typing import TypeVar

T = TypeVar('T')

class PriorityQueue:
    def __init__(self) -> None:
        self.queue: list[T]  = []


    def __str__(self) -> str:
        return ' '.join([str(i) for i in self.queue])


    def isEmpty(self) -> bool:
        return len(self.queue) == 0


    def enqueue(self, data: T) -> None:
        if (self.isEmpty()):
            self.queue.append(data)
        else:
            i : int = 0
            while (i < len(self.queue) and data[1] > self.queue[i][1]):
                i += 1
            self.queue.insert(i, data)


    def dequeue(self) -> T:
        return self.queue.pop(0)


    def getLowestPriorityKey(self) -> float:
        return self.queue[0][1]
