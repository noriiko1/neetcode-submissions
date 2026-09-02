class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        u = ''.join(sorted(s))
        v = ''.join(sorted(t))
        if u == v:
            return True
        else:
            return False