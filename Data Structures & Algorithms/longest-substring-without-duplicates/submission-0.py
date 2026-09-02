class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt, L = 0,0
        chk = set()

        for R in range(len(s)):
            while s[R] in chk:
                chk.remove(s[L])
                L += 1
            chk.add(s[R])
            cnt = max(cnt, R - L + 1)
        return cnt