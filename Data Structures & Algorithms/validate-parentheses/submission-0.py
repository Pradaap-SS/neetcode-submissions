class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in matching:         # it's a closing bracket
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:                        # it's an opening bracket
                stack.append(char)

        return len(stack) == 0