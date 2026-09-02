class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 0:
            return True

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif c == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif c == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                return False
        return len(stack) == 0