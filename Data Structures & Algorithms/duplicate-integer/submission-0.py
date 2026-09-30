class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_duplicates = set()
        for num in nums:
            if num in seen_duplicates:
                return True
            seen_duplicates.add(num)

        return False