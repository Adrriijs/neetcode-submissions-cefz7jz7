class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(1, len(edges) + 1)}

        def bfs(start, target):
            visit = set()                   
            q = deque()
            q.append(start)
            visit.add(start)

            while q:
                curNode = q.popleft()
                if curNode == target:
                    return True

                for nei in graph[curNode]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)

            return False

        for a,b in edges:
            if bfs(a,b):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)
        
        return []
            