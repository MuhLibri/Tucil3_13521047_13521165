class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        if (self.isEmpty()):
            self.queue.append(data)
        else:
            i : int = 0
            while (i < len(self.queue) and data[1] > self.queue[i][1]):
                i += 1
            self.queue.insert(i, data)

    def dequeue(self):
        return self.queue.pop(0)