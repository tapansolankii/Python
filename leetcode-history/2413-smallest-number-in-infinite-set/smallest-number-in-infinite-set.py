import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1
        self.heap = []
        self.seen = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.heap:
            val = heapq.heappop(self.heap)
            self.seen.remove(val)
            return val
        
        val = self.current
        self.current += 1
        return val

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.current and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)
