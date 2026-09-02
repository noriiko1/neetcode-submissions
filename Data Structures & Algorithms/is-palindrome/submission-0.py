class Solution:
    def isPalindrome(self, s: str) -> bool:
        daStr = ""

        for c in range(len(s)):
            if s[c].isalnum():
                daStr += s[c].lower()

        L, R = 0, len(daStr) - 1
        if len(s) == 0:
            return True
        while L < R:
            if daStr[L] != daStr[R]:
                return False
            L += 1
            R -= 1
        return True
            