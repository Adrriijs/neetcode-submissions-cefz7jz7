class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")
            elif p == "(":
                stack.append(")")
            else:
                if not stack or p != stack.pop():
                    return False
        
        return len(stack) == 0