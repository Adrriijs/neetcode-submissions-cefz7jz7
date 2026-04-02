class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        h = {}
        len_s = 0

        for r in range(len(s)):
            h[s[r]] = 1 + h.get(s[r], 0)
            len_s = max(len_s, h[s[r]])

            while (r - l + 1) - len_s > k:
                h[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res