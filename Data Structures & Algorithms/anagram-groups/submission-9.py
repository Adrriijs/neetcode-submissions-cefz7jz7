class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        res = []

        for st in strs:
            sorted_text = "".join(sorted(st))
            if sorted_text in hm:
                hm[sorted_text].append(st)
            else:
                hm[sorted_text] = [st]
        
        for thing in hm:
            res.append(hm[thing])
        
        return res
