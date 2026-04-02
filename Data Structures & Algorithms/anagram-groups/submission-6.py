class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        answer = []

        for s in strs:
            holder = "".join(sorted(s))
            if holder in hashmap:
                hashmap[holder].append(s)
            else:
                hashmap[holder] = [s]
        
        for key in hashmap:
            answer.append(hashmap[key])

        return answer
