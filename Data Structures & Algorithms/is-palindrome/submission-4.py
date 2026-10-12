class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char for char in s if char.isalnum())
        clean_text = clean_text.lower()

        l, r = 0, len(clean_text) - 1

        while l < r:
            if clean_text[l] != clean_text[r]:
                return False
            l += 1
            r -= 1
        
        return True
