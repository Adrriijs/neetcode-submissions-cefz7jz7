class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Counter bikin hashmap freq out of string
        """

        map_s = Counter(s)
        map_t = Counter(t)

        return map_s == map_t