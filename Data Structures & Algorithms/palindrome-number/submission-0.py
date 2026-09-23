class Solution:
    def isPalindrome(self, x: int) -> bool:
        L, R = 0,len(str(x)) - 1
        pali = str(x)
        while L < R:
            if pali[L] != pali[R]:
                return False
            else:
                L += 1
                R -= 1
        return True