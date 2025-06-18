class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        for node in range(len(graph)):
            if color[node] != 0: #check if node is explored using BFS
                continue
            queue = deque()
            queue.append(node)
            color[node] = 1

            while queue: #BFS 
                curr = queue.popleft()

                for nei in graph[curr]: 
                    if color[nei] == 0:
                        color[nei] = -color[curr]
                        queue.append(nei)
                    elif color[nei] != -color[curr]:
                        return False
        
        return True
