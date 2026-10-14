class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sC, tC = {}, {}
        for e in range(len(s)):
            sC[s[e]] = 1 + sC.get(s[e],0)
            tC[t[e]] = 1 + tC.get(t[e],0)
        return sC == tC
        