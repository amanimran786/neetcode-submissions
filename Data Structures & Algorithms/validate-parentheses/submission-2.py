class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            # if it's an opening bracket, push onto stack
            if char in pairs.values():
                stack.append(char)
            # if it's a closing bracket
            elif char in pairs:
                # if no opening bracket or mismatch → invalid
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        # if stack is empty, everything was matched
        return len(stack) == 0
