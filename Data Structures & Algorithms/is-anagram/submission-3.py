class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqS = {}
        freqT = {}

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]

            freqS[charS] = 1 + freqS.get(charS, 0)
            freqT[charT] = 1 + freqT.get(charT, 0)
        
        return freqS == freqT
