class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ord(a) = 97

        why tupple: immutable and hashable
        """
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())
