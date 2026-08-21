class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                
                opening = stack.pop()
                if char == ")" and opening != "(":
                    return False
                if char == "]" and opening != "[":
                    return False
                if char == "}" and opening != "{":
                    return False
        return len(stack) == 0