class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seenNumbers = {}

        for i in range(n):
            num = nums[i]
            complement = target - num
            if complement in seenNumbers: 
                return [seenNumbers[complement], i]
            else:
                seenNumbers[num] = i
            