class Solution:
    """
    simple encode and decode
    n#word n for the length, # just seperator

    hello, world = 5#hello5#world
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    """
    convert number first i to j
    """

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        
        return res
