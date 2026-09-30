class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through each word and use its sorted word as a key to lookup its group
        groups = {}

        for word in strs: 
            sortedWord = "".join(sorted(word))
            groups.setdefault(sortedWord, []).append(word)
          
        return list(groups.values())



            
        

