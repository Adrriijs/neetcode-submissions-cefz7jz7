class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        answer = []

        for s in strs:
            key = "".join(sorted(s))
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        
        for key in hashmap:
            answer.append(hashmap[key])

        return answer
