# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where 
# different letters represent different tasks. Tasks could be done without original order. 
# Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there 
# must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

from collections import deque
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        q = deque(maxlen=n)
        heap = self.buildHeap(tasks)
        result = []
        while heap:
            temp = []
            done = False
            print('heap ', heap)
            while not done:
                if heap:
                    count, task = heappop(heap)
                    count = -1*count
                    if task not in q:
                        q.append(task)
                        count -= 1
                        result.append(task)
                        done = True
                    if count > 0:
                        temp.append((count*-1, task))
                else:
                    result.append('#')
                    q.append('#')
                    done = True
                print(result)
            for item in temp:
                heappush(heap, item)
        return result

    def buildHeap(self, tasks):
        heap = []
        dict = {}
        for c in tasks:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for key, val in dict.items():
            heappush(heap, (-val, key))
        return  heap


tasks = ["A","A","A","B","B","B"]
n = 2
# tasks = ["A","A","A","B","C","D","E"]
# n = 2
ans = Solution().leastInterval(tasks, n)
print(len(ans), ans)
