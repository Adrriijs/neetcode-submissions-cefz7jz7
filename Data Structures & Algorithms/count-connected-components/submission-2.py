class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        res = 0

        def bfs(node):
            q = deque()
            q.append(node)
            visit.add(node)

            while q:
                curNode = q.popleft()

                for nei in graph[curNode]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
                
        for node in range(n):
            if node not in visit:
                bfs(node)
                res += 1
        
        return res
