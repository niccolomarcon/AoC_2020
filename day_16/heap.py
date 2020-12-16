import heapq


class Heap:
    def __init__(self, values_weights_list):
        self.heap = []
        self.pos = {}
        for v, w in values_weights_list:
            self.push(v, w)

    @property
    def empty(self):
        return len(self.heap) == 0

    def push(self, value, weight):
        self.pos[value] = item = [weight, value]
        heapq.heappush(self.heap, item)

    def pop(self):
        _, value = heapq.heappop(self.heap)
        del self.pos[value]
        return value

    def update(self, value, weight):
        self.pos[value][0] = weight
        heapq.heapify(self.heap)

    def __iter__(self):
        return self.pos.keys().__iter__()
