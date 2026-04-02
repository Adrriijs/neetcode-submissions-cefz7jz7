class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = ''.join(c for c in s if c.isalnum())
        new_str = new_str.lower()

        for i in range(len(new_str) // 2):
            # check if left and right is the same
            if new_str[i] != new_str[-i-1]:
                return False
        
        return True
