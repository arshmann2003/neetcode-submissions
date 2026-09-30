class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        n = len(s)
        m = len(t)

        if n!=m:
            return False

        map_s = {}
        map_t = {}

        for i in range(n):
            letter = s[i]
            if letter in map_s:
                map_s[letter] += 1
            else:
                map_s[letter] = 1
        
        for i in range(m):
            letter = t[i]
            if letter in map_t:
                map_t[letter] += 1
            else:
                map_t[letter] = 1

        for i in range(m):
            letter = t[i]
            if letter in map_s and map_s[letter] == map_t[letter]:
                continue
            else:
                return False 
                
        return True
            

        
