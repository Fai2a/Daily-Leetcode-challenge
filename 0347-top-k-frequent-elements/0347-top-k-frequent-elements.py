class Solution:
    def topKFrequent(self, A, k):
        q = []

        for n, v in Counter(A).items():
            heapq.heappush(q, [v, n])

            if len(q) > k:
                heapq.heappop(q)

        res = []

        while q:
            v, n = heapq.heappop(q)
            res.append(n)
        return res