class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for eff, spd in zip(efficiency, speed):
            eng.append((eff,spd))
        eng.sort(reverse=True) #sort eff in decreasing order

        res, total_speed = 0, 0
        minHeap = []

        for eff, spd in eng:
            if len(minHeap) == k: #minHeap stores k speeds
                total_speed -= heapq.heappop(minHeap)
            total_speed += spd
            heapq.heappush(minHeap, spd)
            res = max(res, eff*total_speed)
        
        return res % (10 ** 9+7)