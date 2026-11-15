class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seenNums = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in seenNums:
                j = 1
                consecutive = 1
                while nums[i] + j in seenNums:
                    consecutive += 1
                    j += 1
                longest = max(longest, consecutive)
        return longest

            






