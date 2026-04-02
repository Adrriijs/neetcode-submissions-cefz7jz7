class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        res = []
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            visit.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            if crs not in res:
                res.append(crs)
                
            visit.remove(crs)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
        




