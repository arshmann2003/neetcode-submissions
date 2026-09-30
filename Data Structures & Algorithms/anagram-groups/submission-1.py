class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through each word and use its sorted word as a key to lookup its group

        groups = {}

        n = len(strs)
        for i in range(n):
            word = strs[i]
            sorted_word = "".join(sorted(word))

            if sorted_word not in groups:
                groups[sorted_word] = []

            groups[sorted_word].append(word)

        return list(groups.values())
