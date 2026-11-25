class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        w = strs[i]

        while i < len(w):
            validLetter = True
            for j in range(1, len(strs)):
                word = strs[j]
                if len(word)-1 < i or word[i] != w[i]:
                    validLetter = False
                    break
            if not validLetter:
                return res
            else:
                res += w[i]
                i += 1
        return res

                

        
            