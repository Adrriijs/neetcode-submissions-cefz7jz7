class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        visit = set()
        done = set()

        def dfs(crs):
            if crs in visit:
                return False
            if crs in done:
                return True
            
            if preMap[crs] == []:
                res.append(crs)

            visit.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            visit.remove(crs)
            done.add(crs)
            res.append(crs)

            return True
            
        for crs in preMap:
            if dfs(crs) == False:
                return []

        return res