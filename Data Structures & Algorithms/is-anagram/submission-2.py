class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create two hashmaps and count letter frequency, compare hashmaps to see if they are the same 
        if len(s) != len(t):
            return False

        sCount = {}
        tCount = {}
        
        for c in s:
            if c in sCount: 
                sCount[c] += 1
            else: 
                sCount[c] = 1
        
        for c in t:
            if c in tCount:
                tCount[c] += 1
            else:
                tCount[c] = 1

        for c in s:
            if c in tCount and sCount[c] == tCount[c]:
                continue
            else:
                return False

        return True
